import os
import random
import statistics

import score
import clear

# Python code to check for empty list
# IMPLICIT way or Pythonic way
def isemptylist(lis1):
    if not lis1:
        return True
    else:
        return False

def hm_welcome():
    print("\n                »»»»»»»»»»»»»»» Welcome to Hangman! «««««««««««««««\n\n")
    print("""
        How to play:
            » You have to guess the hidden word before the hangman fully appears. Words are only coutries.
            » First try guessing by writing letter. Do not repeat letters.
            » If you think you know the word, try to guess it, but be careful, you only have one chance!
            » Finally, have fun!
            » Insert "quit" in "Your guess:" to end the game.
        \n\n""")

def hm_guess(word, used, wd_spaces):
    user_input = ""
    ltr = ""
    idx = 0

    user_input = input(" Your guess: ").lower()
    if (user_input.isalpha() or " " in user_input):
        if (len(user_input) == 1):
            if (user_input in str(used)):
                print("\n Letter already used. Try again.\n")
                print(" List of used letters:")
                print("  > {}\n".format(" ".join(used)))
                return (hm_guess(word, used, wd_spaces))
            elif (user_input in str(word)):
                used.append(user_input)
                while (user_input in str(word)):
                    idx = int(word.index(user_input))
                    wd_spaces[idx] = user_input
                    word[idx] = '$'
                return (True, used, wd_spaces)
            else:
                used.append(user_input)
                return (False, used, wd_spaces)
        else:
            return (user_input, used, wd_spaces)
    else:
        print("\n Please, enter only letters or words.\n")
    return (hm_guess(word, used, wd_spaces))

def hm_play(word, used, wd_spaces, wrongs):
    board = ("   _____     ",
            "   |    |    ",
            "   |    {}    ".format("O" if wrongs >= 1 else " "),
            "   |   {}   ".format("/|\\" if wrongs >= 4 else "/| "
                                if wrongs >= 3 else " | "
                                if wrongs >= 2 else "   "),
            "   |   {}    ".format(" | " if wrongs >= 2 else "   "),
            "   |  {}  ".format("_/ \_" if wrongs >= 6 else "_/   "
                                if wrongs >= 5 else "     "),
            "   |         ",
            "   ==========")
    guess = ""

    if (isemptylist(used) == False):
        clear.clear_idle()
    print("\n                »»»»»»»»»»»»»»» Hangman «««««««««««««««\n\n")
    print("{}\n".format("\n".join(board)))
    print("   Word: {}\n\n".format(" ".join(wd_spaces)))
    if (wrongs == 6 or "_" not in wd_spaces):
        return (wrongs)
    guess, used, wd_spaces = hm_guess(list(word), used, wd_spaces)
    if (guess == True):
        return (hm_play(word, used, wd_spaces, wrongs))
    elif (guess == False):
        wrongs += 1
        return (hm_play(word, used, wd_spaces, wrongs))
    elif (guess == "quit"):
        return (None)
    elif (guess != word):
        wrongs = 6
    return (wrongs)
    

def hm_start():
    countries = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
    "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
    "Colombia", "Comoros", "Congo, Democratic Republic of the Congo", "Republic of the Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
    "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")
    play_again = ""
    word = []
    wd = ""
    wd_spaces = []
    ltr = ''
    total_wrongs = []
    nr_games = 0
    nr_wins = 0

    while (play_again == "" or play_again == "y"):
        clear.clear_idle()
        hm_welcome()
        wrongs = 0
        wd_spaces = []
        word = random.choice(countries).lower()
        wd = "".join(word)
        nr_games += 1

        for ltr in word:
            if (ltr.isalpha()):
                wd_spaces.append("_")
            else:
                wd_spaces.append(ltr)
        wrongs = hm_play(word, [], wd_spaces, 0)
        if (wrongs is None):
            return (None, None, None)
        elif (wrongs < 6):
            nr_wins += 1
            print("\n Congratulations! YOU WON!\n")
            print(" The country was '{}'\n".format(wd))
        else:
            print("\n Game over! YOU LOST!\n")
            print(" The country was '{}'.\n".format(wd))
        total_wrongs.append(float(wrongs))
        print(" Score: {} wins out of {} games\n\n".format(nr_wins, nr_games))
        play_again = "Not expected"
        while (play_again != "" and play_again != "y" and play_again != "n"):
            play_again = input(" Play again? [Y/n]: ").lower()
    return (nr_games, nr_wins, 0 if isemptylist(total_wrongs) == True else statistics.mean(total_wrongs))

def hangman():
    nr_games = 0
    nr_wins = 0
    avg_wrongs = 0.0
    newscore = "Not expected"

    nr_games, nr_wins, avg_wrongs = hm_start()
    if (avg_wrongs is not None):
        while (newscore != "" and newscore != "y" and newscore != "n"):
                newscore = input("\n Save score? [Y/n]: ").lower()
        if (newscore == "" or newscore == "y"):
            score.hm_save_score(nr_games, nr_wins, round(avg_wrongs, 2))
    score.hm_show_score()


