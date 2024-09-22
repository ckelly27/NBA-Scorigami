from fetch import getNBAData
import csv
import os

class storeData:

    # gameData is an array of dictionaries that contains information about each NBA game
    def __init__(self, gameData):
        self.gameData = gameData
        self.fileName = "NBAGameData.csv"
    
    # Stores the data as a CSV
    def saveToCSV(self):
        fileExists = os.path.isfile(self.fileName)

        # Open the file in append mode if it already exists; otherwise, write mode
        with open(self.fileName, mode="a" if fileExists else "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.gameData[0].keys())
            
            # Writes the header only if the file doesn't already exist
            if not fileExists:
                writer.writeheader()

            # Initializes set to store existing game data for duplicate checking
            existingData = set()

            # If the file already exists, read its content to populate existingData
            if fileExists:
                with open(self.fileName, mode="r", encoding="utf-8") as readFile:
                    reader = csv.DictReader(readFile)
                    for row in reader:
                        game_tuple = (row['game_date'], row['visitor_team'], row['visitor_score'], row['home_team'], row['home_score'])
                        existingData.add(game_tuple)

            # Writes each game's data as a new row if it's not a duplicate
            for game in self.gameData:
                # Temp row used to compare to existing data
                gameTuple = (game['game_date'], game['visitor_team'], game['visitor_score'], game['home_team'], game['home_score'])
                if gameTuple not in existingData:
                    writer.writerow(game)

        print("Data successfully written to " + self.fileName)


