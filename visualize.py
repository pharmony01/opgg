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


def show_champion_data(
    champion_information: np.ndarray[np.str_], name: str, level: str, pfp: str
) -> None:
    """Will show information, not ready yet"""
    # Extract the relevant data from the input array
    champion_names = [row[0] for row in champion_information]
    win_rates = [float(row[1].strip("%")) for row in champion_information]
    games_played = [int(row[2].split(" ")[0]) for row in champion_information]
    kda_ratios = [float(row[3].split(":")[0]) for row in champion_information]
    urls = [row[4] for row in champion_information]
    images = [io.imread(url) for url in urls]
    size = max(games_played)

    # Create a figure and set its size
    fig = plt.figure(figsize=(10, 6))

    # Set the title for both subplots
    fig.suptitle("Champion Statistics", y=0.95, fontsize=16)

    # Create the subplots
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    # Create the bar chart for win rates
    bars1 = ax1.bar(champion_names, win_rates)
    ax1.set_ylabel("Win Rate (%)")
    ax1.set_ylim(0, 100)

    # Set the win rate labels on top of the bars
    ax1.bar_label(bars1, labels=[f"{win_rate:.2f}%" for win_rate in win_rates])

    # Create the bar chart for games played
    bars2 = ax2.bar(champion_names, games_played)
    ax2.set_ylabel("Games Played")
    ax2.set_ylim(0, size + (int(size * 0.1)))
    ax2.set

    # Set the win rate labels on top of the bars
    ax2.bar_label(bars2, labels=games_played)

    plt.show()
