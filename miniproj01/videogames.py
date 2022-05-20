#!/usr/bin/env python3

from data import category

def main():

    #helper functions
    def results(userChoice):
        if userChoice in category:
            print(category[userChoice])
    # initial input for getting a suggestion...
    start = input("Welcome! Would you like help getting a video game suggestion?? [y] or [n]").lower()

    
    # conditional statement checking if user wants help or not...
    if start == "y":
        print("Perfect! Let's get started.")
        catchoice = input("""
        Pick a video game category you're interested in, for suggestions type [s],
        otherwise enter a category you know you enjoy.
        >""")
        if catchoice in category:
            results(catchoice)
        else:
            count = 0
            while catchoice == "s" and count < len(category):
                for genre, value in category.items(): 
                    print(genre)
                    decision = input("Do you want this category [y] or [n]?").lower()
                    if decision == "n":
                        count += 1
                        continue
                    elif decision == "y":
                        results(genre)
                        break
                break
    else:
        print("Why you run this file then?")
main()
