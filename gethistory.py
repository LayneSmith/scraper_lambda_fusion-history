import requests
import csv
from io import StringIO
from bs4 import BeautifulSoup
from datetime import datetime

def scrapeHistory():
    """Scrape history from team history feed."""

    payload_array = [['day', 'game_date', 'event', 'year', 'time', 'home', 'home_score', 'away', 'away_score', 'tier']]

    # GET SCHOOLS LIST
    url = 'https://home.gotsoccer.com/rankings/team_async.aspx?TeamID=862573&pagesize=100&mode=History'
    #requests
    url_r = requests.get(url)
    #run the requests through soup
    url_soup = BeautifulSoup(url_r.content, "html.parser")

    dates = url_soup.findAll("p",{"class":"font-weight-bold"})
    events = url_soup.findAll("p",{"class":"text-smaller"})
    gameTables = url_soup.findAll("table",{"class":"game-table"})

    for index, game in enumerate(gameTables):   # default is zero

        date_list = dates[index].text.split(', ')
        datetime_object = datetime.strptime(dates[index].text, '%A, %B %d, %Y')
        game_day = date_list[0].lstrip()
        game_date = datetime_object
        game_year = date_list[2]
        event = events[index].text

        games = gameTables[index].findAll('tr')
        for gm in games:
            tds =  gm.findAll('td')
            game_time = tds[0].text
            home_team = tds[1].text
            away_team = tds[3].text
            score_list = tds[2].find('span').text.split(' - ')
            home_score = score_list[0]
            away_score = score_list[1]
            game_tier = tds[4].text
            payload_array.append([game_day, game_date, event, game_year, game_time, home_team, home_score, away_team, away_score, game_tier])

    si = StringIO()
    cw = csv.writer(si)
    for row in payload_array:
        cw.writerow(row)

    # DEPLOY
    history_data = si.getvalue()
    return history_data
            

# this function is just for our testing purposes,
# just calling the main handler function
if __name__ == '__main__':
    scrapeHistory()