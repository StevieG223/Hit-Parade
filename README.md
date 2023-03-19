# Hit-Parade
Jukebox Time Machine -UK

Description:
Have you ever wondered what a year sounded like? 
This project attempts to answer that question. Webscrapping the "NME Single of the Year" Wikipedia page, this program uses Youtube to play the hit singles of that year from the UK. 

Theoretically, this program can run with any json as long as it is properly formatted. 

I mostly made this because I love 1980s-1990s British popular music like the Smiths, Morrissey, Pulp, Oasis, David Bowie, The Jam, etc. I believe that this would also have some application in language learning and building out cultural competancy when learning a foriegn language. I plan to eventaully take this project in that direction by allowing users to choose a country to "travel" to as well as a time. 

Requirements:
Python: Python 3
Libraries: SerpAPI (pip install google-search-results), Pandas, BeautifulSoup4
API key: SerpApi

Installation:
1. Install required libraries
2. Get SerpAPI key
3. (optional) create song data, program predicts json file with 'year' and 'song' keys. 'year' value will be list of years as int, 'song' values will be list of lists for songs of corresponding years. get_data.py can be modified to do this with a wikipedia page of your choice. 
4. Run program

TO DO:
-Fix bugs and improve error handling
-Add nicer interface using Tkinter or tinycss
-Build a geographic selector
-Add data for different countries (currently planning Italy, USA, possibly Spain or a Spanish-speaking country)
