### Debug TRUE
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

### First Dict
owner = {
    "crea_date":"2021-08-02",
    "creator":" YDeltagon",
    "Twitch":" @YDeltagon", 
    "Twitter":" @YDeltagon",
    "Youtube":" YannD YDeltagon",
    "Discord":" YannD / YDeltagon#2432",
}
### 
in_user_name = input("What is your name ? ")
in_user_age = 0
while not in_user_age > 0:
    in_user_age = input("What is your age ? ")
    try:
        in_user_age = int(in_user_age)
    except:
        in_user_age = 0
        print("ERROR : Pls, enter a valide numbers")

welcome = ["Welcome ", "Hello ", "Surprise ", "Heyheyhey "]
wlc = ["Hey ", "Ho ", "Hi ", "YoLo "]

### Generate a Random number for the firts list
import random
nbwlc = random.randint(0,3)
### Generate a Random number for the second list
import random
nbwelcome = random.randint(0,3)

### Print messages
print(wlc[nbwlc] + in_user_name + ".")
print()
print(welcome[nbwelcome] + in_user_name + " on my first Python code !")
print("You have " + str(in_user_age - 142))

### Print a message depending on the response
my_social = input("What network of" + owner["creator"] + " do you want to know ? ")
print("My " + my_social + " is" + owner[my_social])

### Debug the random numbers
logging.debug(type(in_user_age))
logging.debug(nbwlc)
logging.debug(nbwelcome)


# in_user_social = "na"
# while not in_user_social == exit:
#     in_user_social = input("Which social network do you want to know ? ")
#         try:
#             "social"
#         except:
#             print("ERROR : Pls, enter a valide network")