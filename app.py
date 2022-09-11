import json

config_json = "game-config.json"
game_config = json.load(open(config_json))


def play_levels():
    for level in game_config["levels"]:
        print(level["file"])


play_levels()
