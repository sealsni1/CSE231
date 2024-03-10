# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str


import csv
import string
from operator import itemgetter

###################################################################################
# Assignment: Project 06

# Description: The program reads data from CSV and TXT files, to process song lyrics, and
# various operations on the data.
# The project includes the implementation of various functions to read
# and process song data, calculate average word counts for singers, find distinct
# vocabularies for each singer, search for songs based on user input, and display
# the results.

# Functions:
# - open_file(message) -> fp
# - read_stopwords(fp) -> set
# - validate_word(word, stopwords) -> bool
# - process_lyrics(lyrics, stopwords) -> set
# - update_dictionary(data_dict, singer, song_name, song_words_set) -> None
# - read_data(fp, stopwords) -> dict
# - calculate_average_word_count(data_dict) -> dict
# - find_singers_vocab(data_dict) -> dict
# - display_singers(combined_list) -> None
# - search_songs(data_dict, words) -> list
# - main()
###################################################################################


def open_file(message):
    ''' Prompts the user for a filename,
    The program will try to open the file
    (Try, Except) and then returns the file to main
    '''

    # Create while loop for try and except functions
    while True:

        # Try to open the file
        try:
            file = input(message)

            fp = open(file, 'r')

            return fp

        # If the file does not exist display error message
        # and re-prompt user for a new filename
        except FileNotFoundError:

            print("\nFile is not found! Try Again!")


def read_stopwords(fp):
    ''' Takes file pointer (stopwords) as parameter,
    and returns a set of unique stopwords that are converted
    to lowercase. It closes the file when done with it.
    '''

    # Create a set to hold the unique stopwords
    stopwords_set = set()

    # Iterate through the file to add each word
    # into the set (make sure they are lowercase)
    for line in fp:

        stop_word = line.split()

        for word in stop_word:

            word = word.lower()

            stopwords_set.add(word)

    # Close the file when finished
    fp.close()

    return stopwords_set


def validate_word(word, stopwords):
    ''' Receives a word and a set as parameters.
    If the given word is in the stopwords set or it has any
    punctuation the function returns False.
    Else, it returns True
    '''

    # If the words is all numbers or letters
    if word.isalpha():

        # If the word is in stopwords set
        if word not in stopwords:

            return True

    return False


def process_lyrics(lyrics, stopwords):
    ''' Receives a set of lyrics and stopwords as parameters.
    The function then splits the lyrics by spacing and strips it
    of whitespace and punctuation (also lowercase). It then
    calls for the validate_word function to validate each word.
    If the word is validated it will add the word to a set
    and return it '''

    # Assign a set to hold the lyrics for each song
    lyrics_set = set()

    words = lyrics.lower().split()

    for word in words:

        # Strip the words of any punctuation
        word = word.strip(string.punctuation)

        # Call validate_word function to make sure the word is relevant
        if validate_word(word, stopwords):

            # Add the words to the lyrics if they pass validate_word function
            lyrics_set.add(word)

    return lyrics_set


def read_data(fp, stopwords): # Fix
    ''' Reads the data and collects: singer name, song name, and
    lyrics (all strings). Process the lyrics by using the process_lyrics
    function to create a set of words. It will then add add those three
    things to a dictionary and return it to the user '''

    # Create a dictionary to store the key, value pairs
    data_dict = {}

    # Read the csv file
    reader = csv.reader(fp)

    # Skip the header
    next(reader)

    for row in reader:

        # Define the singer, song name, and lyrics for each row
        singer = row[0]
        song_name = row[1]
        song_lyrics = row[2].lower()

        song_lyrics = song_lyrics.lower()

        # Call process_lyrics function to get a set for the song lyrics
        lyrics = process_lyrics(song_lyrics, stopwords)

        # Call update_dictionary function to add all the
        # key, value pairs to the dictionary
        update_dictionary(data_dict, singer, song_name, lyrics)

    fp.close()

    return data_dict


def update_dictionary(data_dict, singer, song, words):
    ''' Receives four parameters: dta_dict, singer, song, and
    words. The function inserts a song_name: song words_set key
    valye pair to the dictionary of the singer. Does not return
    anything.'''

    # If the singer is not already in the set add them to it
    if singer not in data_dict:

        data_dict[singer] = {}

    # Update the dictionary to include all the key, value pairs
    data_dict[singer][song] = words


def calculate_average_word_count(data_dict): # Fix
    ''' receives data_dict and returns another
    dictionary which contains average word counts
    of singers. '''

    # Create a dictionary to hold values
    avg_dict = {}

    total_words = 0

    for singer, songs in data_dict.items():

        # Calculate the total amount of words used in each song by the singer
        # (I do not know how to iterate through this correctly, so I asked
        # on stack overflow how to do it)
        total_words = sum(len(words) for words in songs.values())

        # Calculate the total amount of songs by the singer
        num_songs = len(songs)

        # From total_words and num_songs find the average amount of words
        # used in each song by the singer
        avg_dict[singer] = total_words / num_songs

    return avg_dict


