#!/usr/bin/env python3

# Python libraries
from pprint import pprint

import requests
import json
import re
from random import randint
import os.path
import time
# from refinery import xtp
from ioc_finder import find_iocs

# Choose a working directory path
pathDirectory = os.path.dirname(os.path.realpath(__file__)) + "/data"


# Color setup
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def printAscii():
    """
    ASCII Art
    """
    print("""
  _____          _       _____ ____   _____ ______      _                  _             
 |  __ \        | |     |_   _/ __ \ / ____|  ____|    | |                | |            
 | |__) |_ _ ___| |_ ___  | || |  | | |    | |__  __  _| |_ _ __ __ _  ___| |_ ___  _ __ 
 |  ___/ _` / __| __/ _ \ | || |  | | |    |  __| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
 | |  | (_| \__ \ ||  __/_| || |__| | |____| |____ >  <| |_| | | (_| | (__| || (_) | |   
 |_|   \__,_|___/\__\___|_____\____/ \_____|______/_/\_\\__|_|  \__,_|\___|\__\___/|_|   
        """)


def checkPastebinAPIStatut():
    """
    This function check Pastebin API statut access : allowed / not allowed
    """
    requestPastebinAPI = requests.get('https://scrape.pastebin.com/api_scraping.php')
    if requestPastebinAPI.status_code == 200:
        print(
            f"IP Access  : Your IP address is {bcolors.OKGREEN}allowed{bcolors.ENDC} to connect to the Pastebin.com API")
    else:
        print(
            f"IP Access  : Your IP address is {bcolors.FAIL}not allowed{bcolors.ENDC} to connect to the Pastebin.com API")
        print("Please visit this webpage: https://pastebin.com/doc_scraping_api ")
        print("Then, enter the IP address of your machine in section: 'Your Account & Whitelisted IP'")
        exit()


def pastebinRequest():
    # Create daily directory
    todayDate = time.strftime("%d-%m-%y")
    directory = pathDirectory + "/" + todayDate
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        # Pastebin request
        jsonResponse = requests.get("https://scrape.pastebin.com/api_scraping.php").json()
        for element in jsonResponse:
            scrape_url = element["scrape_url"]
            key = element["key"]
            request = requests.get(scrape_url)
            download = request.text
            filename = (str(key) + ".txt")
            if os.path.isfile(filename) is True:
                pass
            else:
                savepath = directory + "/"
                savedPastePath = os.path.join(savepath, filename)
                print(savedPastePath)
                with open(savedPastePath, "w") as savedPasteFile:
                    savedPasteFile.write(download)
                pprint(find_iocs(download))
                quit()

        print("Sleeping time between 60-100 seconds")
        time.sleep(randint(60, 100))
    except Exception as e:
        print(e)


# Entry point of the script
def main():
    printAscii()
    checkPastebinAPIStatut()
    pastebinRequest()
    while True:
        pastebinRequest()


if __name__ == '__main__':
    main()
