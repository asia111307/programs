# -*- coding: cp1250 -*-
# milionerzy
import os
import random
import pickle
import sys
import time
from colorama import init, Fore, Back, Style
init()


used_questions = []  # zbi�r wykorzystanych ju� pyta�
# ko�a ratunkowe dost�pne
P = 1
H = 1
T = 1
MONEY = (500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000)
MONEY_SAFE = (0, 1000, 40000, 1000000) # progi gwarantowane


def greetings():
    """ powitanie """
    time.sleep(1)
    print(Fore.BLUE + """"\n                       ************************ """)
    print(Fore.RESET + """                         M I L I O N E R Z Y   """)
    print(Fore.BLUE + """                       ************************ """)
    print(Fore.YELLOW + """                       -- cognitive edition --  """)

    time.sleep(2)
    print(Fore.RESET + "\n\n\t\t\tWitamy w " + Fore.CYAN + "Milionerach!" + Fore.RESET)
    time.sleep(1)
    print(" To wydanie specjalne, poniewa� jest przeznaczone dla kognitywist�w.")
    time.sleep(2)
    print(" Czy jeste� gotowy, by zmierzy� si� z pytaniami i zawalczy� o milion z�otych?")
    time.sleep(2)
    print(" Je�li tak, wci�nij Enter. Je�li nie chcesz rozpoczyna� gry, wci�nij Q.")
    key = input()
    if key.lower() == 'q':
        end_game()
    return key


def user_name():
    time.sleep(1)
    name = input(" Podaj swoje imi�: ")
    print(" Zatem czas zaczyna� gr�, " + Fore.CYAN + str(name.capitalize()) + Fore.RESET + "!")
    return name


def instructions():
    """ instrukcja """
    time.sleep(1)
    print("\n Przedstawi� Ci teraz zasady gry.")
    time.sleep(2)
    print("\n Aby zosta� Milionerem, musisz odpowiedzie� na " + Fore.CYAN + "12" + Fore.RESET + " pyta�. Ka�de jest warte okre�lon� kwot� pieni�dzy.")
    time.sleep(3)
    print(" Pytania o numerach " + Fore.CYAN + "2" + Fore.RESET + " i " + Fore.CYAN + "7" + Fore.RESET +  " to pytania, na kt�re odpowied� daje Ci sum� gwarantowan�.\n")
    time.sleep(3)
    print("""    <  12   1 000 000 z� >""")
    print(Fore.CYAN + """    <  11   500 000 z� >
    <  10   250 000 z� >
     <  9   125 000 z� >
     <  8   75 000 z� >""")
    print(Fore.RESET +"""     <  7   40 000 z� >""")
    print(Fore.CYAN +"""     <  6   20 000 z� >
     <  5   10 000 z� >
     <  4   5 000 z� >
     <  3   2 000 z� >""")
    print(Fore.RESET +"""     <  2   1 000 z� >""")
    print(Fore.CYAN +"""     <  1   500 z� >""")
    time.sleep(3)
    print(Fore.RESET +"\n Do ka�dego pytania otrzymasz " +Fore.CYAN + "4 warianty odpowiedzi" + Fore.RESET + ", ale tylko " + Fore.CYAN + "jedna" + Fore.RESET + " z nich jest poprawna.")
    time.sleep(2)
    print("\n W dowolnym momencie programu mo�esz si� wycofa� (wciskaj�c klawisz " + Fore.CYAN + "Q" + Fore.RESET + ") i zatrzyma� dotychczas zdobyte pieni�dze.")
    time.sleep(3)
    print("\n Do dyspozycji masz " + Fore.CYAN + "3 ko�a ratunkowe" + Fore.RESET + ": \n Pytanie do publiczno�ci (klawisz " + Fore.CYAN + "P" + Fore.RESET + "), \n P� na p� (" + Fore.CYAN + "H"  + Fore.RESET + ") \n oraz Telefon do przyjaciela (" + Fore.CYAN + "T" + Fore.RESET + ").")
    time.sleep(4)
    print("\n\n Chyba ju� wszystko wiesz. Rozpoczynamy walk� o milion z�otych!")
    time.sleep(3)


def open_quest_pack(file, r):
    """ otwarcie zwen�trznego pliku z baz� pyta� """
    try:
        quest_file = open(file, r)
        quest_pack = pickle.load(quest_file)
        return quest_pack
    except (IOError, TypeError):
        time.sleep(1)
        print("\n\a Niestety co� posz�o nie tak... Niestety musimy zako�czy� program.")
        time.sleep(1)


def question_choice(quest_pack):
    """ losowanie pytania i wyodr�bnienie jest sk�adowych """
    while True:
        quest_box = random.choice(quest_pack)
        if quest_box in used_questions:
            continue
        else:
            used_questions.append(quest_box)
            break
    question = quest_box[0]
    answers = quest_box[1]
    correct = quest_box[2]
    return question, answers, correct


