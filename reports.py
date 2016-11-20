
# Report functions
import csv
import operator

print("Greetings, Judy!\nFirst you will have to enter the name of the file which you want to use, then select from the main menu!\n")
filename = input("From which file do you want to read in information? ")
'''try:
    with open(filename) as testfile:
        return "Valid file"
except IOError:
    return "Could not read file:", filename'''
#while True: # nem volt itt
print("\nMain menu:\n1. How many games are in the file?\n2. Is there a game from the given year?")
print("3. Which was the latest game?\n4. How many games are in the file by genre?")
print("5. On which line is the given game?\n6. List of games in alphabetical order.")
print("7. What genres are in the file?\n")
user_input = input("Press the number of the option or type 'exit' to quit. ")#lehet hogy elég ezt az egyet while-ba rakni
#na így király, csak nem csinál semmit hanem mindig ezt dobja fel
if user_input == "2":
    year = input("\nWhich year? ")
elif user_input == "4":
    genre = input("\nWhat genre are you looking for? ")
elif user_input == "5":
    title = input("\nWhich game are you looking for? ")
        


def count_games(filename):
    '''
    Counts how many games are in the given file.
    '''
    with open(filename) as f:
        count = 0
        for line in f.readlines():
            count += 1
        return count


def decide(filename, year):
    '''
    Tells you if there is a game from the given year.
    '''
    with open(filename) as f:
        reader = csv.reader(f,delimiter = '\t')

        titles = []
        total_copies_sold = []
        release_dates = []
        genres = []
        publishers =[]

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_copies_sold.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)

    if str(year) in release_dates: #if year in release_dates:
        return True
    else:
        return False


def get_latest(filename):
    '''
    Returns the latest game from the file.
    '''
    with open(filename) as f:
        reader = csv.reader(f,delimiter = '\t')

        titles = []
        total_copies_sold = []
        release_dates = []
        genres = []
        publishers =[]

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_copies_sold.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)
        
        latest_dict = dict(zip(titles, release_dates))
        return max(latest_dict.items(), key = operator.itemgetter(1))[0] # Ehhez kell az operator


def count_by_genre(filename, genre):
    '''
    Counts how many games are in the file from a given genre.
    '''
    with open(filename) as f:
        reader = csv.reader(f, delimiter = '\t')
        counter = 0
        for line in reader:
            if genre in line:
                counter += 1
        return counter   

        
def get_line_number_by_title(filename, title):
    '''
    Returns the line where the game is found.
    '''
    with open(filename) as f:
        count = 0
        for line in f.readlines():
            count += 1

    with open(filename) as f:
        reader = csv.reader(f, delimiter = '\t')

        titles = []
        total_copies_sold = []
        release_dates = []
        genres = []
        publishers =[]

        for name, sold, date, gamegenre, pubteam in reader:
            titles.append(name)
            total_copies_sold.append(sold)
            release_dates.append(date)
            genres.append(gamegenre.lower())
            publishers.append(pubteam)
        
        line_number = []
        for i in range(1, count + 1):
            line_number.append(i)
        dict_line_and_title = dict(zip(line_number, titles))
        #return dict_line_and_title
        for line, name in dict_line_and_title.items():
            if name == title:
                return line
            #else:
                #return "There is no such game." Ez nem kell és akkor működik, a teszten is


def sort_abc(filename):
    '''
    Returns the games in alphabetical order.
    '''
    with open(filename) as f:
        reader = csv.reader(f, delimiter = '\t')

        titles = []
        total_copies_sold = []
        release_dates = []
        genres = []
        publishers =[]

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_copies_sold.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)
        
        return (sorted(titles))
    

def get_genres(filename):
    '''
    Returns the genres of the games.
    '''
    with open(filename) as f:
        reader = csv.reader(f, delimiter = '\t')

        titles = []
        total_copies_sold = []
        release_dates = []
        genres = []
        publishers =[]

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_copies_sold.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)
        
        lower_genres = map(str.lower, genres)
        dict_genres = dict(zip(lower_genres, genres))
        sorted_genres = sorted(dict_genres.items(), key=operator.itemgetter(0))
        key_genres = []
        val_genres = []
        for key, value in sorted_genres:
            key_genres.append(key)
            val_genres.append(value)
        return val_genres
#a while True alatt minden egy tabbal kijjeb volt
#ha minden beljebb volt, akkor tovább ment amig bekéri a plusz cuccokat, de nem hívott meg semmit!

#LEHET HOGY A MENÜ NEM IS KELL CSAK SIMÁN MEG KELL HÍVNI A GECIBE AZ EGÉSZET EGYBE!!!!
#http://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python
#http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#http://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
#http://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
#http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
#http://stackoverflow.com/questions/14067267/lower-case-from-a-text-file
#
#
