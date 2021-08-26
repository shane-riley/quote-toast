#!python3
"""
@file main.py
@Main script for random toast notification
@author Shane Riley <shane.riley@pitt.edu>
@version 1
@date 2020-11-22
"""

import win10toast
import sys
import os
import random

# Change cwd
os.chdir(os.path.dirname(sys.argv[0]))

QUOTES_FILE = "quotes.txt"
ICON_PATH = "icon.ico"
DURATION = 10
LENGTH = 50
quotes_list = []

# Load quotes into list on startup
def loadQuotes():
    with open(QUOTES_FILE, encoding="utf-8") as f:
        one_quote = ""
        for line in f:
            # Check if line empty
            if line == "\n":
                if len(one_quote) <= LENGTH:
                    quotes_list.append(one_quote)
                one_quote = ""
            else:
                one_quote = one_quote + line


# Pick a quote at random from list
def getQuote():
    return random.choice(quotes_list)

# Make notification
def toastQuote(a_quote):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Quote of the day", a_quote, icon_path=ICON_PATH, duration=DURATION)

# Main function
def main():
    loadQuotes()
    a_quote = getQuote()
    toastQuote(a_quote)


if __name__ == "__main__":
    main()