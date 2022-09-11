import json
from console_mapper import print_info_okblue

LEVELS = "levels"

FILE = "file"

INFO = "info"

config_json = "game-config.json"
game_config = json.load(open(config_json))


def play_levels():
    for level in game_config[LEVELS]:
        level_path = level[FILE]
        level_config = json.load(open(level_path))
        print_info_okblue(level_config[INFO], end="\n")


play_levels()
