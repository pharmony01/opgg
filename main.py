from scraping import *
from visualize import *
from website_interaction import *
import numpy as np
import random

test_summoners = [
    "SeductiveOtter",
    "Heartstee1y",
    "vEternity",
    "Pockyˇ",
    "Yuraodo",
    "lightrocket2",
    "Quantum",
]


def main():
    # Summoner name input
    summoner_name = random.choice(test_summoners)
    url = f"https://www.op.gg/summoners/na/{summoner_name}"
    soup = get_soup(url)
    # If the summoner has played any ranked games query their information
    try:
        # Not currently functional
        # update_profile(url)
        wins, losses, total_wr, rank, lp = get_overall_stats(soup)
        champion_information = get_champion_info(soup)
        name, level, pfp = get_summoner_info(soup)
        print_champion_data(
            champion_information, wins, losses, total_wr, rank, lp, name, level
        )
        show_champion_data(champion_information, name, level, pfp)

    except IndexError:
        print(f"{summoner_name} has not played any ranked games this season")
    pdb.set_trace()


if __name__ == "__main__":
    main()
