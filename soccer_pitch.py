from mplsoccer import Pitch
import matplotlib
import matplotlib.pyplot as plt
from read_data import read_data


def get_pitch(player):
    matplotlib.use('TkAgg')
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.set_facecolor("#22312b")
    ax.patch.set_facecolor("#22312b")
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    pitch.draw(ax=ax)
    complete_passes, incomplete_passes = read_data(player)
    plt.gca().invert_yaxis()
    for i in range(len(complete_passes)):
        plt.plot((complete_passes[i][0][0], complete_passes[i][1][0]),
                 (complete_passes[i][0][1], complete_passes[i][1][1]), color="lime")
        plt.scatter(complete_passes[i][0][0], complete_passes[i][0][1], color="black")
    for i in range(len(incomplete_passes)):
        plt.plot((incomplete_passes[i][0][0], incomplete_passes[i][1][0]),
                 (incomplete_passes[i][0][1], incomplete_passes[i][1][1]), color="red")
        plt.scatter(incomplete_passes[i][0][0], incomplete_passes[i][0][1], color="black")
    plt.title(f'Passes made by: {player}', color="white", size=20)
    plt.show()
