from scraping import *
from visualize import *
import numpy as np


def main():
    # Summoner name input
    summoner_name = "Révenant"
    soup = get_soup(summoner_name)
    # If the summoner has played any ranked games query their information
    try:
        wins, losses, total_wr, rank, lp = get_overall_stats(soup)
        champion_information = get_champion_info(soup)
        name, level, pfp = get_summoner_info(soup)
        print_champion_data(
            champion_information, wins, losses, total_wr, rank, lp, name, level
        )
        show_champion_data(champion_information)

    except IndexError:
        print(f"{summoner_name} has not played any ranked games this season")


if __name__ == "__main__":
    main()
