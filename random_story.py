#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:18:43 2022

@author: annamarakasova
"""

print("""Let's create a story! :)
You will be prompted to answer some questions.
Give random answers and let's see what story gets written!""")
who = input("Who?\n>>>")
when = input("When?\n>")
with_who = input("With who?\n>>>")
action = input("What did they do?\n>>>")
consequences = input("What were the consequences of that?\n>>>")
people = input("What did people say about it?\n>>>")

story = f"""{who} {action} {with_who} {when}. As a result,
{consequences}, and people around said that {people}"""

print(story)