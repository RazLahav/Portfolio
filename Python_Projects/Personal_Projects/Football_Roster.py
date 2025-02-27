"""Football Roster"""

import random
from copy import deepcopy

'''Community Member Players'''
members_data = [["Avi Hady",4.45,"A"],["Asaf Zachar",3.2,"D"],["Adir Frenkel",3.8,"D"],["Dor Zafrir",3.9,"M"],
                ["David Fish",3.2,"D"],["Daniel Ben Haim",4.4,"A"],["Daniel Menashe",2.5,"D"],["David Costa",3.2,"D"],
                ["David Biton",3.2,"D"],["Eden Bruchis",4.47,"A"],["Hod Gohasi",3.9,"M"],["Hagai Viloga",3.2,"D"],
                ["Ido Amran",3.87,"M"],["Itay Shalev",3.2,"D"],["Itay Zamir",3.2,"D"],
                ["Kobi Pando",3.2,"D"],["Nir Lahav",2.5,"A"],["Niv Poleg",3.46,"D"],["Niv Galsman",3.46,"D"],
                ["Omer Talmi",3.37,"M"],["Omer Zafrir",3.37,"D"],["Ofir Ohayon",3.2,"D"],["Ran Zakuta",2.78,"M"],
                ["Ran Cohen",3.7,"A"],["Raz Lahav",4.16,"A"],["Shon Ohana",3.2,"D"],["Yoav Zafrir",2.3,"D"]]
'''UI Seperator'''
readable_seperator = '-------------------------------------------'

'''
    Goalkeeper Turn:
        This function returns turn of a goalkeeper.
'''
def goalkeeper(lst):
    while True:
        rand = random.randrange(1,8)
        if rand in lst:
            lst.pop(lst.index(rand))
            return rand
'''
    Unregistered New Player:
        This function assures that legionnaire rating is a number and between (1.5-5.0).
'''
def legionnaire(name):
    ascii_lst = list(filter(lambda x: x in range(65, 91) or x in range(97, 123), range(65, 123)))
    while True:
        try:
            name = valid_chr(input("Enter legionnaire's full name: ").title())
            print(readable_seperator)
            if not name:
                assert not name, f"Invalid Name, Please Enter Alphabet Characters Only\n{readable_seperator}"
            else:
                break
        except:
            continue
    while True:
        try:
            leg_rating = min(float(input(f'Enter the Rating of {name}: ').strip()),5)
            print(readable_seperator)
            assert (leg_rating >= 1.5 and leg_rating <= 5), f"Invalid Rating, Please Enter Digits Only\n{readable_seperator}"
            break
        except:
            print(f"Invalid Rating, Please Enter Digits Only\n{readable_seperator}")
            continue
    while True:
        try:
            leg_position = input(f'Enter the Position of {name}: (A/M/D) ').strip().capitalize()
            print(readable_seperator)
            assert leg_position in ["A","M","D"] ,f"Invalid Position, Please Enter (A,M,D) Only\n{readable_seperator}"
            break
        except:
            print(f"Invalid Rating, Please Enter Digits Only\n{readable_seperator}")
            continue
    print(f"Press Enter To Approve {name} with {leg_rating} Rating and ({leg_position}) position, " + '\n' + f"Or Any Other Key To Start Over: \n{readable_seperator} ", end="")
    x = input()
    if x != "":
        return legionnaire(name)
    else:
        print(f"{name} registered successfully.\n{readable_seperator}")
        return [name, leg_rating, leg_position] # returning and list with legionnaire's name, rating, position.


def dup_opt_lft(lst1,lst2,name):
    lst1 = members_data
    z = name
    return (len(list(filter(lambda x: z in x[0], lst1))) -
            len(list(filter(lambda y: z in y[0], lst2))))

'''
    Lowest Rating Player
'''
def min_ind(lst):
    min_rating = 5
    for i in lst:
        if i[1] < min_rating:
            min_rating = min(i[1],min_rating)
            bottom = lst.index(i)
    return bottom

