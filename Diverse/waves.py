import pyglet
import math
import os

from progressbar import Progress
from PIL import Image


class Waves:
    def __init__(self, radius, thickness, color, win):
        self.win = win
        self.color = color
        self.radius = radius
        self.thickness = thickness
        self.frame = 0
        self.points = {}
        self.img = []
        for i in range(2 * radius):
            for j in range(2 * radius):
                x, y = radius - i, radius - j
                hyp = x ** 2 + y ** 2
                hyp = math.sqrt(hyp)
                self.points[(x, y)] = round(hyp)

    def _calc_strength(self, point, n):
        hyp = self.points[point]
        # if not hyp:
        #     hyp = self.thickness
        delta = n
        n_hyp = hyp - delta
        fact = math.cos(n_hyp * 2 * math.pi / self.thickness)
        stren = int(round(fact * 255 * 0.5 + 255 * 0.5))
        if hyp >= self.radius:
            stren = 0
        elif self.radius - hyp < self.thickness:
            fact = (self.radius - hyp) / self.thickness
            fact = 1 - math.log(1 + fact * (math.e - 1))
            stren -= int(round(fact * 255))
        elif hyp < self.thickness:
            fact = hyp / self.thickness
            fact = 1 - math.log(1 + fact * (math.e - 1))
            stren -= int(round(fact * 255))
        return stren

    def _draw_img(self, todraw, n):
        w, h = self.win
        img = Image.new("RGBA", (w, h))
        pixels = img.load()
        for j in todraw:
            x, y, stren = j
            r, g, b, a = 0, 0, 255, stren
            nx, ny = x + w / 2, y + h / 2
            pixels[nx, ny] = (r, g, b, a)
        script_path = os.getcwd()
        zeros = "0" * (len(str(self.thickness)) - len(str(n)))
        name = script_path + "/waves/" + zeros + str(n) + ".png"
        img.save(name)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img = img.tobytes()
        _img = pyglet.image.ImageData(w, h, "RGBA", img)
        spr = pyglet.sprite.Sprite(_img)
        self.img.append(spr)

    def _del_extra(self):
        script_path = os.getcwd() + "/waves/"
        for file_n in os.listdir(script_path):
            if file_n.endswith(".png"):
                n = int(file_n[:-4])
                if n < 0 or n >= self.thickness:
                    os.remove(script_path + file_n)
                elif len(str(n)) > len(str(self.thickness)):
                    os.remove(script_path + file_n)

    def generate(self):
        if not os.path.exists(os.getcwd() + "/waves/"):
            os.makedirs(os.getcwd() + "/waves/")
        col = self.color
        thi = self.thickness
        progress = Progress(thi)
        self.img = []
        for i in range(thi):
            todraw = []
            for j in self.points:
                x, y = j
                stren = self._calc_strength(j, i)
                todraw.append((x, y, stren))
            self._draw_img(todraw, i)
            progress.Increment()
        self._del_extra()
        progress.End()

    def load(self):
        script_path = os.getcwd() + "/waves/"
        self.img = []
        progress = Progress(len(os.listdir(script_path)))
        for file_n in os.listdir(script_path):
            progress.Increment()
            if file_n.endswith(".png"):
                img = pyglet.image.load(script_path + file_n)
                img.anchor_x = img.width / 2
                img.anchor_y = img.height / 2
                spr = pyglet.sprite.Sprite(img)
                self.img.append(spr)
        progress.End()

    def draw(self, dt):
        w, h = self.win
        self.frame %= len(self.img)
        spr = self.img[self.frame]
        spr.x, spr.y = w / 2, h / 2
        spr.draw()
        self.frame += 1


def draw(dt, win, func, fps):
    win.clear()
    func.draw(dt)
    fps.draw()


def main():
    w, h = 500, 500
    cp = "Circle"
    win = pyglet.window.Window(w, h, visible=False, caption=cp)
    d_time = 1.0 / 60
    radius = 100
    thi = 40
    waves = Waves(radius, thi, None, (w, h))
    waves.generate()
    waves.load()
    fps = pyglet.clock.ClockDisplay()
    win.set_visible()
    pyglet.clock.schedule_interval(draw, d_time, win, waves, fps)
    pyglet.app.run()


if __name__ == "__main__":
    main()
