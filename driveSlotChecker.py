# coding: utf8
from __future__ import print_function
import datetime
import requests
from bs4 import BeautifulSoup
import time
from lxml import html
from twilio.rest import Client

client = Client("ACXXXX", "XXXXXX")
# Il s'agit de l'account_sid + auth_token récupéré depuis la console twilio http://www.twilio.com/console
 
while True: 
    # A remplacer par l'identifiant de votre drive, que l'on peut trouver 
    # dans les liens présent sur cette page : https://www.auchandrive.fr/drive/nos-drives/
    driveId = "935"
    driveUrl = "https://www.auchandrive.fr/drive/mag/anything-" + driveId

    resp = requests.get(driveUrl)
    data = resp.content
 
    soup = BeautifulSoup(data, "lxml")
    tree = html.fromstring(data)

    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end=" : ")

    isit = tree.xpath('//div[@class="next-slot__text-slot"]/text()')

    if isit:
        msg = u'Créneau Auchan Drive disponible ' + isit[0];
        print(msg)
        client.messages.create(to="+33xxx", # Votre numéro de téléphone portable
            from_="+1xxxx", # Le numéro de votre compte Twilio
            body=msg)
        break # Le script se termine
    else:
        print("Pas de créneau disponible")
        time.sleep(60*2) # Pause de 2 minutes
        continue # Et on poursuit la boucle