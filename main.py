from scraping import *


def main():
    # Summoner name input
    summoner_name = "Ainn"
    soup = get_soup(summoner_name)
    # If the summoner has played any ranked games query their information
    try:
        wins, losses, total_wr, rank, lp = get_overall_stats(soup)
        champion_information = get_champion_info(soup)
        name, level, pfp = get_summoner_info(soup)
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

    except IndexError:
        print(f"{summoner_name} has not played any ranked games this season")
    except Exception:
        print("Wow you broke this good")
    finally:
        pdb.set_trace()


if __name__ == "__main__":
    main()
