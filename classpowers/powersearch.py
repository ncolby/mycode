#!/usr/bin/env python3 

from powersdata import classinfo

def main():
    username = input("Enter your name to search for your power > ").capitalize()

    for person in classinfo['all']:
        if person['name'] == username:
            print(f"My name is {person['name']}")
            print(f"My spirit animal is {person['spirit animal']}")
            print(f"My skills are {person['skill level']}")
            print(f"My super power is {person['super power']}")

main()
