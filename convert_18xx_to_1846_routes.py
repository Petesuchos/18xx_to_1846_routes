import json


def load_game_data(filename):
    with open(filename) as file:
        game_data = json.load(file)
    return game_data


def fix_rotation(tile, rotation):
    rotation_3_tiles = [19, 41, 42]
    rotation_2_tiles = [6, 8, 16, 51, 292]
    rotation_1_tiles = [5, 7, 14, 39, 47, 291]

    if tile in rotation_3_tiles:
        return (rotation + 3) % 6

    if tile in rotation_2_tiles:
        return (rotation + 2) % 6

    if tile in rotation_1_tiles:
        return (rotation + 1) % 6

    return rotation


def remove_undo_redo(action_list):
    confirmed_actions = []
    for index, action in enumerate(action_list):
        if action['type'] == 'undo':
            if index + 1 > len(action_list) or action_list[index + 1]['type'] != 'redo':
                confirmed_actions.pop()
        else:
            confirmed_actions.append(action)
    return confirmed_actions


def tile_configuration(game_data):
    action_list = remove_undo_redo(game_data['actions'])
    lay_tile_action_list = [a for a in action_list if a['type'] == 'lay_tile']

    board_layout = {}
    for lay_tile_action in lay_tile_action_list:
        hexagon = lay_tile_action['hex']
        tile = int(lay_tile_action['tile'].split('-')[0])
        rotation = fix_rotation(tile, int(lay_tile_action['rotation']))

        board_layout[hexagon] = [tile, rotation]

    return board_layout


def export_tile_configuration(filename):
    game_data = load_game_data(filename)
    tiles = tile_configuration(game_data)
    tile_str = ''

    for hexagon, tile in tiles.items():
        tile_str += f'{hexagon}; {tile[0]}; {tile[1]}\n'

    return tile_str
