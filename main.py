import json
from serpapi import GoogleSearch
import webbrowser

# Add your api key below
SERPAPI_KEY = 'Your SerpAPI key'

# open song data, program predicts json file with 'year' and 'song' keys.
# 'year' value will be list of years as int
# 'song' values will be list of lists for songs of corresponding years
with open('data.json') as json_file:
    song_data = json.load(json_file)


def play_song(song):
    """
    searches 'song' using serapi, retrieves the link, and opens top url in web browser
    :param song: song to be searched and then played
    :return: None
    """
    global SERPAPI_KEY
    params = {
        "api_key": SERPAPI_KEY,
        "engine": "youtube",
        "search_query": song
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    video_url = results['video_results'][1]['link']
    webbrowser.open(video_url)


def get_year(data):
    """
    takes a year from user input, finds if year is valid, if valid, returns songs' index position for that year and year
    :param data: this will be songs data entered into the user interface function
    :return: index pos, year
    """
    while True:
        selected_year = input(f"Please give a year ({data['year'][0]}-{data['year'][-1]}):\t")
        if selected_year.isnumeric():
            selected_year = int(selected_year)
            try:
                if data['year'][-1] >= selected_year >= data['year'][0]:
                    songs_pos = data['year'].index(selected_year)
                    break
            except TypeError:
                print("Please give a valid year")
    return songs_pos, selected_year


def user_interface(data):
    """
    user inputs choices into the terminal, program finds songs in data, user selects song, plays song
    :return: None
    """
    print("Welcome to hit parade! Choose a year!")
    pos, year = get_year(data)
    print(f'Welcome to {year}!')
    print("The top five songs are:")
    song_list = data['songs'][pos]
    index = 0
    for song in song_list:
        print(f'{index + 1} - {song}')
        index += 1
    listen_choice = input("\nWould you like to listen to one of these songs (y/n)?\t").lower()
    while True:
        if listen_choice == 'y':
            while True:
                try:
                    song_choice = (int(input(f"Choose a song (1-{index}):\t")))
                    if 0 < song_choice <= index:
                        break
                    else:
                        print('Please enter a valid choice')
                except (ValueError, IndexError):
                    print("Oops! That was not a valid number.  Try again_choice...")
            chosen_song = song_list[song_choice - 1]
            print(f"Now playing {chosen_song}")
            play_song(chosen_song)
            break
        elif listen_choice == 'n':
            replay = True
            while replay:
                again_choice = input("play again_choice (a) or exit (x)?").lower()
                if again_choice == 'x':
                    print("See you next time!")
                    replay = False
                elif again_choice == 'a':
                    user_interface(data)
                else:
                    print("Please enter a valid response (a/x):\t")
            break
        else:
            print('Please enter a valid choice')
            listen_choice = input("\nWould you like to listen to one of these songs (y/n)?\t").lower()



user_interface(song_data)
