import random
import pyglet


class Game:
    black = 'c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    green = 'c3B', (0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0)
    graph = [black, green]

    def _gen_cell_values(self):
        cx, cy = self.data["n cells"]
        cells = []
        for i in range(cx):
            newl = []
            for j in range(cy):
                life = 0
                prev = 0
                neighb = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
                          (i - 1, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i + 1, j - 1)]
                excl = []
                if i == 0:
                    excl.append((i - 1, j))
                    excl.append((i - 1, j - 1))
                    excl.append((i - 1, j + 1))
                elif i == cx - 1:
                    excl.append((i + 1, j))
                    excl.append((i + 1, j - 1))
                    excl.append((i + 1, j + 1))
                if j == 0:
                    excl.append((i, j - 1))
                    excl.append((i - 1, j - 1))
                    excl.append((i + 1, j - 1))
                elif j == cy - 1:
                    excl.append((i, j + 1))
                    excl.append((i - 1, j + 1))
                    excl.append((i + 1, j + 1))
                excl = set(excl)
                for k in excl:
                    neighb.remove(k)
                neighb = tuple(neighb)
                newl.append({"status": life, "previous": prev, "pos": neighb})
            cells.append(newl)
        self.data["cells"] = cells

    def _gen_cell_graph(self):
        cx, cy = self.data["n cells"]
        cw, ch = self.data["cell dim"]
        for i in range(cx):
            for j in range(cy):
                x1, x2 = i * cw, (i + 1) * cw
                y1, y2 = j * ch, (j + 1) * ch
                quad = (x1, y1, x1, y2, x2, y2, x2, y1)
                # vlb = pyglet.graphics.vertex_list(4, ('v2f', quad), self.black)
                # vlg = pyglet.graphics.vertex_list(4, ('v2f', quad), self.green)
                # self.data["cells"][i][j]["vertex"] = (vlb, vlg)
                self.data["cells"][i][j]["g pos"] = quad

    def __init__(self, w, h, cx, cy):
        """
        w = window width
        h = window height
        cx = cells per column
        cy = cells per row
        """
        self.data = {"win dim": (w, h), "cell dim": (int(w / cx), int(h / cy)),
                     "n cells": (cx, cy), "frame": 0}
        self._gen_cell_values()
        self._gen_cell_graph()

    def changecell(self, cell, value):
        i, j = cell
        self.data["cells"][i][j]["status"] = value
        self.data["cells"][i][j]["previous"] = value

    def random(self, weight=0.5):
        cells = self.data["cells"]
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                seed = random.random()
                cells[i][j]["status"] = 0
                cells[i][j]["previous"] = 0
                if seed > weight:
                    cells[i][j]["status"] = 1
                    cells[i][j]["previous"] = 1

    def _first_frame(self):
        batch = pyglet.graphics.Batch()
        for i in self.data["cells"]:
            for j in i:
                quad = j["g pos"]
                stat = j["status"]
                # vert = j["vertex"][stat]
                color = self.graph[stat]
                batch.add(4, pyglet.gl.GL_QUADS, None, ('v2f', quad), color)
                # vert.draw(pyglet.gl.GL_QUADS)
                # pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', quad), color)
        batch.draw()

    def _update_status(self):
        cells = self.data["cells"]
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                neighb = 0
                status = cells[i][j]["status"]
                for k in cells[i][j]["pos"]:
                    neighb += cells[k[0]][k[1]]["previous"]
                new_status = 0
                if status:
                    if 2 <= neighb < 4:
                        new_status = 1
                else:
                    if neighb == 3:
                        new_status = 1
                cells[i][j]["status"] = new_status

    def _draw_cells(self):
        batch = pyglet.graphics.Batch()
        for i in self.data["cells"]:
            for j in i:
                stat = j["status"]
                # vert = j["vertex"][stat]
                color = self.graph[stat]
                quad = j["g pos"]
                if stat == 1:
                    batch.add(4, pyglet.gl.GL_QUADS, None,
                              ('v2f', quad), color)
                    # vert.draw(pyglet.gl.GL_QUADS
        batch.draw()

    def newframe(self):
        cells = self.data["cells"]
        self._update_status()
        self._draw_cells()
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                cells[i][j]["previous"] = cells[i][j]["status"]
        self.data["frame"] += 1


def draw(dt, func, win):
    win.clear()
    func()


def main():
    w, h = 1000, 1000
    cx, cy = 100, 100
    cp = "Game of Life"
    game = Game(w, h, cx, cy)
    game.random(0.5)
    win = pyglet.window.Window(w, h, visible=False, caption=cp, vsync=0)
    d_time = 1.0 / 20
    win.set_visible()
    pyglet.clock.schedule_interval(draw, d_time, game.newframe, win)
    pyglet.app.run()


if __name__ == "__main__":
    main()