def display_quest(question, answers):
    """ wy�wietla wylosowane pytanie """
    time.sleep(1)
    print("\n Oto pytanie:\n\n")
    time.sleep(2)
    print(" " + Fore.CYAN + question + Fore.RESET + "\n")
    time.sleep(2)
    for i in answers:
        print(" " + str(i))
        time.sleep(1)
    time.sleep(1)
    print("\n\n Pami�taj, �e w ka�dym momencie gry mo�esz si� wycofa� (Q) lub skorzysta� z k� ratunkowych (P, H, T).")


def p(name):
    """ ko�o ratunkowe Publiczno�� """
    global P
    if P == 0:
        print("\n\a Niestety, to ko�o ratunkowe zosta�o przez Ciebie ju� wykorzystane.")
    else:
        P = 0
        time.sleep(1)
        print("\n\n A wi�c prosimy o pomoc Publiczno�� w studiu!")
        time.sleep(3)
        a = int(random.randrange(100))
        b = int(random.randrange((100-a)))
        c = int(random.randrange((100-a-b)))
        d = int(100-a-b-c)
        print("\n\n G�osy publiczno�ci rozk�adaj� si� nast�puj�co:\n")
        print(" A:  " + str(a) + " %")
        print(" B:  " + str(b) + " %")
        print(" C:  " + str(c) + " %")
        print(" D:  " + str(d) + " %")
    time.sleep(3)
    print("\n\n Dobrze, " + str(name.capitalize()) + ". Jaka jest Twoja decyzja? ")


def h(correct, answers, name):
    """ ko�o ratunkowe P� na p� """
    global H
    half_answ = []  # to sie wy�wietli po odrzuceniu dw�ch b��dnych odpowiedzi
    if H == 0:
        print("\a\n Niestety, to ko�o ratunkowe zosta�o przez Ciebie ju� wykorzystane.")
    else:
        H = 0
        time.sleep(2)
        print("\n\n Wybra�e� P� na p�. Prosimy komputer o odrzucenie losowo dw�ch b��dnych odpowiedzi:\n\n")
        time.sleep(3)
        ans_num = 0
        if correct == 'a': # przypisanie liczby do odpowiedzi (do tej pory mia�y literki)
            ans_num = 0
        elif correct == 'b':
            ans_num = 1
        elif correct == 'c':
            ans_num = 2
        elif correct == 'd':
            ans_num = 3
        half_answ.append(answers[ans_num]) # dodanie do listy prawid�owej odpowiedzi
        while True:  # losowanie drugiej odpowiedzi, kt�ra si� wy�wietli
            second_num = random.choice(answers)
            if second_num == answers[ans_num]:
                continue
            else:
                half_answ.append(second_num)
                break
        half_answ.sort()
        for i in half_answ:
            print(" " + str(i))
        time.sleep(1)
        print("\n\n Dobrze, " + str(name.capitalize()) + ".Jaka jest Twoja decyzja? ")
    return half_answ


def t(name, correct, i, half_answers):
    """ ko�o ratunkowe Telefon do przyjaciela"""
    global T
    if T == 0:
        print("\n\a Niestety, to ko�o ratunkowe zosta�o przez Ciebie ju� wykorzystane.")
    else:
        T = 0
        time.sleep(1)
        print("\n\n Wybra�e� Telefon do przyjaciela. Zatem dzwonimy!")
        time.sleep(3)
        NAMES = ('Darek', 'Kaziu', 'Ireneusz', 'Anastazja', 'Gra�yna', 'Janusz', 'Monika', 'Halina', 'Agnieszka', 'Brajan', 'Karina', 'D�esika', 'Marek')
        random_name = random.choice(NAMES)
        KNOWS = ('know', 'not_know')
        print("\n\n Witaj, " + str(random_name) + "! " + str(name.capitalize()) + " gra w�a�nie o " + str(MONEY[i]) + " z� i potrzebuje Twojej pomocy.")
        time.sleep(3)
        print(" Znasz ju� pytanie. Oczekujemy na Twoj� odpowied�!\n")
        time.sleep(3)
        print(" " + random_name.upper() + str(": Dobrze, postaram si� pom�c."))
        time.sleep(3)
        print(" " + random_name.upper() + str(": Hmmm..."))
        time.sleep(4)
        know = random.choice(KNOWS)
        if know == 'know':
            texts = (": Chyba znam poprawn� odpowied� na to pytanie. Wed�ug mnie jest to odpowied� ", ": Na szcz�cie wiem, jak Ci pom�c. Prawid�owa odpowied� to ", ": Ha! To akurat pami�tam ze studi�w! To na pewno ", ": To by� jeden z niewielu wyk�ad�w, kt�re pami�tam. Odpowied� to ")
            print(" " + str(random_name.upper()) + str(random.choice(texts)) + str(correct.upper()) + ".")
        elif know == 'not_know':
            rand_group = ('A', 'B', 'C', 'D')
            texts = (": Nie mam pewno�ci co do odpowiedzi na to pytanie. Obstawiam odpowied� ", ": Kurcz�, wybacz mi, ale nie pami�tam tego dok�adnie. Ale co� kojarz�, �e to b�dzie ", ": Fuck! Akurat na tych zaj�ciach mnie nie by�o. Ale mo�e zaznacz ", ": Wstyd si� przyzna�, ale nie mam pewno�ci. Ale raczej odpowied� to ")
            print(" " + str(random_name.upper()) + str(random.choice(texts)) + str(random.choice(rand_group)) + ".")
        time.sleep(3)
        print("\n\n Dobrze. Jaka jest Twoja decyzja, " + str(name.capitalize()) + "?")


