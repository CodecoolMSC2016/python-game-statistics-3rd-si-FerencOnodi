
# Export functions
from reports import *

export_file = input("Where and what kind do you want the export file to be? ")
def export_count_games():
    with open(export_file, "a+") as f:
        f.write("\n" + str(count_games(filename)))

def export_decide():
    with open(export_file, "a+") as f:
        f.write("\n" + str(decide(filename, year)))

def export_get_latest():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_latest(filename)))

def export_count_by_genre():
    with open(export_file, "a+") as f:
        f.write("\n" + str(count_by_genre(filename, genre)))
    
def export_get_line_number_by_title():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_line_number_by_title(filename, title)))

def export_sort_abc():
    with open(export_file, "a+") as f:
        f.write("\n" + str(sort_abc(filename)))

def export_get_genres():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_genres(filename)))

def main():
    if user_input == "1":
        export_count_games()#működik :)
    elif user_input == "2":
        export_decide()
    elif user_input == "3":
        export_get_latest()
    elif user_input == "4":
        export_count_by_genre()
    elif user_input == "5":
        export_get_line_number_by_title()
    elif user_input == "6":
        export_sort_abc()
    elif user_input == "7":
        export_get_genres()
main()