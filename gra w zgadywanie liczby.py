# -*- coding : cp1250 -*-
# zgaduje liczbę od 1 do 100
# uwzględnia to, że użytkownik wpisał zły znak zamiast liczby
# użytkownik dostanie max 5 podpowiedzi

import time
import random
import os

def begin():
    print("\n\t\t*** GRA W ZGADYWANIE LICZBY ***\n")
    time.sleep(1)
    print("Witaj!")
    time.sleep(1)
    print (u"\nZagrajmy w grę.")
    time.sleep(2)
    print (u"Ja wymyślam liczbę z zakresu od 0 do 100, a Ty próbujesz ją odgadnąć.")
    time.sleep(2)
    print (u"Jeśli nie trafisz, dam Ci pięć podpowiedzi.")
    time.sleep(2)
    print(u"Jesteś gotowy?")
    time.sleep(1)
    print (u"Aby rozpocząć grę, wciśnij dowolny klawisz.")
    print (u"Aby się poddać lub zrezygnować, wciśnij q.")
    time.sleep(1)
    key = input()
    if key.lower() == 'q':
        end_game()
    return key



points = 0 # liczba zdobytych punktów w całej grze
amount = 0 # liczba wszystkich liczb do odgadnięcia


def guess_number(used_numbers):
    while True:
        user_number = input(u"Wprowadź liczbę: ")
        try: # sprawdzanie, czy User wprowadził prawidłowy znak oraz czy nie wpisał czegoś, co już typował wcześniej
            if user_number in used_numbers:
                print(u"\aJuż podawałeś taka liczbę. Podaj inną.")
                continue
            else:
                used_numbers.append(user_number)
                user_number = int(user_number)
            break
        except ValueError:
            print (u"\aWprowadzono nieprawidłową wartość.")
            continue
    return user_number


def end_game():
    time.sleep(1)
    os.system('cls')
    print(u"\nGra została zakończona.")
    time.sleep(1)
    print(u"Liczba wszystkich przykładów do odgadnięcia: " + str(amount))
    print(u"Liczba zdobytych punktów: " + str(points))
    input("Aby wyjść z programu, wciśnij Enter.")


def next_exmpl(): # przejście do następnego przykładu + podsumowanie
    print(u"\nCzy przejść do następnego przykładu? Jeśli tak, wciśnij dowolny klawisz. Jeśli chcesz zakończyć grę, wciśnij q.")
    print(u"Liczba wszystkich przykładów do odgadnięcia: " + str(amount))
    print(u"Dotychczas zdobyte punkty: " + str(points))
    key = input()
    if key.lower() == 'q':
        end_game()
    return key


def main():
    key = begin()
    while key.lower() != 'q':
        number = random.randint(0, 100)
        chance = 0  #użytkownik może dostać max 5 podpowiedzi, by odgadnąć liczbę
        global amount
        amount += 1
        os.system('cls')
        time.sleep(1)
        print(u"\nZgadnij, o jakiej liczbie myślę.")
        used_numbers = []  # lista wpisywanych już przez użytkownika liczb, żeby nie typował tych samych ponownie
        user_number = guess_number(used_numbers)
        global points
        while chance >= 0:
            if chance == 5 and number == user_number:
                print(u"\nBRAWO! To właśnie liczba " + str(number) + u". Aby ją odgadnąć, potrzebowałeś prób: " + str(chance+1))
                points += 1
                key = next_exmpl()
                chance = -1 # wyjście z pętli while, by zacząć nową grę
                os.system('cls')
            elif chance >= 5:
                print(u"\a\nKONIEC! Niestety nie zgadłeś :( Ta liczba to " + str(number) + ".")
                key = next_exmpl()
                chance = -1
                os.system('cls')
            while chance >= 0 and chance < 5:
                if int(user_number) > int(number):
                    chance += 1
                    print(u"\nŹle. Moja liczba jest mniejsza. Spróbuj jeszcze raz.")
                    user_number = guess_number(used_numbers)
                elif int(user_number) < int(number):
                    chance += 1
                    print(u"\nŹle. Moja liczba jest większa. Spróbuj jeszcze raz.")
                    user_number = guess_number(used_numbers)
                elif int(number) == int(user_number):
                    print(u"\nBRAWO! To właśnie liczba " + str(number) + u". Aby ją odgadnąć, potrzebowałeś prób: " + str(chance+1))
                    points += 1
                    key = next_exmpl()
                    chance = -1
                    os.system('cls')

main()