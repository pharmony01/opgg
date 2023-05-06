from bs4 import *
import requests
import random
import re
import pdb

# ToS bamboozler list
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36d',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
]

def get_soup(summoner_name):
    '''Requests the website url and pretends to be a random agent from the agent_list, returns the soupified page'''
    r = requests.get(f'https://www.op.gg/summoners/na/{summoner_name}', headers={'User-Agent': random.choice(user_agents_list)})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_overall_stats(soup):
    '''Returns wins, losses, total win rate (wr), rank, and LP'''
    wins = int(re.search("([0-9]+)(W+?)", str(soup.find_all("div", class_="win-lose")[0]))[0][:-1])
    losses = int(re.search("([0-9]+)(L+?)", str(soup.find_all("div", class_="win-lose")[0]))[0][:-1])
    total_wr = round(wins / (wins + losses), 2) * 100
    rank = soup.select('.tier')[0].text.strip().capitalize()
    lp = soup.select('.lp')[0].text.strip()
    return wins, losses, total_wr, rank, lp

def get_champion_info(soup):
    '''Finds the champion names, individual wr, games played, kda, and image'''
    
    # Finds their winrate based on class
    # The two classes represent the "red" and the "grey" winrates
    wr = soup.select('.css-b0uosc, .css-1nuoroq')
    
    # Gets their games played, and information for the pictures by class
    played = soup.select('.count')
    face = soup.select('.face')[1:]
    
    # Gets their kda based on class
    # There are 4 of them, since there are 4 different colors for KDAs
    kda = soup.select('.css-954ezp, .css-1w55eix, .css-10uuukx, .css-19wuqhz')
    
    champion_info = []
    for i in range(len(wr)):
        # Appends all stats into a list
        temp_champ = []
        tag = face[i].find('img')
        temp_champ.append(tag.get('alt'))
        temp_champ.append(wr[i].text)
        temp_champ.append(played[i].text)
        temp_champ.append(kda[i].text)
        temp_champ.append(tag.get('src'))
        champion_info.append(temp_champ)
    return champion_info

def get_summoner_info(soup):
    '''Returns the summoners name, level, and profile picture (pfp)'''
    level = soup.select('.level')[0].text
    pfp = soup.select('.profile-icon')[0].find('img').get('src')
    name = soup.select('.name')[0].text
    return name, level, pfp
    
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
        print(f"They have played a total of {wins+losses} games")
        print(f"They have won {wins} and lost {losses} for a winrate of {total_wr}%")
        print(f"They are currently in {rank} with {lp}")
        print("These are their most played champtions:")
        for champ in champion_information:
            print(f"{champ[0]}")
            print(f"    WR: {champ[1]}")
            print(f"    {champ[2]}")
            print(f"    {champ[3]}")
    except:
        print(f"{summoner_name} has not played any ranked games this season")
    
    
    
    
if __name__ == "__main__":
    main()