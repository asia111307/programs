# -*- coding : utf-8 -*-
# gracz tak długo wpisuje odpowedź na pytanie trzylatka, aż nie wpisze poprawnej

import time


def begin():
    time.sleep(1)
    print(u"\n\t\t\t*** Oto program TRZYLATEK ***")
    time.sleep(2)
    print(u"\nUciekaj, póki jeszcze możesz :'(")
    time.sleep(2)
    print(u"Zaraz nasz trzyletni tester oprogramowania zbombarduje Cie pytaniami 'Dlaczego?' i nie wypuści, dopóki nie odpowiesz prawidłowo.")
    time.sleep(3)
    print(u"Czy jesteś gotowy, aby się z nim zmierzyć?\nJeśli tak, wciśnij dowolny klawisz.\nJeśli jednak wiesz, że nie podołasz i wymiękniesz, już teraz zrezygnuj, wciskając klawisz q.")
    key = input("Twoja decyzja: ")
    return key

key = begin()
if key.lower() != 'q':
    time.sleep(1)
    print(u"\nA zatem uwaga - nadciąga nasz tester! Powódź pytań zacznie się za:")
    time.sleep(2)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("!!!!!!!!\n")
    time.sleep(1)

    response = u"\n" # odpowiedź użytkownika
    poss_resp = ("dlatego", "dlatego.", "dlatego!") # możliwe warianty odpowiedzi, która zakończy program
    while response.lower() not in poss_resp:
        response = input(u"\aDlaczego?\n")
    time.sleep(1)
    print(u"\n...Aaaaa, to już wiem!")
    time.sleep(2)

    input(u"\n\t\t***** UDAŁO CI SIĘ! Serdeczne gratulacje! *****\nMożesz teraz bezpiecznie opuścić program, wciskając Enter, i psychicznie odpocząć.\n")
else:
    print("\nRozumiem Twoją decyzję. Trzymaj się!\n ")
    input("Wciśnij enter, by zakończyć program.\n")

