### Debug TRUE
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

### First Dict (not use)
owner = {
    "crea_date":"2021-08-02",
    "creator":" YDeltagon",
    "Twitch""twt":" @YDeltagon", 
    "Twitter":" @YDeltagon",
    "Youtube":" YannD YDeltagon",
    "Discord":" YannD / YDeltagon#2432",
}
### User enter his name
your_name = input("What is your name ? ")

### List for future
welcome = ["Welcome ", "Hello ", "Surprise ", "Heyheyhey "]
wlc = ["Hey ", "Ho ", "Hi ", "YoLo "]

### Generate a Random number for the firts list
import random
nbwlc = random.randint(0,3)
### Generate a Random number for the second list
import random
nbwelcome = random.randint(0,3)

### Print simple messages
print(wlc[nbwlc] + your_name + ".")
print(welcome[nbwelcome] + your_name + " on my first Python code !")
print()

### Print a message depending on the response
my_social = input("What network of" + owner["creator"] + " do you want to know ? ")
print("My " + my_social + " is" + owner[my_social])

### Debug the random numbers
logging.debug(nbwlc)
logging.debug(nbwelcome)