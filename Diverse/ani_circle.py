import pyglet, random, math, os

from PIL import Image

class Circle:

    def __init__(self, radius, thickness, color, win):
        self.win = win
        self.color = color
        self.radius = radius
        self.thickness = thickness
        self.points = {}
        self.current = 0
        self.delta = 100
        self.angle = 300
        self.img = []
        self.loaded = False
        for i in range(2*radius):
            for j in range(2*radius):
                x,y = radius - i, radius - j
                hyp = x**2 + y**2
                fx, fy = float(x), float(y)
                if hyp:
                    hyp = math.sqrt(hyp)
                    angle = math.atan2(fy, fx)
                    angle = angle*360/(2*math.pi)
                    angle = angle + 179
                    if hyp <= radius and hyp >= radius - thickness:
                        self.points[(x, y)] = round(angle)

    def generate(self):
        delta = self.delta
        w, h = self.win
        for cur in range(360):
            draw = []
            img = Image.new("RGBA", (w, h))
            pixels = img.load()
            d_cur = cur - delta
            for i in self.points:
                x, y = i
                angle = self.points[i]
                fac = 0
                if angle <= cur and angle > d_cur:
                    fac = (angle - d_cur)/(delta/2)
                    if fac > 1:
                        fac = 2 - fac
                else:
                    if angle + delta > cur + 360:
                        fac = (angle - 360 - d_cur)/(delta/2)
                        if fac > 1:
                            fac = 2 - fac
                strength = int(fac*255)
                if strength > 0:
                    last = angle
                    draw.append((x, y, strength))
            for i in draw:
                x, y, strength = i
                r, g, b, a = 0, 0, 255, strength
                nx, ny = x + self.win[0]/2, y + self.win[1]/2
                pixels[nx, ny] = (r, g, b, a)
            script_path = os.getcwd()
            name = script_path + "/circle/" + str(cur) + ".png"
            img.save(name)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img = img.tobytes()
            _img = pyglet.image.ImageData(w, h, "RGBA", img)
            spr = pyglet.sprite.Sprite(_img)
            self.img.append(spr)
            print(cur),

    def load(self):
        self.img = []
        self.loaded = True
        for i in range(360):
            script_path = os.getcwd()
            name = script_path + "/circle/" + str(i) + ".png"
            img = pyglet.image.load(name)
            spr = pyglet.sprite.Sprite(img)
            self.img.append(spr)

    def draw(self, dt):
        w, h = self.win
        self.angle = self.angle % 360
        spr= self.img[self.angle]
        spr.x, spr.y = 0, 0
        spr.draw()
        self.angle += 1




def draw(dt, win, func):
    win.clear()
    func.draw(dt)
    #quad = (0,300, 500,300, 500, 400, 0, 400)
    #col = ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255))
    #pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', quad), col)

def main():
    w, h = 500, 500
    cp = "Circle"
    win = pyglet.window.Window(w, h, visible=False, caption=cp, vsync=0)
    d_time = 1.0/60
    radius = 100
    thi = 20
    circle = Circle(radius, thi, None, (w, h))
    circle.delta = 180
    circle.generate()
    #circle.load()
    win.set_visible()
    pyglet.clock.schedule_interval(draw, d_time, win, circle)
    pyglet.app.run()

if __name__ == "__main__":
    main()




