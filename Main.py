### Import
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
import random

### Base
welcome = ["Welcome ", "Hello ", "Surprise ", "Heyheyhey "]
wlc = ["Hey ", "Ho ", "Hi ", "YoLo "]
nbwlc = random.randint(0,3)
nbwelcome = random.randint(0,3)

### First fonc loop condition
def fonc_user_count():
    in_user_count = 0
    while in_user_count <= 0:
        in_user_count = input("Numbers of players ? ")
        try:
            in_user_count = int(in_user_count)
        except:
            print("ERROR " + in_user_count + ": Pls, enter a valide numbers")
            in_user_count = 0
        if in_user_count > 4 :
            print("max 4 players")
            in_user_count = 0
        elif in_user_count <= 0 :
            print("Pls, enter a valide numbers")
            in_user_count = 0
    return in_user_count


def fonc_user_name(user_nmb):
    in_user_name = ""
    while in_user_name == "":
        in_user_name = input("Player " + user_nmb + ", what is your name ? ")
    return in_user_name


def fonc_user_age(user_name):
    in_user_age = 0
    while in_user_age == 0:
        in_user_age = input(user_name + ", what is your age ? ")
        try:
            in_user_age = int(in_user_age)
        except:
            in_user_age = 0
            print("ERROR " + user_name + ": Pls, enter a valide numbers")
    return in_user_age


def fonc_user_select():
    user_exist = 0
    global user_age1
    global user_age2
    global user_age3
    global user_age4
    global user_name1
    global user_name2
    global user_name3
    global user_name4
    global user_count
    if user_count == 1 :
        while user_exist == 0:
            in_user_exist = input("What is your player name ? ")
            if in_user_exist == user_name1 :
                user_exist = 1
            else:
                print("ERROR " + in_user_exist + " not exist")
    elif user_count == 2 :
        while user_exist == 0:
            in_user_exist = input("What is your player name ? ")
            if in_user_exist == user_name1 :
                user_exist = 1
            elif in_user_exist == user_name2 :
                user_exist = 2
            else:
                print("ERROR " + in_user_exist + " not exist")
    elif user_count == 3 :
        while user_exist == 0:
            in_user_exist = input("What is your player name ? ")
            if in_user_exist == user_name1 :
                user_exist = 1
            elif in_user_exist == user_name2 :
                user_exist = 2
            elif in_user_exist == user_name3 :
                user_exist = 3
            else:
                print("ERROR " + in_user_exist + " not exist")
    elif user_count == 4 :
        while user_exist == 0:
            in_user_exist = input("What is your player name ? ")
            if in_user_exist == user_name1 :
                user_exist = 1
            elif in_user_exist == user_name2 :
                user_exist = 2
            elif in_user_exist == user_name3 :
                user_exist = 3
            elif in_user_exist == user_name4 :
                user_exist = 4
            else:
                print("ERROR " + in_user_exist + " not exist")
    else:
        print("WTF 1")
    return user_exist


def fonc_print_user_select(name, age):
    print()
    print(welcome[nbwelcome] + name + " on my first Python code !")
    print(name + ", you have " + str(age))
    if age == 17:
        print("Next years, mother fucker !")
    elif age == 18:
        print("WELCOME !!!")
    elif 12 <= age < 18:
        print("OMG!")
    elif age == 1 or age ==2:
        print("Liars")
    elif age > 110:
        print("Liars")
    elif age > 80:
        print("Boomers")
    elif age > 50:
        print("Keep calm")
    elif age > 18:
        print("You are Adult")
    else:
        print("You are Young")


### First Dict
owner = {
    "Twitch":" @YDeltagon", 
    "Twitter":" @YDeltagon",
    "Youtube":" YannD YDeltagon",
    "Discord":" YannD / YDeltagon#2432",
}


### Question
user_count = fonc_user_count()
if user_count == 1:
    user_name1 = fonc_user_name("1")
elif user_count == 2:
    user_name1 = fonc_user_name("1")
    user_name2 = fonc_user_name("2")
elif user_count == 3:
    user_name1 = fonc_user_name("1")
    user_name2 = fonc_user_name("2")
    user_name3 = fonc_user_name("3")
elif user_count == 4:
    user_name1 = fonc_user_name("1")
    user_name2 = fonc_user_name("2")
    user_name3 = fonc_user_name("3")
    user_name4 = fonc_user_name("4")

if user_count == 1:
    user_age1 = fonc_user_age(user_name1)
elif user_count == 2:
    user_age1 = fonc_user_age(user_name1)
    user_age2 = fonc_user_age(user_name2)
elif user_count == 3:
    user_age1 = fonc_user_age(user_name1)
    user_age2 = fonc_user_age(user_name2)
    user_age3 = fonc_user_age(user_name3)
elif user_count == 4:
    user_age1 = fonc_user_age(user_name1)
    user_age2 = fonc_user_age(user_name2)
    user_age3 = fonc_user_age(user_name3)
    user_age4 = fonc_user_age(user_name4)

user_select = fonc_user_select()


"""
### First For
for i in range(0, str(user_count)):
    fonc_user_name(str(i+1))
"""


### Print messages
if user_select == 1:
    fonc_print_user_select(user_name1, user_age1)
elif user_select == 2:
    fonc_print_user_select(user_name2, user_age2)

"""
### Print a message depending on the response
my_social = input("What network of" + owner["creator"] + " do you want to know ? ")
print("My " + my_social + " is" + owner[my_social])
"""

### Debug the random numbers
logging.debug(type(user_age1))
logging.debug(type(user_age2))
logging.debug(nbwlc)
logging.debug(nbwelcome)

"""
in_user_social = "na"
while not in_user_social == exit:
    in_user_social = input("Which social network do you want to know ? ")
        try:
            "social"
        except:
            print("ERROR : Pls, enter a valide network")
"""