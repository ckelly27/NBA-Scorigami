import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class getNBAData:

    def __init__(self, toMonth, toYear):
        self.errorList = []
        self.errorCount = 0
        self.startYear = 1977
        self.startMonth = "october"

        self.toMonth = toMonth
        self.toYear = toYear + 1
        # Initialize list of dictionaries of game data
        self.gameData = []

        self.validMonths = ["october", "november", "december", "january", "february", "march", "april", "may", "june"]
        if self.toMonth not in self.validMonths:
            print("invalid")
            return 0

        self.getTargetData()
        if len(self.errorList) != 0:
            print("There may be some missing data.")

        
            
    # Returns the number of errors
    def getError(self):
        print(self.errorCount)
    
    # Returns the list of game data
    def getGameData(self):
        return self.gameData
    
    # Loops through years and months til target date is reached
    def getTargetData(self):
        for year in range(self.startYear, self.toYear):
            for month in self.validMonths:
                self.oneMonthData(month, year)
    
    # Extracts the data from one month of one year
    def oneMonthData(self, month, year):
        # Fetch the webpage
        url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_games-' + month + '.html'  
        response = requests.get(url)

        # Parse the webpage content
        if response.status_code == 200:
            parsedHTML = BeautifulSoup(response.text, 'html.parser')

            # Extracts the div containing the data
            dataDiv = parsedHTML.find('div', id='div_schedule')  
        
            # Extracts the rows containing the data
            rows = dataDiv.find_all("tr")
            #print(rows)

            for row in rows:
            # Extracts the visitor's team name and score
                visitor_team = row.find('td', {'data-stat': 'visitor_team_name'})
                visitor_score = row.find('td', {'data-stat': 'visitor_pts'})

            # Extracts the home team's name and score
                home_team = row.find('td', {'data-stat': 'home_team_name'})
                home_score = row.find('td', {'data-stat': 'home_pts'})

                # Extracts the date of the game
                # First argument of find method is 'th' because date is stored within a th tag in the html document
                game_date = row.find('th', {'data-stat': 'date_game'})
            
                # Check if all required elements exist before accessing their text
                if visitor_team and visitor_score and home_team and home_score and game_date:
                    visitor_team_text = visitor_team.get_text()
                    visitor_score_text = visitor_score.get_text()
                    home_team_text = home_team.get_text()
                    home_score_text = home_score.get_text()
                    game_date_text = game_date.get_text()

                    if visitor_score_text == "" or home_score_text == "":
                        print("Games have not been played yet.")
                        break

                    else:
                    # Print the extracted information
                        #print(f"Visitor Team: {visitor_team_text} - {visitor_score_text}")
                        #print(f"Home Team: {home_team_text} - {home_score_text}")
                        #print(f"Game Date: {game_date_text}")
                        #print("-" * 40)

                        # Adds dictionary of the game to list of games
                        self.gameData.append({
                            'game_date': game_date_text,
                            'visitor_team': visitor_team_text,
                            'visitor_score': visitor_score_text,
                            'home_team': home_team_text,
                            'home_score': home_score_text
                        })



        else:
            self.errorList.append(response.status_code)

if __name__ == "__main__":
    m = getNBAData("october", 1977)
    #print(m.getGameData())
    m.getError()