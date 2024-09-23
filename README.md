# NBA-Scorigami

Scorigami-tracking program for the NBA
### STILL WORK IN PROGRESS

### Why?
Scorigami is a phenomenon in sports where the final score of a game is unique in the sense that no other game has ever had that same final score. This is something that is farily well-known and documented in the NFL. Another sport that I have interest in is basketball, particularly the NBA. I have found that scorigami in the NBA isn't really something that is well-known, nor is it documented as widely as it is in the NFL. This program seeks to remedy this disparity between the two leagues.

### How?
Data courtesy of https://www.basketball-reference.com <br><br>
I had originally intended to use an API that would have contained the data I needed, but I was unable to find a free one that I liked. Therefore, using data-scraping techniques, I scraped data from the website above. I used the requests library to extract the HTML code that the website runs on. Using another library, BeautifulSoup, I was able to narrow down and filter the HTML code to extract the data I wanted.
<br> <br>
An unfortunate caveat to web scraping, as opposed to using an API, is that there are limits to how many requests the program can make before hitting rate limits and encountering an HTTP 429 error ("Too Many Requests"). To avoid this issue, I had to introduce a delay of 3 seconds between each request, allowing me to stay within the maximum request rate of 20 requests per minute. Unfortunately, with so much data to pull, this made the extraction of all games from the 1976-1977 season to the most recent season take just over 30 minutes. 
