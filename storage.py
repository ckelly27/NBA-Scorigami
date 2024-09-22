from fetch import getNBAData
import csv
import os

class storeData:

    # gameData is an array of dictionaries that contains information about each NBA game
    def __init__(self, gameData):
        self.gameData = gameData
        self.fileName = "nbaGameData.csv"
    
    # Stores the data as a CSV
    def saveToCSV(self):
        fileExists = os.path.isfile(self.fileName)

        # Open the file in append mode if it already exists. If it doesn't, write mode
        with open(self.fileName, mode="a" if fileExists else "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.gameData[0].keys())
            
            # Write the header only if the file doesn't already exist
            if not fileExists:
                writer.writeheader()

            # Write each game's data (each dictionary) as a new row
            for game in self.gameData:
                writer.writerow(game)
        
        print("Data successfully written to " + self.fileName)

# Example usage:
if __name__ == "__main__":
    # Fetch the NBA data using the getNBAData class from fetch.py
    data_fetcher = getNBAData("november", 1977)
    
    # Fetch the data (which will populate the gameData)
    game_data = data_fetcher.getGameData()
    
    # Store the data using the storeData class
    data_saver = storeData(game_data)
    data_saver.saveToCSV()

