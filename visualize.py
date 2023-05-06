import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pdb


def print_champion_data(
    champion_information: np.ndarray[np.str_],
    wins: str,
    losses: str,
    total_wr: str,
    rank: str,
    lp: str,
    name: str,
    level: str,
) -> None:
    print(f"You searched for {name}")
    print(f"This summoner is level {level}")
    print(f"They have played a total of {wins+losses} ranked games")
    print(f"They have won {wins} and lost {losses} for a winrate of {total_wr}%")
    print(f"They are currently in {rank} with {lp}")
    print("These are their most played champtions:")
    for champ in champion_information:
        print(f"{champ[0]}")
        print(f"    WR: {champ[1]}")
        print(f"    {champ[2]}")
        print(f"    {champ[3]}")


def show_champion_data(champion_information: np.ndarray[np.str_]) -> None:
    """Will show information, not ready yet"""
    champion_information = np.array(champion_information)
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    # a = io.imread()

    # plt.imshow(a)
    # plt.axis("off")
    # plt.show()
