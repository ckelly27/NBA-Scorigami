# NBA-Scorigami

Scorigami-tracking program for the NBA

### Why?
Scorigami is a phenomenon in sports where the final score of a game is unique in the sense that no other game has ever had that same final score. This is something that is farily well-known and documented in the NFL. Another sport that I have interest in is basketball, particularly the NBA. I have found that scorigami in the NBA isn't really something that is well-known, nor is it documented as widely as it is in the NFL. This program seeks to remedy this disparity between the two leagues.

### How?
Data courtesy of https://www.basketball-reference.com <br><br>
I had originially intended to use an API that would have contained the data that I needed, but I was unable to find one that I liked that was free. Therfore, using data-scraping techniques, I scraped data from the website above. I used the requests library to extract the html code that the website runs off of. Using another library, BeautifulSoup, I was able to narrow down and filter the html code that contained my desired data and extracted it. An unfortunate caveat to webscraping as opposed to using an API, though, is that there are only so many requests the program can make before hitting rate-limits before you get timed out and ecounter an error 429 ("Too many requests"). To avoid this issue, I had to introduce a delay between each request (3 seconds) so I could achieve the maximum allowed request rate (20 requests/minute). Unfortunately, with so much data to pull, this made the extraction of the data of all games starting from the 1976-1977 season to the most recent season just above a 30 minute process. 
