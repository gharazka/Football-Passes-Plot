import json


def read_data(player):
    complete_passes = []
    incomplete_passes = []
    with open("15946.json", "r") as file:
        data = json.load(file)
    for data_dict in data:
        if data_dict["type"]["name"] == "Pass":
            if data_dict["player"]["name"] == player:
                try:
                    if data_dict["pass"]["outcome"]:
                        incomplete_passes.append([data_dict["location"], data_dict["pass"]["end_location"]])
                except KeyError:
                    complete_passes.append([data_dict["location"], data_dict["pass"]["end_location"]])

    return complete_passes, incomplete_passes


def get_player_list():
    with open("15946.json", "r") as file:
        data = json.load(file)
    print("Insert a name from the list:")
    for player in data[0]["tactics"]["lineup"]:
        print(player["player"]["name"])
    for player in data[1]["tactics"]["lineup"]:
        print(player["player"]["name"])
    print()