'''
    Valid Name
'''
def valid_chr(text):
      # removing unwanted spaces and titling the name for further process.
    ascii_lst = list(filter(lambda x: x in range(65, 91) or x in range(97, 123),range(65, 123)))  # list of allowed character in ascii.
    split_name = []
    for chr in str(text):
        split_name.append(chr)
        if ord(chr) != 32 and ord(chr) not in ascii_lst:  # condition of allowed character in ascii.
            print(f"Invalid Name\n{readable_seperator}")
            return

    return text
'''
    Checking for Members Players
'''
def is_member(name, lst): # Full and correct name was inserted.
    candidates = list(filter(lambda x: name == x[0], members_data))
    candidates = list(filter(lambda y: y not in lst, candidates))
    for member in candidates:
        if name == member[0]:
            return member
        else:
            continue
    return

'''
    Checking Similar First Name of Players
'''
def mul_first_name(name, lst): # list of matching first name.
    candidates = list(filter(lambda x: name == x[0][0:len(name)], members_data))
    candidates = list(filter(lambda y: y not in lst, candidates))
    dup = 0
    if len(candidates) > 0:
        return candidates
    else:
        return candidates

'''
    Printing Candidates of Similar First Name
'''
def print_candidates(name, lst):
    dup = 0
    print(f'Which {name} ?\n{readable_seperator} ')
    for i in lst:
        dup += 1
        print(f'{dup}. {i[0]}')
    dup += 1
    print(f'{dup}. Return, it was a typo !')
    dup += 1
    print(f'{dup}. Choose from library.')
    return print(f'{dup + 1}. I want to add legionnaire.\n{readable_seperator}')

'''
    Printing Options in Case There's No Candidates With Similar First Name
'''
def print_option_left(name, lst): # printing available candidates
    dup = 1
    print(f"Couldn't Find Any {name}.\n{readable_seperator}")
    print(f'{dup}. Return, it was a typo !')
    dup += 1
    print(f'{dup}. Choose from library.')
    return print(f'{dup+1}. I want to add legionnaire.\n{readable_seperator}')
'''
    Checking if a Player Already Registered
'''
def registered_players(name, lst): # checking if a player was alreay registered
    for i in lst:
        if i[0] == name:
            return name
    return

'''
    Checking for Valid choose of User
'''
def choose(name, lst):
    while True:
        try:
            selection = input(f"Select from the options above: ")
            print(readable_seperator)
            if int(selection) in list(range(1,len(lst)+1)):
                return int(selection)-1
            elif int(selection) in list(range(len(lst)+1,len(lst)+4)):
                return int(selection)
            else:
                print(f"Invalid Option\n{readable_seperator}")
                continue
        except:
            print(f"Invalid Option\n{readable_seperator}")
            continue

'''
    How Many Players Arriving Today
'''
def limit_arrival():
    while True:
        try:
            selection = input(f"{readable_seperator}\nHow Many Players Arriving Today: ")
            print(readable_seperator)
            if int(selection) in list(range(15,22)):
                return int(selection)
            else:
                print(f"Invalid Option\n{readable_seperator}")
                continue
        except:
            print(f"Invalid Option\n{readable_seperator}")
            continue

'''
    List of Players That Wasn't Added
'''
def library(lst):
    # list of players that wasn't added
    candidates = [x for x in members_data if x not in lst]
    for i,name in enumerate(candidates):
        print(f'{i+1}. {name[0]}')
    print(readable_seperator)
    while True:
        try:
            selection = input(f"Select from the options above: ")
            print(readable_seperator)
            if int(selection) in range(1,len(candidates)+1):
                print(f"{candidates[int(selection)-1][0]} registered successfully.\n{readable_seperator}")
                return candidates[int(selection)-1]
        except:
            print(f"Invalid Option\n{readable_seperator}")
            continue


    return

