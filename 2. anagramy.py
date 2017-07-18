# -*- coding: utf-8 -*-
# gracz odgaduje słowo z podanych liter
# co mozna zrobic: dodac podpowiedzi (minus unkty), podzial na kategorie, rearanazacja liter

import time
import random
import os

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon", "klamerka", "ziemniaki", "szampon",
             "kompot", "przypadek", "pies", "chmurka", "programowanie")
used_words = []  # lista wylowowanych już w grze słów, żeby nie losowało tych samych ponownie do odgadnięcia
points = 0  # liczba zdobytych punktów w całej grze
amount = 0  # liczba wszystkich wyświetlonych słów do odgadnięcia

def begin():
    """ powitanie """
    print(u"\n\t\t*** GRA W ZGADYWANIE SŁÓW ***\n")
    time.sleep(1)
    print("Witaj!")
    time.sleep(1)
    print(u"\nZagrajmy w grę.")
    time.sleep(2)
    print(u"Ja pokazuję Ci ciąg liter, a Ty próbujesz ułożyć z nich słowo.")
    time.sleep(2)
    print(u"Za każde dobrze odgadnięte słowo otrzymujesz jeden punkt.\nMasz pięć szans na odgadnięcie jednego słowa, w przeciwnym razie nie otrzymasz punktu.")
    time.sleep(2)
    print(u"Jesteś gotowy?")
    time.sleep(2)
    print(u"Aby rozpocząć grę, wciśnij dowolny klawisz.")
    print(u"Aby się poddać lub zrezygnować, wciśnij q.")
    key = input(u"Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    return key


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    os.system('cls')
    print(u"\nGra została zakończona.")
    print(u"Liczba wszystkich słów do odgadnięcia: " + str(amount))
    print(u"Liczba zdobytych punktów: " + str(points))
    print(u"Dziękujemy za udział w grze.")
    input("Aby wyjść z programu, wciśnij Enter.")


def next_exmpl():
    """ przejście do następnego przykładu + bieżące podsumowanie """
    print(u"\nCzy przejść do następnego przykładu? Jeśli tak, wciśnij dowolny klawisz. Jeśli chcesz zakończyć grę, wciśnij q.")
    print(u"Liczba wszystkich słów do odgadnięcia: " + str(amount))
    print(u"Dotychczas zdobyte punkty: " + str(points))
    key = input()
    if key.lower() == 'q':
        end_game()
    return key


def bad_answer(used_guess):
    """ podanie złej odpowiedzi + sprawdzenie """
    print(u"\aNiestety, ale to błędna odpowiedź. Spróbuj jeszcze raz!")
    answer = input(u"Zgadnij, co to za słowo: ")
    while answer in used_guess:
        print(u"Już podawałeś tę literę. Podaj inną.")
        answer = input("Podaj literę: ")
    return answer


def new_word(word):
    """ tworzenie anagramu z wylosowanego słowa z puli """
    anagram = ""
    while word:
        pos = random.randrange(len(word))
        anagram += word[pos].upper() + " "
        word = word[:pos] + word[(pos+1):]
    print("\t\t" + str(anagram))
    return anagram


def brawo(correct):
    global points
    print(u"\nBRAWO! To właśnie słowo '" + str(correct.upper()) + "'.")
    points += 1
    key = next_exmpl()
    os.system('cls')
    return key


def main():
    key = begin()
    while key.lower() != 'q':
        if len(used_words) == len(WORDS): # wszystkie słowa z puli sa w liście wykorzystanych
            time.sleep(1)
            print(u"\aWygląda na to, że zaprezentowaliśmy Ci wszystkie słowa z naszej puli.")
            time.sleep(1)
            end_game()
            break
        used_guess = []
        os.system('cls')
        time.sleep(1)
        print(u"\nZgadnij, co to za słowo: \n")
        while True:
            word = random.choice(WORDS)
            if word in used_words:
                continue
            else:
                used_words.append(word)
                break
        correct = word # przechwycenie słowa przed zmianą go w anagram
        new_word(word)
        answer = input(u"\nJakie to słowo?\n  ")
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
                    print(u"\aNiestety nie zgadłeś! To słowo to '" + str(correct.upper()) + "'.")
                    print(u"Nie otrzymujesz punktu za to słowo.")
                    key = next_exmpl()
                    os.system('cls')
                    break
            break
main()

