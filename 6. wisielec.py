# -*- coding : utf-8 -*-
# gra wisielec
# można dodać kategorie

import time
import random
import os

def begin():
    print(u"\n\t\t*** GRA WISIELEC ***\n")
    time.sleep(1)
    print("Witaj!")
    time.sleep(1)
    print(u"\nZagrajmy w wisielca.")
    time.sleep(2)
    print(u"Ja wymyślam słowo, a Ty próbujesz je odgadnąć, podając litery.")
    time.sleep(2)
    print(u"Za każde dobrze odgadnięte słowo otrzymujesz jeden punkt.")
    time.sleep(2)
    print(u"Jesteś gotowy?")
    time.sleep(2)
    print(u"Aby rozpocząć grę, wciśnij dowolny klawisz.")
    print(u"Aby się poddać lub zrezygnować, wciśnij q.")
    key = input(u"Twoja decyzja: ")
    if key.lower() == "q":
        end_game()
    return key

WORDS = ("interdyscyplinarny", "protodeklaratywy", "kompot", "przypadek", "pies", "chmurka", "programowanie", "python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon", "klamerka", "ziemniaki", "szampon")

used_words = [] # lista wylowowanych już w grze słów, żeby nie losowało tych samych ponownie do odgadnięcia
points = 0 # liczba zdobytych punktów w całej grze
amount = 0 # liczba wszystkich wyświetlonych słów do odgadnięcia


def end_game():
    os.system('cls')
    time.sleep(1)
    print(u"\nGra została zakończona.")
    print(u"Liczba wszystkich słów do odgadnięcia: " + str(amount))
    print(u"Liczba zdobytych punktów: " + str(points))
    print(u"Dziękujemy za udział w grze.")
    input("Aby wyjść z programu, wciśnij Enter.")


def next_exmpl(): # przejście do następnego przykładu + podsumowanie
    print(u"\nCzy chcesz przejść do następnego przykładu? Jeśli tak, wciśnij dowolny klawisz. Jeśli chcesz zakończyć grę, wciśnij q.")
    print(u"Liczba wszystkich słów do odgadnięcia: " + str(amount))
    print(u"Dotychczas zdobyte punkty: " + str(points))
    key = input()
    if key.lower() == "q":
        end_game()
    return key


def bad_answer(tries, word):
    if tries < 8:
        if tries == 1:
            print(""" 
        |
        |
        |
        |
        |
        |
        """)
        elif tries == 2:
            print(""" 
         ______
        |
        |
        |
        |
        |
        |
         """)
        elif tries == 3:
            print(""" 
         ______
        |      |
        |      O
        |
        |
        |
        |
        """)
        elif tries == 4:
            print(""" 
         ______
        |      |
        |      O
        |      |
        |
        |
        |
        """)
        elif tries == 5:
            print(""" 
         ______
        |      |
        |      O
        |     /|
        |
        |
        |
        """)
        elif tries == 6:
            print(""" 
         ______
        |      |
        |      O
        |     /|>
        |
        |
        |
        """)
        elif tries == 7:
            print(""" 
         ______
        |      |
        |      O
        |     /|>
        |     /
        |
        |
        """)
    if tries == 8:
        print(""" 
         ______
        |      |
        |      O
        |     /|>
        |     / \ 
        |
        |
        """)
        print(u"\nPRZEGRAŁEŚ!")
        print("To było słowo '" + str(word.upper()) +"'.")


def main():
    key = begin()
    global used_words
    global points
    global amount
    while key.lower() != 'q':
        if len(used_words) == len(WORDS): # wszystkie słowa z puli sa w liście wykorzystanych
            os.system('cls')
            time.sleep(1)
            print(u"\aWygląda na to, że zaprezentowaliśmy Ci wszystkie słowa z naszej puli.")
            time.sleep(1)
            end_game()
            break
        while True:
            word = random.choice(WORDS)
            if word in used_words:
                continue
            else:
                used_words.append(word)
                break
        amount += 1
        mod_word = [] # zamiana wylosowanego słowa na ciąg znaków, który będzie się aktualizował
        word_letters = [] # zbiór wyodrębnionych liter wylosowanego słowa
        used_letters = []  # litery wprowadzone już przez użytkownika
        correct_mod_w = []  # kompletny zbiór liter odgadniętego słowa
        for i in word:
            mod_word.append('_')
            correct_mod_w.append('_')
            word_letters.append(i)
        mod_word[0] = word[0]
        mod_word[-1] = word[-1]
        correct_mod_w = ""
        for i in word_letters:
            correct_mod_w  += " " + i
        disp_word= ""
        for i in mod_word:
            disp_word += " " + i # to, co zostanie wyświetlone użytkownikowi
        disp_word.upper()
        os.system('cls')
        time.sleep(1)
        print(u"\nOdgadnij słowo: \n\n")
        print("\t\t" + str(disp_word.upper()))
        answer = input("\nPodaj literę: ")
        tries = 0
        while True:
            try:
                while answer.lower() in word_letters:
                    for i in range(len(word_letters)): # zamiana kresek na litery
                        if word_letters[i] == answer.lower():
                            mod_word[i] = answer.lower()
                    disp_word = ""
                    for i in mod_word:
                        disp_word += " " + i
                    print(u"\n\n\nTa litera znajduje się w słowie! Podaj następną.\n")
                    used_letters.append(answer)
                    bad_answer(tries, word)
                    print("\n\t\t" + str(disp_word.upper()))
                    if disp_word == correct_mod_w:
                        print(u"\n\nBRAWO! Odgadłeś słowo! To właśnie '" + str(word.upper()) +"'.")
                        points += 1
                        word_letters = None
                        key = next_exmpl()
                        break
                    print(u"\nWykorzystane litery: " + str(used_letters))
                    answer = input(u"\nPodaj literę: ")
                    while answer in used_letters:
                        print(u"Już podawałeś tę literę. Podaj inną.")
                        answer = input("Podaj literę: ")
                while answer.lower() not in word_letters:
                    tries += 1
                    print(u"\a\n\n\nNiestety, ale taka litera nie występuje w słowie. Spróbuj jeszcze raz!\n")
                    bad_answer(tries, word)
                    if tries == 8:
                        word_letters = None
                        key = next_exmpl()
                        break
                    used_letters.append(answer)
                    print("\n\t\t" + str(disp_word.upper()))
                    print(u"\nWykorzystane litery: " + str(used_letters))
                    answer = input(u"\nPodaj literę: ")
                    while answer in used_letters:
                        print(u"Już podawałeś tę literę. Podaj inną.")
                        answer = input("Podaj literę: ")
            except TypeError:
                break
main()
