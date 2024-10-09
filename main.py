from storage import storeData
from fetch import getNBAData
import pandas as pd
from datetime import date
import sys
import time


def getData():
            
    # Fetch the NBA data using the getNBAData class from fetch.py
            dataFetcher = getNBAData(currMonth, currYear)
            
            # Fetch the data (which will populate the gameData)
            gameData = dataFetcher.getGameData()
            
            # Store the data using the storeData class
            data_saver = storeData(gameData)
            data_saver.saveToCSV()

def checkCSV():
    ans = getInput("Do you already have the up-to-date NBA CSV? (y/n) ", ("y", "n"))
    if ans == "n":
        if getInput("This process will take about 30 min. Is this okay? (y/n) ", ("y", "n")) == "y":
             getData()
        else:
             sys.exit(0)
        
        
def getInput(text, responses):
       
    while True:
        ans = input(text).strip().lower()
        if ans not in responses:
            print("Please enter a valid answer")
        else:
            return ans 

if __name__ == "__main__":
    # Dictionary of months of the NBA season
    monthDict = {10: "october", 11: "november", 12: "december", 1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june"}
    # Gets today's date
    today = str(date.today())
    currYear = int(today[0: 4])
    currMonth = monthDict.get(int(today[5:7]))

    # If current month isn't during NBA season, defaults to june (end of last season)
    currMonth = "june" if currMonth == None else currMonth
    
    checkCSV()
    df = pd.read_csv("NBAGameData.csv")
    

    


            
