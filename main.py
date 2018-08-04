import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get('https://api.github.com/users/{}/events/public'.format(username))
    event = response.json()[0]['type']
    stamp = response.json()[0]['created_at']
    print("\n")
    print("The user {}'s latest event was {}, performed on {}".format(username,
                                                                       event,
                                                                       stamp))
    print("\n")
    answer = input("Would you like to see previous events? (y/n):    ")
    if answer.lower() == "y":
        print("\n")
        history = list(range(0, 10))
        for i in history:
            event = response.json()[i]['type']
            stamp = response.json()[i]['created_at']
            print("{} -  {}".format(event, stamp))

    else:
        pass
