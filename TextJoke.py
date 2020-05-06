#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:46:37 2020

@author: clintonpotter

Pulls random joke from csv file and uses SMTP to text number of your choice.
"""

import csv, random
import smtplib

def getJoke(csvfile):
    """ Pulls random joke from CSV file"""

    jokefile = open(csvfile) #opens csv file
    jokeReader = csv.reader(jokefile) #initiates reader and assigns object
    jokeData = list(jokeReader)  #creates list object from csv object
    
    jokeline = random.randint(2,9985) #generates random integer, which corresponds to the csv line
    joke = jokeData[jokeline][1] #Pulls string from list
    print(joke)
    return joke


def sms(joke):
    carriers = {
            'att': '@mms.att.net',
            'tmobile': '@tmomail.net',
            'verizon': '@vtext.com',
            'sprint': '@page.nextel.com'}
    #Dictionary of carrier's texting SMTP formats

    to_number = '1111111111{}'.format(carriers['verizon']) #number to text
    auth = ('user@gmai.com', 'Password') #gmail authentification
    server = smtplib.SMTP("smtp.gmail.com", 587)  #intiates unsecure connection
    server.starttls() #upgrades it to secure
    server.login(auth[0], auth[1]) #inputs user info
    
    server.sendmail( auth[0], to_number, joke)
    
sms(str(getJoke('path_to_file/reddit-jokes.csv')))
