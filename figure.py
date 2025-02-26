class Figure:
    def __init__(self, id, *cells):
        self.id_figure = id
        self.figure = []
        for cell_list in cells:
            if isinstance(cell_list, list):
                self.figure.extend(cell_list)
            else:
                self.figure.append(cell_list)


    def draw(self, screen):
        for i in self.figure:
            i.draw(screen)

    def move_figure(self, dx, dy):
        n = []
        for i in self.figure:
            n.append(i.can_move(dx, dy))
        if all(n):
            for i in self.figure:
                i.move(dx, dy)

    def place_figure(self, map):
        color = self.figure[0].color
        n = []
        for i in self.figure:
            x, y = i.x_map, i.y_map
            n.append(map[x][y].can_change())
        if all(n):
            for i in self.figure:
                x, y = i.x_map, i.y_map
                map[x][y].change(color)
                map[x][y].is_free = False
            return map, True
        return map, False
