from scraping import *
from visualize import *
import numpy as np
import random
import argparse

test_summoners = [
    "SeductiveOtter",
    "Heartstee1y",
    "vEternity",
    "Yuraodo",
    "lightrocket2",
    "Quantum",
]

parser = argparse.ArgumentParser(
    description="Scrape an op.gg user's ranked information"
)
parser.add_argument("--user", help="Summoner name to be searched")
parser.add_argument(
    "--log", help="makes an HTML output file from the soup", action="store_true"
)


def main(args):
    # Summoner name input
    summoner_name = args.user if args.user else random.choice(test_summoners)
    url = f"https://www.op.gg/summoners/na/{summoner_name}"
    soup = get_soup(url)

    # Write an html output file
    if args.log:
        with open("output.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

    # If the summoner has played any ranked games query their information
    try:
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
    main(parser.parse_args())
