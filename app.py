import json
from console_mapper import print_info_okblue_formatting, print_question_header, print_info_red

CURRENT_LEVEL = "current_level"

QUESTION = "question"
NAME = "name"
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


def is_current_state_fixed():
    pass


def print_next_level_info(info):
    pass


def play_levels():
    game_config = load_game_configs()
    state = load_state_from_file()

    # for level in game_config[LEVELS]:
    #     level_path = level[FILE]
    #     level_config = json.load(open(level_path))
    #     print_question_header("Question: " + level_config[QUESTION], end="\n")
    #     print_info_red(str(state["current_level"]), end="\n")
    #     print_info_okblue_formatting(level_config[INFO], end="\n")
    while state[CURRENT_LEVEL] < len(game_config[LEVELS]):
        # print_next_level_info(game_config["levels"][state["current_level"]+1])
        print(game_config[LEVELS][state[CURRENT_LEVEL]])
        state[CURRENT_LEVEL] += 1
        write_state(state)


def write_state(updated_state):
    print(updated_state)
    conf = open(STATE_JSON, "w")
    json.dump(updated_state, conf, indent=2)
    conf.close()


play_levels()
