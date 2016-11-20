
# Export functions
from reports import *

export_file = input("Where and what kind do you want the export file to be? ")

def export_get_most_played():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_most_played(file_name)))

def export_sum_sold():
    with open(export_file, "a+") as f:
        f.write("\n" + str(sum_sold(file_name)))

def export_get_selling_avg():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_selling_avg(file_name)))

def export_count_longest_title():
    with open(export_file, "a+") as f:
        f.write("\n" + str(count_longest_title(file_name)))

def export_get_date_avg():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_date_avg(file_name)))

def export_get_game():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_game(file_name, title)))

def export_count_group_by_genre():
    with open(export_file, "a+") as f:
        f.write("\n" + str(count_grouped_by_genre(file_name)))

def export_get_date_ordered():
    with open(export_file, "a+") as f:
        f.write("\n" + str(get_date_ordered(file_name)))


def main():
    export_get_most_played()
    export_sum_sold()
    export_get_selling_avg()
    export_count_longest_title()
    export_get_date_avg()
    export_get_game()
    export_count_group_by_genre()
    export_get_date_ordered()
main()