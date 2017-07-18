# -*- coding : utf-8 -*-
# odwrócona gra w zgadywanie - teraz zgaduje komputer
# user podaje liczbę, a komputer ją zgaduje. Dostaje 5 podpowiedzi od Usera
# podpowiedzi Usera są generowane przez komputer

import time
import random
import os

def begin():
    print(u"\n\t\t*** GRA W ZGADYWANIE LICZBY PRZEZ KOMPUTER***\n")
    time.sleep(1)
    print("Witaj!")
    time.sleep(1)
    print(u"\nZagrajmy w grę.")
    time.sleep(2)
    print(u"Teraz to Ty, drogi Graczu, wymyślasz liczbę z zakresu od 0 do 100, a ja próbuję ją odgadnąć.")
    time.sleep(3)
    print(u"Mam pięć szans. Jesteś gotowy?")
    time.sleep(1)
    print(u"Aby rozpocząć grę, wciśnij dowolny klawisz.")
    print(u"Aby się poddać lub zrezygnować, wciśnij q.")
    time.sleep(1)
    key = input()
    if key.lower() == "q":
        end_game()
    return key


def guess_number(): # User wymyśla liczbę i wpisuje ją
    while True:
        user_number = input(u"\nPomyśl jakąś liczbę z zakresu od 0 do 100: \n")
        try: # sprawdzanie, czy User wprowadził prawidłowy znak
            user_number = int(user_number)
            if user_number < 0 or user_number > 100: # sprawdzenie, czy User wpisał liczbę z dobrego przedziału
                print(u"\a\nCoś czuję, że wprowadziłeś złą liczbę... Spróbuj jeszcze raz.")
                continue
            break
        except ValueError:
            print(u"\aWprowadzono nieprawidłową wartość.")
            continue
    return user_number


def random_comp_choice(a, b, used_numbers): # komputer zgaduje liczbę. Uwzględnia wcześniejsze podpowiedzi co do przedziałów
    time.sleep(2)
    print(u"KOMPUTER: Hmmm... No dobrze, no to może...")
    time.sleep(1)
    while True:
        number = random.randint(int(a), int(b))
        if number in used_numbers:
            continue
        else:
            used_numbers.append(number)
            break
    print(u"Czy to " + str(number) + "?")
    time.sleep(2)
    return number


def play_again():
    print(u"\nCzy chcesz zagrać jeszcze raz? Jeśli tak, wciśnij dowolny klawisz. Jeśli nie, wciśnij q.")
    key = input()
    if key.lower() == "q":
        end_game()
    return key


def end_game():
    os.system('cls')
    time.sleep(1)
    print(u"\nGra została zakończona.")
    time.sleep(2)

def main():
    key = begin()
    while key.lower() != 'q':
        os.system('cls')
        time.sleep(1)
        used_numbers = []  # lista wylowowanych już przez komputer liczb, żeby nie typował tych samych ponownie
        user_number = guess_number()
        chance = 0 # maksymalna liczba szans na odgadnięcie liczby dla komputera: 5
        time.sleep(1)
        number = int(random.randint(0, 100))
        print(u"\nNo to zgaduję!")
        print(u"Czy ta liczba to " + str(number) + "?")
        if int(user_number) == int(number):
            print(u"USER: BRAWO! To właśnie liczba " + str(user_number) + ".")
            key = play_again()
        elif int(user_number) > int(number):
            number1 = 100 # liczba, do której komputer ma się odnieść, budując pierwszy przedział na zgadywanie liczby
        elif int(user_number) < int(number):
            number1 = 0
        while chance >= 0:
            if chance == 5 and int(number) == int(user_number):
                print(u"\nUSER: BRAWO! To właśnie liczba " + str(user_number) + u". Aby ją odgadnąć, potrzebowałeś " + str(chance+1) + u" prób!")
                key = play_again()
                chance = -1 # wyjście z pętli while, by zacząć grę od początku
            elif chance >= 5:
                print(u"\a\nUSER: KONIEC GRY! Niestety nie zgadłeś :( Ta liczba to " + str(user_number) + ".")
                key = play_again()
                chance = -1
            while chance >= 0 and chance < 5:
                if int(number) > int(user_number):
                    chance += 1
                    print(u"\nUSER: Źle. Moja liczba jest mniejsza. Spróbuj jeszcze raz.")
                    old = number # przechwycenie liczby przed jej zmianą, by móc ją uwzględnić w przedziale
                    number = random_comp_choice(number1, old, used_numbers)
                    if int(number) < int(user_number):
                        number1 = old
                elif int(number) < int(user_number):
                    chance += 1
                    print(u"\nUSER: Źle. Moja liczba jest większa. Spróbuj jeszcze raz.")
                    old = number
                    number = random_comp_choice(old, number1, used_numbers)
                    if int(number) > int(user_number):
                        number1 = old
                elif int(number) == int(user_number):
                    print(u"\nUSER: BRAWO! To właśnie liczba " + str(user_number) + u". Potrzebowałeś prób: " + str(chance+1))
                    key = play_again()
                    chance = -1

main()
