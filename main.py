import time
import requests
from csv import reader

# Need create folder "img" !!!!!!!!!!!!!!!!!!!!!!

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"
           }
number = 1

with open("urls.csv", 'r') as csv_file:
    for line in reader(csv_file):
        print(str(line))
        img_data = requests.get(url=line[0], headers=headers).content

        with open("img/" + str(number) + '.png', 'wb') as handler:
            handler.write(img_data)
            number += 1
            # time.sleep(0.5)
