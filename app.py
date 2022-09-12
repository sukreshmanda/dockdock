import json
from console_mapper import print_info_okblue

STATE_JSON = "state.json"
LEVELS = "levels"
FILE = "file"
INFO = "info"

config_json = "game-config.json"
config_file = open(config_json)
state_file = open(STATE_JSON)

game_config = json.load(config_file)
load_state = json.load(state_file)

config_file.close()
state_file.close()

load_state["current_level"] = 0


def play_levels():
    for level in game_config[LEVELS]:
        level_path = level[FILE]
        level_config = json.load(open(level_path))
        print_info_okblue(level_config[INFO], end="\n")


def write_state(updated_state):
    print(updated_state)
    conf = open(STATE_JSON, "w")
    json.dump(updated_state, conf, indent=2)
    conf.close()


write_state(load_state)
