
# Printing functions
from reports import  *


def print_count_games():
    print((count_games(filename)))

def print_decide():
    print(decide(filename, year,))

def print_count_by_genre():
    print(count_by_genre(filename, genre))

def print_get_genres():
    print(get_genres(filename))

def print_get_latest():
    print(get_latest(filename))

def print_get_line_number_by_title():
    if get_line_number_by_title(filename, title) == None:
        print("There is no such game in the file.")
    else:
        print(get_line_number_by_title(filename, title))

def print_sort_abc():
    print(sort_abc(filename))

def print_get_genres():
    print(get_genres(filename))

def main(): #a while true nem volt benne
    #while True: #így csak egy sima végtelen ciklust kapok
    if user_input == "1":
        print_count_games()
    elif user_input == "2":
        print_decide()
    elif user_input == "3":
        print_get_latest()
    elif user_input == "4":
        print_count_by_genre()
    elif user_input == "5":
        print_get_line_number_by_title()
    elif user_input == "6": #abc sorrend
        print_sort_abc()
    elif user_input == "7": #milyen zsánerek vannak
        print_get_genres()
    elif user_input == "exit":
        exit()
main() #lehet hogy a main-en belül kell while-ba tenni mindent hogy újra és újra használni lehessen