def find_singers_vocab(data_dict):
    ''' Receives data_dict as parameter and
    returns a dictionary containing a set of distinct
    words used by every singer. '''

    # Create a dictionary to hold the distinct words for each singer
    singer_vocab = {}

    # for key, values in the dictionary
    for singer, songs in data_dict.items():

        vocab = set()

        for words in songs.values():

            # add the distinct words into the dictionary
            vocab.update(words)

        singer_vocab[singer] = vocab

    return singer_vocab


def display_singers(combined_list): # Fix
    ''' Receives a list containing (singer, avg word count, number of songs,
     and vocab size). It then prints the top ten songs in the list according
      to the sort function below. '''

    # Sort the list by avg word count (descending) and then by vocabulary size
    # (descending) if two or more tuples have the same avg word count
    combined_list = sorted(combined_list, key=itemgetter(1, 3), reverse=True)

    # Print the header that displays the top ten songs after being sorted
    print("\n{:^80s}".format("Singers by Average Word Count (TOP - 10)"))

    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer", "Average Word Count",
          "Vocabulary Size", "Number of Songs"))

    print('-' * 80)

    # Print the top 10 tuples from the list after being sorted
    for row in combined_list[:10]:

        avg_word_count = round(row[1], 2)

        print("{:<20}{:>20}{:20}{:>20}".format(row[0], avg_word_count, row[2], row[3]))


def search_songs(data_dict, words):
    ''' receives data_dict and a set of words. It then returns
    a list of tuples every time it finds a match. '''

    # Create a list to hold each song that matches the user
    # Prompted word
    matching_list = []

    for singer, songs in data_dict.items():

        for song, lyrics in songs.items():

            # if the words are in the song lyrics add the singer
            # and song name to the matching list and return it to main
            if words.issubset(lyrics):

                matching_list.append((singer, song))

    matching_list = sorted(matching_list, key = lambda x: (x[0], x[1]))

    return matching_list


def main(): # Fix

    # Call open_file(message) to open the stopword file
    fp_stopwords = open_file('\nEnter a filename for the stopwords: ')

    # Call read_data(fp, stopwords) to open the song data file
    fp_songdata = open_file('\nEnter a filename for the song data: ')

    # Call read_stopwords to get a list of unique stopwords from file
    reading_stopwords = read_stopwords(fp_stopwords)

    # Call read_data(fp, stopwords) to create a set of words
    reading_songdata = read_data(fp_songdata, reading_stopwords)

    # Call calculate_average_word_count to get the
    # average word counts for each singer in the file
    avg_word_count = calculate_average_word_count(reading_songdata)

    # Call find_singers_vocab to get the vacab size used for each
    # singer in the file
    singer_words = find_singers_vocab(reading_songdata)

    # Create a list to hold singer, avg word count, number of songs,
    # and vocab size for each singer in the file
    combined_list = []

    for singer in reading_songdata:

        combined_list.append((singer, avg_word_count[singer], len(singer_words[singer]),
                              len(reading_songdata[singer])))

    # Call display function to display the top 10 singers by average word count to the user
    display_singers(combined_list)

    # This block of code is so the user can search for songs by the words
    # that are in the lyrics (executes the song search part of the code)
    print("\nSearch Lyrics by Words")

    while True:
        # Prompt user for a word to do a word search with
        user_word = input("\nInput a set of words (space separated), press enter to exit: ")

        check = False
        contains_stopword = False

        # If the user does not enter a word or character exit the program
        if not user_word:
            break

        # Make the user prompted word lowercase and then
        # add the words into a set to use issubset function
        user_words = user_word.lower()
        words_dict = set(user_words.split())

        # If the word contains any punctuation or it is in stopwords
        # set check to True to enter the if statement below
        for word in words_dict:
            for ch in word:
                if ch in string.punctuation:
                    check = True

                if word in reading_stopwords:
                    contains_stopword = True

        # If check is True display the error messages and re-prompt the user
        # for a new set of search words
        if check or contains_stopword:

            print('\nError in words!')
            print('1-) Words should not have any digit or punctuation')
            print('2-) Word list should not include any stop-word')

        else:

            # Call search_songs function to find the songs that have the
            # user prompted word in it
            songs = search_songs(reading_songdata, words_dict)

            # Display the matching singers and songs to the search words
            print(f"\nThere are {len(songs)} songs containing the given words!")

            # Create a variable so it only prints the top 5 songs
            # if there is more than 5 songs
            i = 1

            # If there is any songs that match the search words
            # display the headers for the given items (singer, song)
            if songs:
                print("{:<20s} {:<s}".format('Singer', 'Song'))

            # Prints the singers, and songs that match the search words
            for singer, song in songs:

                if i <= 5:

                    print("{:<20s} {:<s}".format(singer, song))

                i += 1



if __name__ == '__main__':
    main()
