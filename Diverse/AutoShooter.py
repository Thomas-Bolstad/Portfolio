import pyglet
import math
import random

from PIL import Image


def make_circle(x, y, radius, color):
    points = []
    pi = math.pi
    col = []
    for i in range(8):
        angle = 2 * pi * i / 4
        rx = math.cos(angle) * radius
        ry = math.sin(angle) * radius
        nx = x + rx
        ny = y + ry
        points.append(int(nx))
        points.append(int(ny))
        for j in color:
            col.append(j)
    l = int(len(points) / 2)
    # print(l, len(points), len(col))
    # print(points)
    points = tuple(points)
    col = tuple(col)
    # print(l, points, col)
    return pyglet.graphics.vertex_list(l, ('v2f', points), ('c3B', col))


class Base:
    black = 'c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    green = 'c3B', (0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0)

    def _graph(self):
        w = self.data["win"][0]
        x1 = int(w / 2 - 20)
        x2 = int(w / 2 + 20)
        y1, y2 = 0, 40
        quad = (x1, y1, x1, y2, x2, y2, x2, y1)
        gbase = pyglet.graphics.vertex_list(4, ('v2f', quad), self.green)
        self.data["g base"] = gbase

    def __init__(self, w, h):
        '''
        w = window width
        h = window height
        proj = instance of Project class
        '''
        self.data = {"x": w / 2, "y": 40, "win": (w, h), "frame": 0, "p speed": 10, "reload": 30, "last": -30,
                     "angle": 0, "targets": {}}
        self.angles = [0 for i in range(3600)]
        # self.data["proj"] = proj
        self._graph()

    def _add_target(self, i):
        targets = self.data["targets"]
        # pos = i.data["position"]
        # speed = i.data["speed"]
        targets[i] = i.data
        # targets[i]["pos"] = pos
        targets[i]["proj"] = False
        # targets[i]["speed"] = speed

    def _aim_target(self, i):
        targets = self.data["targets"]
        # sp = targets[i]["speed"]
        x, y = i.data["pos"]
        cx, cy = self.data["win"][0] / 2, 40
        vp = self.data["p speed"]
        vx, vy = i.data["speed"]
        # dx = pos[0] - self.data["win"][0]/2
        # dy = pos[1] - 40
        a = vx ** 2 + vy ** 2 - vp ** 2
        b = 2 * (vx * (x - cx) + vy * (y - cy))
        c = (x - cx) ** 2 + (y - cy) ** 2
        disc = b ** 2 - 4 * a * c
        # print(vp, a, b, c, b**2 , 4*a*c)
        t1 = random.random() * 3
        t2 = -1
        if disc >= 0:
            t1 = (-b + math.sqrt(disc)) / (2 * a)
            t2 = (-b - math.sqrt(disc)) / (2 * a)
        else:
            print(disc)
        t = t1
        if t1 < 0:
            t = t2
        if t2 < 0:
            t = t1
        if t1 < 0 and t2 < 0:
            t = min(t1, t2)
        return t * vx + x, t * vy + y

    def _draw_cannon(self):
        angle = self.data["angle"]
        pyglet.gl.glLineWidth(5)
        len_ = 25
        x1 = self.data["win"][0] / 2
        y1 = 38
        dx = math.cos(angle) * len_
        dy = math.sin(angle) * len_
        x2, y2 = x1 + dx, y1 + dy
        cl = ('c3B', (0, 255, 0, 0, 255, 0))
        quad = (x1, y1, x2, y2)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', quad), cl)

    def _fire_target(self, i, aim):
        bx = self.data["x"]
        by = self.data["y"]
        dx = aim[0] - bx
        dy = aim[1] - by
        hyp = math.sqrt(dx ** 2 + dy ** 2)
        angle = math.acos(dx / hyp)
        speed = self.data["p speed"]
        proj = Projectile((bx, by), angle, speed)
        self.data["targets"][i]["proj"] = proj
        self.data["angle"] = angle
        deg = angle * 360 / (2 * math.pi)
        deg *= 10
        deg = int(deg)
        self.angles[deg] += 1

    def _update_targets(self, objs):
        rl, frame, last = self.data["reload"], self.data["frame"], self.data["last"]
        nrl = rl + 2 * (random.random() - 0.5) * rl
        w = self.data["win"][0]
        if frame - last >= nrl:
            targets = self.data["targets"]
            for i in objs:
                if i not in targets:
                    if i.data["pos"][0] > 100 or i.data["speed"][0] > -1:
                        if i.data["pos"][0] < w - 100 or i.data["speed"][0] < 1:
                            self._add_target(i)
                            aim = self._aim_target(i)
                            self._fire_target(i, aim)
                            self.data["last"] = frame
                            break
        remove = []
        for i in self.data["targets"]:
            if i not in objs:
                remove.append(i)
        for i in remove:
            del self.data["targets"][i]

    def newframe(self, objs):
        self._update_targets(objs)
        for i in self.data["targets"]:
            # print(i)
            self.data["targets"][i]["proj"].newframe()
        self.data["g base"].draw(pyglet.gl.GL_QUADS)
        self.data["frame"] += 1
        self._draw_cannon()


class Projectile:
    size = 5
    color = (0, 255, 0)

    def __init__(self, coords, angle, speed):
        self.data = {"pos": coords, "angle": angle, "speed": speed, "frame": 0}

    def newframe(self):
        sp = self.data["speed"]
        an = self.data["angle"]
        x, y = self.data["pos"]
        nx = x + sp * math.cos(an)
        ny = y + sp * math.sin(an)
        self.data["pos"] = nx, ny
        graph = make_circle(nx, ny, self.size, self.color)
        graph.draw(pyglet.gl.GL_POLYGON)


