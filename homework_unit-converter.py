"""Program greets user and describes what's the purpose of the program
Program asks user to enter number of kilometers.
User enters the amount of kilometers.
Program converts these kilometers into miles and prints them.
Program asks user if they'd want to do another conversion.
If yes, repeat the above process (except the greeting).
If not, program says goodbye and stops.
"""

print "Hallo! Ich rechne fuer dich gerne Kilometer in Meilen um."

while True:
    print "Bitte gib die Anzahl der Kilometer die ich fuer dich umrechnen soll, hier ein:"
    km = raw_input("Kilometer: ")

    try:
        km = float (km.replace(",", "."))

        miles = km * 0.621371

        print "{0} Kilometer sind {1} Meilen.".format(km, miles)
    except Exception as e:
        print "Please enter a number, not text!"

    choice = raw_input("Soll ich noch eine weitere Distanz fuer dich berechnen? j/n: ")

    if choice.lower() != "j" and choice.lower() != "ja":
        print "Schoen, dass du da warst und ich helfen konnte."
        break