def interpret_answer(correct, i, answers, good_answers, name):
    """ interpretacja wpisanej odpowiedzi """
    while True:
        key = input(" Twoja decyzja: ")
        if key.lower() not in ('a', 'b', 'c', 'd', 'p', 'h', 't', 'q'):
            print("\n\a Nie rozumiem tego polecenia. Powt�rz, prosz�.")
            continue
        if key.lower() == 'p':
            p(name)
            continue
        if key.lower() == 'h':
            h(correct, answers, name)
            continue
        if key.lower() == 't':
            t(name, correct,i, answers)
            continue
        if key.lower() == correct:
            if good_answers == 11:
                time.sleep(2)
                print("\n TAK! TAK! TAK! To by�a prawid�owa odpowed�! Wygra�e� " + Fore.CYAN + "MILION" + Fore.RESET + " z�otych!")
                time.sleep(4)
                good_answers += 1
                sum_up(good_answers)
                break
            else:
                time.sleep(2)
                print("\n\n BRAWO! To jest poprawna odpowied�!")
                time.sleep(1)
                print("\n Wygrywasz " + Fore.CYAN + str(MONEY[i]) + Fore.RESET + " z�!\n")
                time.sleep(2)
                print(" Aby przej�� do nast�pnego pytania, wci�nij Enter.")
                good_answers += 1
                input()
                break
        if key != correct and key not in ('q', 't', 'p', 'h'):
            time.sleep(2)
            print("\n\n\a Niestety, ale to niepoprawna odpowied�.")
            time.sleep(1)
            print("\n Prawid�owa odpowied� to: " + str(correct.upper()))
            time.sleep(2)
            sum_up(good_answers)
            break
        if key.lower() == 'q':
            time.sleep(1)
            print("\n Szkoda, �e zdecydowa�es si� zrezygnowa� z dalszej gry! Ale szanuj� Twoj� decyzj�.")
            time.sleep(2)
            print("\n Wygra�e� w Milionerach " + Fore.CYAN + str(MONEY[good_answers - 1]) + Fore.RESET + " z�. Na pewno przyda si� to na projekty badawcze!")
            end_game()
            break
    return good_answers


def sum_up(good_answers):
    """ podsumowanie wygranej """
    os.system('cls')
    time.sleep(2)
    prize = 0
    while True:
        if good_answers < 2:
            prize = MONEY_SAFE[0]
            print("\n Niestety tym razem nie uda�o si� nic wygra�.")
            break
        elif good_answers >= 2 and good_answers < 7 :
            prize = MONEY_SAFE[1]
        elif good_answers >= 7 and good_answers < 12:
            prize = MONEY_SAFE[2]
        elif good_answers == 12:
            prize = MONEY_SAFE[3]
        print("\n Wygra�e� w naszej grze " + Fore.CYAN + str(prize) + Fore.RESET + " z�! Na pewno przyda si� to na projekty badawcze.")
        break
    time.sleep(4)
    end_game()


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    print("\n Do zobaczenia nast�pnym razem!")
    time.sleep(2)
    input()
    sys.exit()


def main():
    key = greetings()
    while key.lower() != 'q':
        name = user_name()
        instructions()
        input()
        quest_pack = open_quest_pack("questions.dat", "rb")
        good_answers = 0
        while good_answers != 12:
            for i in range(12):
                question, answers, correct = question_choice(quest_pack)
                os.system('cls')
                time.sleep(1)
                print("\n\n Gramy o " + Fore.CYAN + str(MONEY[i]) + Fore.RESET + " z�.")
                display_quest(question, answers)
                time.sleep(2)
                good_answers = interpret_answer(correct, i, answers, good_answers, name)

main()