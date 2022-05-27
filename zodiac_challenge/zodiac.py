#!/usr/bin/env python3


zodiacs = {
    0: ["Monkey", "sharp, smart, curious, and mischievious"],
    1: ["Rooster", "hardworking, resourceful, courageous, and talented"],
    2: ["dog", "loyal, honest, cautious, and kind"],
    3: ["Pig", "symbol of wealth, honesty, and practicality"],
    4: ["Rat", "artistic, sociable, industrious, charming, and intelligent"],
    5: ["Ox", "strong, thorough, determined, loyal, and reliable"],
    6: ["Tiger", "courageous, enthusiastic, confident, charismatic, and a leader"],
    7: ["Hare", "vigilant, witty, quick-minded, and ingenious"],
    8: ["Dragon", "talented, powerful, lucky, and successfull"],
    9: ["Snake", "wise, like to work alone, and determined"],
    10: ["Horse", "animated, active, and energetic"],
    11: ["Sheep", "creative, resilient, gentle, mild-mannered, and shy"],
}


def main():
    name = input("What is your name??\n>")
    year = input("What year were you born??\n>")

    zodmod = int(year)%12

    print(f"{name} your zodiac sign is {zodiacs[zodmod][0]}, you are {zodiacs[zodmod][1]}")


main()
