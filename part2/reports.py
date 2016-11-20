
# Report functions
import csv
import operator

file_name = input("\nFrom which file, do you want to read in, information? ")
title = input("\nGive me the name of the game: ")

def get_most_played(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(float(sold))
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)

        dict_most_played = dict(zip(titles, total_sold_copies))
        return max(dict_most_played.items(), key=operator.itemgetter(1))[0] #Test: Passed
        

def sum_sold(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(float(sold))
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)
        
        return sum(total_sold_copies) #Test: Passed


def get_selling_avg(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        count = 0
        for line in reader:
            count += 1
    
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(float(sold))
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)

        return sum(total_sold_copies) / count # Test: Passed


def count_longest_title(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)
        
        return len(max(titles, key=len)) #Test: Passed


def get_date_avg(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        count = 0
        for line in reader:
            count += 1

    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')
        
        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(sold)
            release_dates.append(int(date))
            genres.append(genre)
            publishers.append(pubteam)

        avg_date = sum(release_dates) / count
        return int("%.0f" % avg_date) # Test: Passed


def get_game(file_name, title):
    with open(file_name) as f:
        get_game = []

        for line in f:
            if line.split('\t')[0] == title:
                get_game.append(line.split('\t')[0])
                get_game.append(float(line.split('\t')[1]))
                get_game.append(int(line.split('\t')[2]))
                get_game.append(line.split('\t')[3])
                get_game.append((line.split('\t')[4]).rstrip('\n'))
        return get_game # Test: Passed


def count_grouped_by_genre(file_name):
    with open(file_name) as f:

        grouped_by_genre = {}

        for line in f:
            if line.split('\t')[3] in grouped_by_genre:
                grouped_by_genre[line.split('\t')[3]] += 1
            else:
                grouped_by_genre[line.split('\t')[3]] = 1        
        return grouped_by_genre #Test: Passed


def get_date_ordered(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter='\t')

        titles = []
        total_sold_copies = []
        release_dates = []
        genres = []
        publishers = []

        for title, sold, date, genre, pubteam in reader:
            titles.append(title)
            total_sold_copies.append(sold)
            release_dates.append(date)
            genres.append(genre)
            publishers.append(pubteam)        
        
        dict_title_date = dict(zip(titles, release_dates))
        sorted_by_date = sorted(dict_title_date.items(), key=operator.itemgetter(1))
        return sorted_by_date