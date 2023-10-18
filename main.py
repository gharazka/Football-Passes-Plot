from soccer_pitch import get_pitch
from read_data import get_player_list

if __name__ == '__main__':
    get_player_list()
    player = input("Insert full player name: ")
    get_pitch(player)



