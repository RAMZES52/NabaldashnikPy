def reverse_map(map):
    r_map = []
    for i in range(8):
        n = [map[j][i] for j in range(8)]
        r_map.append(n)
    return r_map


def check_score(map):
    for i in range(8):
        if all(cell.can_change() == 0 for cell in map[i]):
            for cell in map[i]:
                cell.change(None)
                cell.is_free = True
    r_map = reverse_map(map)
    for i in range(8):
        if all(cell.can_change() == 0 for cell in r_map[i]):
            for cell in r_map[i]:
                cell.change(None)
                cell.is_free = True
    return map
