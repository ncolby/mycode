#!/usr/bin/env python3



DoctorStrange = {"Real Name" : "Stephen Strange",
        "Abilities" : ["Martial Arts", "Energy Blasts", "Sword Fighting"],
        "Aliases" : ["Sherlock", "Sorcerer Supreme", "Vincent Stephens"],
        "Universe" : "Marvel",
        "Education" : ["MD", "Extensive Sorcery Training"]
        }

DoctorStrange["Weird Fact"] = "Doctor Strange was a vampire"

choice = input("Enter something you'd like to know about Doctor Strange 'Weird Fact', 'Real Name', 'Education'\n")

print(DoctorStrange[str(choice)])

# print(DoctorStrange)
