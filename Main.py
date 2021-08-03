### Debug TRUE
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

### First Dict
first_unlock = {
    "crea_date": "2021-08-02",
    "creator": "YDeltagon",
    "social": ["Twitch : @YDeltagon", "Twitter : @YDeltagon"]
}
### 
your_name = input("What is your name ? ")
welcome = ["Welcome ", "Hello ", "Surprise ", "Heyheyhey "]
wlc = ["Hey ", "Ho ", "Hi ", "YoLo "]

### Generate a Random number for the firts list
import random
nbwlc = random.randint(0,3)
### Generate a Random number for the second list
import random
nbwelcome = random.randint(0,3)

### Print messages
print(wlc[nbwlc] + your_name + ".")
print()
print(welcome[nbwelcome] + your_name + " on my first Python code !")

### Debug the random numbers
logging.debug(nbwlc)
logging.debug(nbwelcome)