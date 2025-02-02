from cell import Cell


def generate_map(map):
    for i in range(8):
        columns = []
        for j in range(8):
            columns.append(Cell(i, j, None))
        map.append(columns)
    return map
