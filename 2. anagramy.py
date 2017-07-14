# -*- coding: cp1250 -*-
# gracz odgaduje s�owo z podanych liter
# co mozna zrobic: dodac podpowiedzi (minus unkty), podzial na kategorie, rearanazacja liter

import time
import random
import os

WORDS = ("python", "anagram", "�atwy", "skomplikowany", "odpowied�", "ksylofon", "klamerka", "ziemniaki", "szampon",
             "kompot", "przypadek", "pies", "chmurka", "programowanie")
used_words = []  # lista wylowowanych ju� w grze s��w, �eby nie losowa�o tych samych ponownie do odgadni�cia
points = 0  # liczba zdobytych punkt�w w ca�ej grze
amount = 0  # liczba wszystkich wy�wietlonych s��w do odgadni�cia

def begin():
    """ powitanie """
    print(u"\n\t\t*** GRA W ZGADYWANIE S��W ***\n")
    time.sleep(1)
    print("Witaj!")
    time.sleep(1)
    print(u"\nZagrajmy w gr�.")
    time.sleep(2)
    print(u"Ja pokazuj� Ci ci�g liter, a Ty pr�bujesz u�o�y� z nich s�owo.")
    time.sleep(2)
    print(u"Za ka�de dobrze odgadni�te s�owo otrzymujesz jeden punkt.\nMasz pi�� szans na odgadni�cie jednego s�owa, w przeciwnym razie nie otrzymasz punktu.")
    time.sleep(2)
    print(u"Jeste� gotowy?")
    time.sleep(2)
    print(u"Aby rozpocz�� gr�, wci�nij dowolny klawisz.")
    print(u"Aby si� podda� lub zrezygnowa�, wci�nij q.")
    key = input(u"Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    return key


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    os.system('cls')
    print(u"\nGra zosta�a zako�czona.")
    print(u"Liczba wszystkich s��w do odgadni�cia: " + str(amount))
    print(u"Liczba zdobytych punkt�w: " + str(points))
    print(u"Dzi�kujemy za udzia� w grze.")
    input("Aby wyj�� z programu, wci�nij Enter.")


def next_exmpl():
    """ przej�cie do nast�pnego przyk�adu + bie��ce podsumowanie """
    print(u"\nCzy przej�� do nast�pnego przyk�adu? Je�li tak, wci�nij dowolny klawisz. Je�li chcesz zako�czy� gr�, wci�nij q.")
    print(u"Liczba wszystkich s��w do odgadni�cia: " + str(amount))
    print(u"Dotychczas zdobyte punkty: " + str(points))
    key = input()
    if key.lower() == 'q':
        end_game()
    return key


def bad_answer(used_guess):
    """ podanie z�ej odpowiedzi + sprawdzenie """
    print(u"\aNiestety, ale to b��dna odpowied�. Spr�buj jeszcze raz!")
    answer = input(u"Zgadnij, co to za s�owo: ")
    while answer in used_guess:
        print(u"Ju� podawa�e� t� liter�. Podaj inn�.")
        answer = input("Podaj liter�: ")
    return answer


def new_word(word):
    """ tworzenie anagramu z wylosowanego s�owa z puli """
    anagram = ""
    while word:
        pos = random.randrange(len(word))
        anagram += word[pos].upper() + " "
        word = word[:pos] + word[(pos+1):]
    print("\t\t" + str(anagram))
    return anagram


def brawo(correct):
    global points
    print(u"\nBRAWO! To w�a�nie s�owo '" + str(correct.upper()) + "'.")
    points += 1
    key = next_exmpl()
    os.system('cls')
    return key


def main():
    key = begin()
    while key.lower() != 'q':
        if len(used_words) == len(WORDS): # wszystkie s�owa z puli sa w li�cie wykorzystanych
            time.sleep(1)
            print(u"\aWygl�da na to, �e zaprezentowali�my Ci wszystkie s�owa z naszej puli.")
            time.sleep(1)
            end_game()
            break
        used_guess = []
        os.system('cls')
        time.sleep(1)
        print(u"\nZgadnij, co to za s�owo: \n")
        while True:
            word = random.choice(WORDS)
            if word in used_words:
                continue
            else:
                used_words.append(word)
                break
        correct = word # przechwycenie s�owa przed zmian� go w anagram
        new_word(word)
        answer = input(u"\nJakie to s�owo?\n  ")
        used_guess.append(answer)
        global amount
        amount += 1
        tries = 1
        while True:
            if answer.lower() == correct.lower():
                key = brawo(correct)
                break
            while answer.lower() != correct.lower():
                answer = bad_answer(used_guess)
                used_guess.append(answer)
                tries += 1
                if tries <= 5 and answer.lower() == correct.lower():
                    key = brawo(correct)
                    break
                if tries == 5:
                    print(u"\aNiestety nie zgad�e�! To s�owo to '" + str(correct.upper()) + "'.")
                    print(u"Nie otrzymujesz punktu za to s�owo.")
                    key = next_exmpl()
                    os.system('cls')
                    break
            break
main()

