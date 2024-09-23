from storage import storeData
from fetch import getNBAData
import pandas as pd
from datetime import date
import time

if __name__ == "__main__":
    # Dictionary of months of the NBA season
    monthDict = {10: "october", 11: "november", 12: "december", 1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june"}
    # Gets today's date
    today = str(date.today())
    currYear = int(today[0: 4])
    currMonth = monthDict.get(int(today[5:7]))

    # If current month isn't during NBA season, defaults to june (end of last season)
    if currMonth == None:
        currMonth = "june"

    # TEMPORARY
    print(currYear)
    print(currMonth)

    # Start program timer
    start_time = time.time()

    # Fetch the NBA data using the getNBAData class from fetch.py
    dataFetcher = getNBAData(currMonth, currYear)
    
    # Fetch the data (which will populate the gameData)
    gameData = dataFetcher.getGameData()
    print(dataFetcher.getError())
    
    # Store the data using the storeData class
    data_saver = storeData(gameData)
    data_saver.saveToCSV()

    # Print program runtime
    print("--- %s seconds ---" % (time.time() - start_time))
