#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program reads data from a file located on the internet"""

import urllib2
import csv
import datetime
import logging
import argparse

log = 'error.log'
logging.basicConfig(filename=log, level=logging.ERROR)
logger1 = logging.getLogger('IS211_Assignment2')


def downloadData(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data


def processData(response_data):
    myresult_dict = {}
    response_list = response_data.split("\n")
    f = open(log, 'rt')
    for rec_line in response_list[1:-1]:
        rec = rec_line.split(",")
        try:
            myresult_dict[rec[0]] = (rec[1], datetime.datetime.strptime(rec[2], "%d/%m/%Y"))
        except (ValueError):
            msg = 'Error processing line {} for ID {}'.format(rec_line[0], rec[0])
            logger1.error(msg)
            pass
        else:
            pass

    return myresult_dict


def displayPerson(id, personData):
    while id > 0:
        try:
            id = raw_input('Enter user id: ')
            pid = 'Person #{} '.format(id)
            name = 'is {} '.format(personData[id][0])
            bday = 'with a birthday of {}'.format(personData[id][1])
            record = pid + name + bday
            print record
        except:
            print 'No user found with that id'
            continue
        if id <= 0:
            print "Exiting program..."
            break

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()
    if args.url:
        url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
        csvdata = downloadData(url)
        result = processData(csvdata)
        records = displayPerson(id, result)
    else:
        print 'error'

if __name__ == '__main__':
    main()