class Block:
    color = (0, 255, 0)

    def __init__(self, pos, speed, w, h):
        self.data = {"win": (w, h), "pos": pos, "speed": speed, "dim": (40, 40)}

    def _pyg_color(self, points):
        col = []
        color = self.color
        for i in range(points):
            for j in color:
                col.append(j)
        return ('c3B', col)

    def newframe(self):
        x, y = self.data["pos"]
        sp = self.data["speed"]
        bw, bh = self.data["dim"]
        w, h = self.data["win"]
        nx, ny = x + sp[0], y + sp[1]
        self.data["pos"] = nx, ny
        if nx < 0:
            self.data["speed"][0] *= -1
            self.data["pos"] = 0, ny
        elif nx > w:
            self.data["speed"][0] *= -1
            self.data["pos"] = w, ny
        x1, y1 = nx - bw / 2, ny - bh / 2
        x2, y2 = nx + bw / 2, ny + bh / 2
        quad = (x1, y1, x1, y2, x2, y2, x2, y1)
        cl = self._pyg_color(4)
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', quad), cl)


class Blocks:
    def __init__(self, w, h):
        self.data = {"win": (w, h)}
        self.blocks = {}

    def add(self, pos, speed):
        w, h = self.data["win"]
        block = {}
        bl = Block(pos, speed, w, h)
        block["pos"] = pos
        block["speed"] = speed
        self.blocks[bl] = block

    def remove(self, block):
        del self.blocks[block]

    def newframe(self):
        for i in self.blocks:
            i.newframe()


class Game:
    def __init__(self, w, h, win):
        self.data = {}
        self.win = win
        self.base = Base(w, h)
        self.base.data["reload"] = 10
        self.blocks = Blocks(w, h)
        self.data["win"] = w, h
        self.data["frame"] = 0
        self.data["re"] = 9
        self.data["last"] = - self.data["re"]
        self.done = False
        self.spr = False

    def _add_block(self):
        w, h = self.data["win"]
        x = random.randint(40, w - 40)
        y = h
        vy = -random.random() * 10
        vx = (0.5 - random.random()) * 3
        # vx = 0
        self.blocks.add((x, y), [vx, vy])

    def fix_blocks(self):
        re = self.data["re"]
        nre = re + 2 * (random.random() - 0.5) * re
        last = self.data["last"]
        frame = self.data["frame"]
        if frame - last >= nre:
            self.data["last"] = frame
            self._add_block()
        bls = self.blocks.blocks
        remove = []
        for i in bls:
            if i.data["pos"][1] < 0:
                remove.append(i)
            if i in self.base.data["targets"]:
                pro = self.base.data["targets"][i]["proj"]
                x, y = i.data["pos"]
                px, py = pro.data["pos"]
                dim = i.data["dim"]
                if abs(px - x) < dim[0] and abs(py - y) < dim[1]:
                    remove.append(i)
        for i in remove:
            self.blocks.remove(i)
            # del bls[i]

    def newframe(self):
        bls = self.blocks.blocks
        self.fix_blocks()
        self.base.newframe(bls)
        self.blocks.newframe()
        self.data["frame"] += 1

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1:
            self.done = True
            self.spr = heatmap(self.win, self)
        if self.spr:
            self.spr.draw()


def draw(dt, func, win):
    if not func.done:
        win.clear()
        func.newframe()
    else:
        func.on_mouse_press(0, 0, 0, 0)


def heatmap(win, game):
    pyglet.gl.glLineWidth(1)
    angles = game.base.angles
    max_ = max(angles)
    min_ = 0
    incr = (max_ - min_) / 511.0
    # incr = int(incr)
    if incr == 0:
        incr = 1
    x1 = game.data["win"][0] / 2
    y1 = 0
    blen = game.data["win"][1] * 1.5
    win.flip()
    win.clear()
    # win.flip()
    for i in range(len(angles)):
        rad = i * 2 * math.pi / 360
        rad /= 10
        amount = angles[i]
        r, g, b = 0, 0, 0
        if amount / incr < 256:
            # print(incr, amount)
            b = 255 - int(amount / incr)
        else:
            r = int(amount / incr) - 255
        g = 255 - r - b
        # print(r, g, b),
        dx = math.cos(rad) * blen
        dy = math.sin(rad) * blen
        x2, y2 = x1 + dx, y1 + dy
        cl = ('c3B', (r, g, b, r, g, b))
        quad = (x1, y1, x2, y2)
        # print(quad)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', quad), cl)
    buffer = pyglet.image.get_buffer_manager().get_color_buffer()
    image = buffer.image_data.get_image_data()
    pil_image = Image.frombytes(image.format, (image.width, image.height),
                                image.get_data(image.format, image.pitch))
    pil_image = pil_image.convert('RGB')
    w, h = pil_image.size
    pil_image2 = pil_image.transpose(Image.FLIP_TOP_BOTTOM)
    pil_image2.save("test.png")
    pil_image = pil_image.tobytes()
    pil_image = pyglet.image.ImageData(w, h, "RGB", pil_image)
    win.clear()
    # print(type(pil_image), len(pil_image))
    spr_ = pyglet.sprite.Sprite(pil_image)
    spr_.x, spr_.y = 0, 0
    spr_.draw()
    return spr_


def main():
    w, h = 1000, 1000
    cp = "AutoShooter"
    win = pyglet.window.Window(w, h, visible=False, caption=cp, vsync=0)
    game = Game(w, h, win)
    win.on_mouse_press = game.on_mouse_press
    d_time = 1.0 / 60
    win.set_visible()
    # print(win.double_buffer)
    win.double_buffer = False
    pyglet.clock.schedule_interval(draw, d_time, game, win)
    pyglet.app.run()


if __name__ == "__main__":
    main()
