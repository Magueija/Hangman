import os
import csv

import clear

def hm_save_score(nr_games, nr_wins, avg_wrongs):
    name = ""
    fd = -1
    file_path = os.path.join("scoreboards", "scoreboard.csv")
    csv_rd = None
    csv_wt = None

    while (name == "" or " " in name or len(name) > 25):
        name = input(" Username: ")
        if (" " in name or len(name) > 25):
            clear.clear_idle()
            if (" " in name):
                print("Spaces aren't allowed. You can use '_' as an alternative")
            if (len(name) > 25):
                print("Username max length is 25 characters.")
            print("\n")
    with open(file_path, "a", newline='') as fd:
        csv_wt = csv.writer(fd, delimiter=',')
        csv_wt.writerow([name, str(nr_wins) + "/" + str(nr_games), str(avg_wrongs)])

def hm_show_score():
    fd = -1
    file_path = os.path.join("scoreboards", "scoreboard.csv")
    csv_rd = None
    csv_list = ()
    spaces_len_0 = 1
    spaces_len_1 = 1
    spaces_len_2 = 1

    clear.clear_idle()
    try:
        with open(file_path, "r") as fd:
            print("    »»»»»»»»»»»»»»»»»»»»»» Hangman Scoreboard ««««««««««««««««««««««   \n")
            print("  ____________________________________________________________________ ")
            print(" |         Username         |     Wins/Games     |   Average Wrongs   |")
            print(" |——————————————————————————|————————————————————|————————————————————|")
            csv_rd = csv.reader(fd, delimiter=',')
            for row in csv_rd:
                spaces_len_0 = 25 - len(row[0]);
                spaces_len_1 = 19 - len(row[1]);
                spaces_len_2 = 19 - len(row[2]);
                print(" | " + row[0] + (" " * spaces_len_0) + "|"
                    + " " + row[1] + (" " * spaces_len_1) + "|"
                    + " " + row[2] + (" " * spaces_len_2) + "|")
            print(" |__________________________|____________________|____________________|")
            print("")
    except:
        print("Scoreboard unavailable.")
        print("")

