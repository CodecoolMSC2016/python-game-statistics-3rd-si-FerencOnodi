
# Printing functions
from reports import *

def main():
    try:
        print("\n" + str(get_most_played(file_name)))
        print("\n" + str(sum_sold(file_name)))
        print("\n" + str(get_selling_avg(file_name)))
        print("\n" + str(count_longest_title(file_name)))
        print("\n" + str(get_date_avg(file_name)))
        print("\n" + str(get_game(file_name, title)))
        print("\n" + str(count_grouped_by_genre(file_name)))
        print("\n" + str(get_date_ordered(file_name)))
    except:
        print("\nCould not find %s." % file_name)
main()