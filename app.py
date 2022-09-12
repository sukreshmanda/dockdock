import json
from console_mapper import print_info_okblue

STATE_JSON = "state.json"
LEVELS = "levels"
FILE = "file"
INFO = "info"
CONFIG_JSON = "game-config.json"


def load_game_configs():
    config_file = open(CONFIG_JSON)
    game_config = json.load(config_file)
    config_file.close()
    return game_config


def load_state_from_file():
    state_file = open(STATE_JSON)
    load_state = json.load(state_file)
    state_file.close()
    return load_state


def play_levels():
    game_config = load_game_configs()
    state = load_state_from_file()
    for level in game_config[LEVELS]:
        level_path = level[FILE]
        level_config = json.load(open(level_path))
        print_info_okblue(level_config[INFO], end="\n")


def write_state(updated_state):
    print(updated_state)
    conf = open(STATE_JSON, "w")
    json.dump(updated_state, conf, indent=2)
    conf.close()


write_state()
