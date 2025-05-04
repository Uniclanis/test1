import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Hej! Välkommen till programmet. \nSvara på frågorna.')
time.sleep(2)

#Namn variabler
name_first = input("Förnamn: ").strip().title()
name_second = input("Efternamn: ").strip().title()

print(f"Tack {name_first} {name_second}!")
time.sleep(2)
print(f"Nu ska du, {name_first}, få några olika alternativ att besvara")
time.sleep(2)

clear()

#variabler
age = None
weight = None
height = None

while True:

    print(f"1. Ålder: ({age if age else 'Obesvarad'})")
    print(f"2. Vikt: ({weight if weight else 'Obesvarad'})")
    print(f"3. Längd: ({height if height else 'Obesvarad'})")
    print(f"4. Avsluta")

    choice = input("Välj alternativ 1-4: ")

    if choice == "1":
        age = input("Hur gammal är du? ")
        time.sleep(1)
        clear()
    elif choice == "2":
        weight = input("Hur mycket väger du? (Kg) ")
        time.sleep(1)
        clear()
    elif choice == "3":
        height = input("Hur lång är du? (Cm) ")
        time.sleep(1)
        clear()
    elif choice == "4":
        break
        clear()
    else:
        print("Ogiltigt val. Försök igen")
        time.sleep(2)
        clear()

    if age and weight and height:
        print("Alla uppgifter är besvarade")
        time.sleep(2)
        break

clear()

print(f"Här kommer information om dig")
time.sleep(2)
print(f"{name_first} {name_second}:")
print(f"Du är {age if age else '-'} år gammal. \nDu väger {weight if weight else '-'} kg \nDu är {height if height else '-'} cm lång.")
time.sleep(4)

print("Varning! Detta kännetecknar extrem övervikt för din ålder.")
time.sleep(3)
print("Sök hjälp!")
time.sleep(3)