'''
    Main Function 1, User Inserting Players to Roster
'''
def arriving():
    players_lst = []
    total_num = limit_arrival()
    players_added = 0
    while players_added < total_num:
        print(f'Players in Roster So Far ({players_added})')
        name = valid_chr(input("Enter Player's Name: ").strip().title())
        print(readable_seperator)
        if not name:
            continue
        elif registered_players(name, players_lst):
            print(f'{name} already registered.\n{readable_seperator}')
            continue
            # try thinking on a more efficient way instead of calling the function twice.
        elif is_member(name, players_lst):
            players_lst.append(is_member(name, players_lst))
            print(f"{name} registered successfully.\n{readable_seperator}")
            players_added += 1
        elif True:
            candidates = mul_first_name(name, players_lst) # all matching names to first name given
            # if a first name given leading to a single member he will be added automatically.
            if len(candidates) == 0:
                print_option_left(name, candidates)
                selection = choose(name, "st")
                if selection + 1 == 1:
                    continue
                elif selection + 1 == 2:
                    players_lst.append(library(players_lst))
                    players_added += 1
                else:
                    players_lst.append(legionnaire(name))
                    players_added += 1

            else:
                print_candidates(name, candidates)
                selection = choose(name,candidates)
                if len(candidates) >= selection:
                    players_lst.append(candidates[selection])
                    print(f"{candidates[selection][0]} registered successfully.\n{readable_seperator}")
                    players_added += 1
                elif selection == len(candidates) + 1:
                    continue
                elif selection == len(candidates) + 2:
                    players_lst.append(library(players_lst))
                    players_added += 1
                else:
                    players_lst.append(legionnaire(name))
                    players_added += 1
    return players_lst

'''
    Main Function 2, Allocating layers to Teams.
'''
def teams():
    formation = [[], [], []]
    team1_rating = 0
    team2_rating = 0
    team3_rating = 0
    max_rating = 0
    lst = arriving()
    for gk in range(min(3,21-len(lst))):
        formation[gk].append(["Gk",3,"-"])
    for i in range(len(lst)):
        for player in lst:
            if max_rating < player[1]:
                max_rating = player[1]
                top = lst.index(player)
            else:
                bottom = min_ind(lst)
        if list(filter(lambda x: len(x) == 0, formation)):
            for team in formation:
                if not team:
                    if top > bottom:
                        team.append(lst[top])
                        team.append(lst[bottom])
                        lst.pop(top)
                        lst.pop(bottom)
                    else:
                        team.append(lst[top])
                        team.append(lst[bottom])
                        lst.pop(top)
                        lst.pop(bottom - 1)
                    max_rating = 0
                    break
        elif not list(filter(lambda x: len(x) == 0, formation)):
            for team in formation:
                if formation.index(team) == 0:
                    for player in team:
                        team1_rating += player[1]
                elif formation.index(team) == 1:
                    for player in team:
                        team2_rating += player[1]
                else:
                    for player in team:
                        team3_rating += player[1]
            if lst:
                if min(team1_rating,team2_rating,team3_rating) == team1_rating:
                    formation[0].append(lst[top])
                    lst.pop(top)
                elif min(team1_rating,team2_rating,team3_rating) == team2_rating:
                    formation[1].append(lst[top])
                    lst.pop(top)
                else:
                    formation[2].append(lst[top])
                    lst.pop(top)
            max_rating = 0
            team1_rating,team2_rating,team3_rating = 0,0,0

# This part printing the teams and selecting goalkeeper turns.
    turns = [1, 2, 3, 4, 5, 6, 7]
    x = 1
    for team in formation:
        turns_lst = deepcopy(turns)
        print(f'Team {x}: ',)
        print(readable_seperator)
        x += 1
        for player in team:
            print(f'{player}, Goalkeeper number {goalkeeper(turns_lst)}.')
        print(readable_seperator)

#teams()
