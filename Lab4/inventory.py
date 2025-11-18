import copy


START_POINTS = 15
INVENTORY_SIZE_X = 3
INVENTORY_SIZE_Y = 3
NESSESARILY_THING = 'i'


items = {'r': {'size': 3, 'points': 25},
         'p': {'size': 2, 'points': 15},
         'a': {'size': 2, 'points': 15},
         'm': {'size': 2, 'points': 20},
         'i': {'size': 1, 'points': 5},
         'k': {'size': 1, 'points': 15},
         'x': {'size': 3, 'points': 20},
         't': {'size': 1, 'points': 25},
         'f': {'size': 1, 'points': 15},
         'd': {'size': 1, 'points': 10},
         's': {'size': 2, 'points': 20},
         'c': {'size': 2, 'points': 20}}


def try_main(backpack, items_names, index, current_points):
    if index >= len(items_names):
        return (current_points, backpack)

    score_hor = try_hor(backpack, items_names, index, current_points)
    score_vert = try_vert(backpack, items_names, index, current_points)
    score_skip = try_skip(backpack, items_names, index, current_points)

    return max(score_hor, score_vert, score_skip, key=lambda x: x[0])


def try_hor(backpack, items_names, index, current_points):
    best_result = (float('-inf'), None)
    name = items_names[index]
    size = items[name]['size']
    points = items[name]['points']
    for row in range(INVENTORY_SIZE_Y):
        for col in range(INVENTORY_SIZE_X - size + 1):
            can_place = True
            for k in range(size):
                if backpack[row][col + k] is not None:
                    can_place = False
                    break
            if can_place:
                new_backpack = copy.deepcopy(backpack)
                for k in range(size):
                    new_backpack[row][col + k] = name
                result = try_main(new_backpack, items_names, index + 1,
                                  current_points + points)
                if result[0] > best_result[0]:
                    best_result = result

    return best_result


def try_vert(backpack, items_names, index, current_points):
    best_result = (float('-inf'), None)
    name = items_names[index]
    size = items[name]['size']
    points = items[name]['points']
    new_backpack = copy.deepcopy(backpack)

    if size == 1:
        return (float('-inf'), None)

    for row in range(INVENTORY_SIZE_Y - size + 1):
        for col in range(INVENTORY_SIZE_X):
            can_place = True
            for k in range(size):
                if backpack[row + k][col] is not None:
                    can_place = False
                    break
            if can_place:
                new_backpack = copy.deepcopy(backpack)
                for k in range(size):
                    new_backpack[row + k][col] = name
                result = try_main(new_backpack, items_names, index + 1,
                                  current_points + points)
                if result[0] > best_result[0]:
                    best_result = result

    return best_result


def try_skip(backpack, items_names, index, current_points):
    name = items_names[index]
    points = items[name]['points']
    bp_point = current_points - points

    return try_main(backpack, items_names, index+1, bp_point)


def backpack(items, start_points, inventory_size_x, inventory_size_y):
    backpack = [[None for _ in range(inventory_size_x)] for _ in
                range(inventory_size_y)]
    necessarily_thing_size = items[NESSESARILY_THING]['size']
    necessarily_thing_points = items[NESSESARILY_THING]['points']
    start_points += necessarily_thing_points

    for i in range(necessarily_thing_size):
        backpack[0][i] = NESSESARILY_THING

    items_names = [k for k in items.keys() if k != NESSESARILY_THING]
    best_score, best_backpack = try_main(backpack, items_names, 0,
                                         start_points)

    print(f'Best score: {best_score}')
    print('Best backpack:')

    for row in best_backpack:
        print(row)


if __name__ == '__main__':
    backpack(items, START_POINTS, INVENTORY_SIZE_X, INVENTORY_SIZE_Y)
