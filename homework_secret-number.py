#-*- coding: utf-8 -*-

# GUESS THE SECRET NUMBERS

# Varibles:
secret = 3
guess = int(raw_input("Geben Sie Ihren Vorschlag für die gesuchte Zahl ein: "))

# The Game:
if guess != secret:
    print("Leider falsch! Sie haben die gesuchte Zahl nicht erraten.")
else:
     print("Volltreffer! Sie haben die gesuchte Zahl gefunden!")