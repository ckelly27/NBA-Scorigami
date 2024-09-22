from storage import storeData
from fetch import getNBAData
import pandas as pd
from datetime import date

if __name__ == "__main__":

    today = str(date.today())
    print(today)
    # Fetch the NBA data using the getNBAData class from fetch.py
    #dataFetcher = getNBAData("november", 1977)
    
    # Fetch the data (which will populate the gameData)
    #gameData = dataFetcher.getGameData()
    #print(dataFetcher.getError())
    
    # Store the data using the storeData class
    #data_saver = storeData(gameData)
    #data_saver.saveToCSV()