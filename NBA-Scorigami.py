import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = 'https://www.basketball-reference.com/leagues/NBA_2019_games-october.html'  # Replace with your URL
response = requests.get(url)

# Step 2: Parse the webpage content
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    div_by_id = soup.find('div', id='div_schedule')  # Replace with actual div ID
    print(div_by_id)

    print("-----------------------------------------------------")
    rows = div_by_id.find_all("tr")
    print(rows)

    for row in rows:
    # Try to find the visitor team name and score
        visitor_team = row.find('td', {'data-stat': 'visitor_team_name'})
        visitor_score = row.find('td', {'data-stat': 'visitor_pts'})

    # Try to find the home team name and score
        home_team = row.find('td', {'data-stat': 'home_team_name'})
        home_score = row.find('td', {'data-stat': 'home_pts'})

        # First argument of find method is 'th' because date is stored within a th tag in the html document
        game_date = row.find('th', {'data-stat': 'date_game'})
    
    # Check if all required elements exist before accessing their text
        if visitor_team and visitor_score and home_team and home_score and game_date:
            visitor_team_text = visitor_team.get_text()
            visitor_score_text = visitor_score.get_text()
            home_team_text = home_team.get_text()
            home_score_text = home_score.get_text()
            game_date_text = game_date.get_text()

        # Print the extracted information
            print(f"Visitor Team: {visitor_team_text} - {visitor_score_text}")
            print(f"Home Team: {home_team_text} - {home_score_text}")
            print(f"Game Date: {game_date_text}")
            print("-" * 40)
        else:
            print("Some data missing in this row.")
            print("-" * 40)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")