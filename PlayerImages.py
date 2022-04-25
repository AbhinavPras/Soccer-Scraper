import webbrowser
import time
import sys
import datetime
import math
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from countdown import countdown

waittime = int(input("Time between rounds (seconds): "))   
KillSwitch = input("Kill program after image find? ")
d = input("Enter program: ")
rounds = int(input("How many rounds: "))

df = pd.read_excel('Python.xlsx')
col_Name = df['Player']
col_ID = df['ID']

list_Name = col_Name.values.tolist()
list_ID = col_ID.values.tolist()

found = 0
countID = 0
Switch = 0
Minutes = 0
totalcount = 0
foundNR = ''

for z in list_ID:
    totalcount = totalcount + 1
    
for x in range(rounds):

    countI = 0
    countJ = 0

    print("Round " + str(x))
    #print ("Current time: " + now.strftime("%H:%M:%S"))

    if x > 0:     
        s2 = time.time()
        tdelta = s2 - now
        Minutes = math.floor(tdelta / 60)
        print("Time between rounds: " + str(Minutes) + " minute " + str(round(round(tdelta, 2) - (Minutes * 60), 2)) + " seconds")
        print("ID per second: " + str(round(countID / tdelta, 2)))
        countID = 0
        
        print("Waiting")
        time.sleep(waittime)    #countdown(mins=0, secs=waittime)

    
    now = time.time()
        
    for i in list_ID:
              
        countJ = 0
        countI = countI + 1
        countID = countID + 1
              
        a = "https://eaassets-a.akamaihd.net/fifa/u/f/fm22/prod/s/static/players/players_22/p"
        c = "_"
        e = ".png"

        if (found == 1 and foundNR == str(i)) or Switch == 1:
            if Switch == 0:
                webbrowser.open("https://cdn.discordapp.com/attachments/371215854186135562/748182642347737131/all-done.png")

            if Switch == 1:
                print("Killing program in")
                countdown(mins=0, secs=10)
            sys.exit()

        url = a + str(i) + c + d + e
        req = Request(url)
        Link = url

        try:
            response = urlopen(req)

        except HTTPError as e:
            countJ = countI - 1
            for j in list_Name[countJ:]:
                print("No Image: " + str(i) + " - " + str(j) + " (" + str(countI) + "/" + str(totalcount) + ")")
                break

        else:
            countJ = countI - 1
            for j in list_Name[countJ:]:
                print("Image: " + str(i) + " - " + str(j) + " (" + str(countI) + "/" + str(totalcount) + ")")
                webbrowser.open(Link)
                break

            if found == 0:
                foundNR = str(i)
                found = 1
                waittime = 0
            if KillSwitch == "y":
                Switch = 1
