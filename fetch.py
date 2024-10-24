import requests
from bs4 import BeautifulSoup
import time

class getNBAData:

    def __init__(self, toMonth, toYear):
        # If there is trouble with the request, the error code is appended to this array
        self.errorList = []
        self.errorCount = 0
        self.startYear = 1977
        self.startMonth = "october"

        self.toMonth = toMonth
        self.toYear = toYear 
        
        # Initialize list of dictionaries of game data
        self.gameData = []

        # NBA seasons span this range of months
        self.validMonths = ["october", "november", "december", "january", "february", "march", "april", "may", "june", "july", "august", "september"]
        if self.toMonth not in self.validMonths:
            print("invalid")
            return 0

        self.getTargetData()

        
            
    # Returns the number of errors
    def getError(self):
        print(self.errorCount)
        print(self.errorList)
    
    # Returns the list of game data
    def getGameData(self):
        return self.gameData
    
    # Loops through years and months until target date is reached
    def getTargetData(self):
        for year in range(self.startYear, self.toYear + 1):
            for month in self.validMonths:
                self.oneMonthData(month, year)
                time.sleep(3)

                if (year == self.toYear + 1) and month == self.toMonth:
                    return
    
    # Extracts the data from one month of one year
    def oneMonthData(self, month, year):
        # Fetch the webpage
        url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_games-" + month + ".html"  
        print(url)
        response = requests.get(url)

        # Parse the webpage content
        if response.status_code == 200:
            parsedHTML = BeautifulSoup(response.text, "html.parser")

            # Extracts the div containing the data
            dataDiv = parsedHTML.find("div", id="div_schedule")  
        
            # Extracts the rows containing the data
            rows = dataDiv.find_all("tr")
            #print(rows)

            for row in rows:
            # Extracts the visitor's team name and score
                visitor_team = row.find("td", {"data-stat": "visitor_team_name"})
                visitor_score = row.find("td", {"data-stat": "visitor_pts"})

            # Extracts the home team's name and score
                home_team = row.find("td", {"data-stat": "home_team_name"})
                home_score = row.find("td", {"data-stat": "home_pts"})

                # Extracts the date of the game
                # First argument of find method is 'th' because date is stored within a th tag in the html document
                game_date = row.find("th", {"data-stat": "date_game"})
            
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

                        visitor_score_int = int(visitor_score_text)
                        home_score_int = int(home_score_text)

                        # Determine winning and losing teams and their scores
                        if visitor_score_int > home_score_int:
                            winning_team = visitor_team_text
                            losing_team = home_team_text
                            winning_score = visitor_score_int
                            losing_score = home_score_int
                        else:
                            winning_team = home_team_text
                            losing_team = visitor_team_text
                            winning_score = home_score_int
                            losing_score = visitor_score_int

                        # Adds dictionary of the game to list of games
                        self.gameData.append({
                            "game_date": game_date_text,
                            "visitor_team": visitor_team_text,
                            "visitor_score": visitor_score_text,
                            "home_team": home_team_text,
                            "home_score": home_score_text,
                            "winning_team": winning_team,
                            "losing_team": losing_team,
                            "winning_team_score": winning_score,
                            "losing_team_score": losing_score
                        })
        ## Print erroneous month/year (for my own sake to see if the program was running properly)
        else:
            print("-" * 40)
            print("ERROR:")
            print(month)
            print(year)
            print(response.status_code)
            print(url)
            print("-" * 40)
            self.errorList.append(response.status_code)


