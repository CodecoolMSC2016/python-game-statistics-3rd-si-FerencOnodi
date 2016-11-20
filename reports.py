
# Report functions
import csv
import operator

print("Greetings, Judy!\nFirst you will have to enter the name of the file which you want to use, then select from the main menu!\n")
filename = input("From which file do you want to read in information? ")

print("\nMain menu:\n1. How many games are in the file?\n2. Is there a game from the given year?")
print("3. Which was the latest game?\n4. How many games are in the file by genre?")
print("5. On which line is the given game?\n6. List of games in alphabetical order.")
print("7. What genres are in the file?\n8. When was the release date of the top sold fps?")
user_input = input("Press the number of the option or type 'exit' to quit. ")

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

    if str(year) in release_dates:
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
        return max(latest_dict.items(), key = operator.itemgetter(1))[0]


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
        for line, name in dict_line_and_title.items():
            if name == title:
                return line


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


def when_was_top_sold_fps(filename):
    '''
    Returns the year when the top sold fps was published
    '''
    with open(filename) as f:
        
        dates = []
        sold = []

        for line in f:
            if line.split('\t')[3] == "First-person shooter":
                dates.append(line.split('\t')[2])
                sold.append(float(line.split('\t')[1]))
        
        dict_sold_dates = dict(zip(sold, dates))
        return int(max(dict_sold_dates.items(), key=operator.itemgetter(0))[1])