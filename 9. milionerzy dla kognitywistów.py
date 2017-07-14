# -*- coding: cp1250 -*-
# milionerzy
import os
import random
import pickle
import sys
import time
from colorama import init, Fore, Back, Style
init()


used_questions = []  # zbiór wykorzystanych już pytań
# koła ratunkowe dostępne
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
    print(" To wydanie specjalne, ponieważ jest przeznaczone dla kognitywistów.")
    time.sleep(2)
    print(" Czy jesteś gotowy, by zmierzyć się z pytaniami i zawalczyć o milion złotych?")
    time.sleep(2)
    print(" Jeśli tak, wciśnij Enter. Jeśli nie chcesz rozpoczynać gry, wciśnij Q.")
    key = input()
    if key.lower() == 'q':
        end_game()
    return key


def user_name():
    time.sleep(1)
    name = input(" Podaj swoje imię: ")
    print(" Zatem czas zaczynać grę, " + Fore.CYAN + str(name.capitalize()) + Fore.RESET + "!")
    return name


def instructions():
    """ instrukcja """
    time.sleep(1)
    print("\n Przedstawię Ci teraz zasady gry.")
    time.sleep(2)
    print("\n Aby zostać Milionerem, musisz odpowiedzieć na " + Fore.CYAN + "12" + Fore.RESET + " pytań. Każde jest warte określoną kwotę pieniędzy.")
    time.sleep(3)
    print(" Pytania o numerach " + Fore.CYAN + "2" + Fore.RESET + " i " + Fore.CYAN + "7" + Fore.RESET +  " to pytania, na które odpowiedź daje Ci sumę gwarantowaną.\n")
    time.sleep(3)
    print("""    <  12   1 000 000 zł >""")
    print(Fore.CYAN + """    <  11   500 000 zł >
    <  10   250 000 zł >
     <  9   125 000 zł >
     <  8   75 000 zł >""")
    print(Fore.RESET +"""     <  7   40 000 zł >""")
    print(Fore.CYAN +"""     <  6   20 000 zł >
     <  5   10 000 zł >
     <  4   5 000 zł >
     <  3   2 000 zł >""")
    print(Fore.RESET +"""     <  2   1 000 zł >""")
    print(Fore.CYAN +"""     <  1   500 zł >""")
    time.sleep(3)
    print(Fore.RESET +"\n Do każdego pytania otrzymasz " +Fore.CYAN + "4 warianty odpowiedzi" + Fore.RESET + ", ale tylko " + Fore.CYAN + "jedna" + Fore.RESET + " z nich jest poprawna.")
    time.sleep(2)
    print("\n W dowolnym momencie programu możesz się wycofać (wciskając klawisz " + Fore.CYAN + "Q" + Fore.RESET + ") i zatrzymać dotychczas zdobyte pieniądze.")
    time.sleep(3)
    print("\n Do dyspozycji masz " + Fore.CYAN + "3 koła ratunkowe" + Fore.RESET + ": \n Pytanie do publiczności (klawisz " + Fore.CYAN + "P" + Fore.RESET + "), \n Pół na pół (" + Fore.CYAN + "H"  + Fore.RESET + ") \n oraz Telefon do przyjaciela (" + Fore.CYAN + "T" + Fore.RESET + ").")
    time.sleep(4)
    print("\n\n Chyba już wszystko wiesz. Rozpoczynamy walkę o milion złotych!")
    time.sleep(3)


def open_quest_pack(file, r):
    """ otwarcie zwenętrznego pliku z bazą pytań """
    try:
        quest_file = open(file, r)
        quest_pack = pickle.load(quest_file)
        return quest_pack
    except (IOError, TypeError):
        time.sleep(1)
        print("\n\a Niestety coś poszło nie tak... Niestety musimy zakończyć program.")
        time.sleep(1)


def question_choice(quest_pack):
    """ losowanie pytania i wyodrębnienie jest składowych """
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
    """ wyświetla wylosowane pytanie """
    time.sleep(1)
    print("\n Oto pytanie:\n\n")
    time.sleep(2)
    print(" " + Fore.CYAN + question + Fore.RESET + "\n")
    time.sleep(2)
    for i in answers:
        print(" " + str(i))
        time.sleep(1)
    time.sleep(1)
    print("\n\n Pamiętaj, że w każdym momencie gry możesz się wycofać (Q) lub skorzystać z kół ratunkowych (P, H, T).")


def p(name):
    """ koło ratunkowe Publiczność """
    global P
    if P == 0:
        print("\n\a Niestety, to koło ratunkowe zostało przez Ciebie już wykorzystane.")
    else:
        P = 0
        time.sleep(1)
        print("\n\n A więc prosimy o pomoc Publiczność w studiu!")
        time.sleep(3)
        a = int(random.randrange(100))
        b = int(random.randrange((100-a)))
        c = int(random.randrange((100-a-b)))
        d = int(100-a-b-c)
        print("\n\n Głosy publiczności rozkładają się następująco:\n")
        print(" A:  " + str(a) + " %")
        print(" B:  " + str(b) + " %")
        print(" C:  " + str(c) + " %")
        print(" D:  " + str(d) + " %")
    time.sleep(3)
    print("\n\n Dobrze, " + str(name.capitalize()) + ". Jaka jest Twoja decyzja? ")


def h(correct, answers, name):
    """ koło ratunkowe Pół na pół """
    global H
    half_answ = []  # to sie wyświetli po odrzuceniu dwóch błędnych odpowiedzi
    if H == 0:
        print("\a\n Niestety, to koło ratunkowe zostało przez Ciebie już wykorzystane.")
    else:
        H = 0
        time.sleep(2)
        print("\n\n Wybrałeś Pół na pół. Prosimy komputer o odrzucenie losowo dwóch błędnych odpowiedzi:\n\n")
        time.sleep(3)
        ans_num = 0
        if correct == 'a': # przypisanie liczby do odpowiedzi (do tej pory miały literki)
            ans_num = 0
        elif correct == 'b':
            ans_num = 1
        elif correct == 'c':
            ans_num = 2
        elif correct == 'd':
            ans_num = 3
        half_answ.append(answers[ans_num]) # dodanie do listy prawidłowej odpowiedzi
        while True:  # losowanie drugiej odpowiedzi, która się wyświetli
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
    """ koło ratunkowe Telefon do przyjaciela"""
    global T
    if T == 0:
        print("\n\a Niestety, to koło ratunkowe zostało przez Ciebie już wykorzystane.")
    else:
        T = 0
        time.sleep(1)
        print("\n\n Wybrałeś Telefon do przyjaciela. Zatem dzwonimy!")
        time.sleep(3)
        NAMES = ('Darek', 'Kaziu', 'Ireneusz', 'Anastazja', 'Grażyna', 'Janusz', 'Monika', 'Halina', 'Agnieszka', 'Brajan', 'Karina', 'Dżesika', 'Marek')
        random_name = random.choice(NAMES)
        KNOWS = ('know', 'not_know')
        print("\n\n Witaj, " + str(random_name) + "! " + str(name.capitalize()) + " gra właśnie o " + str(MONEY[i]) + " zł i potrzebuje Twojej pomocy.")
        time.sleep(3)
        print(" Znasz już pytanie. Oczekujemy na Twoją odpowiedź!\n")
        time.sleep(3)
        print(" " + random_name.upper() + str(": Dobrze, postaram się pomóc."))
        time.sleep(3)
        print(" " + random_name.upper() + str(": Hmmm..."))
        time.sleep(4)
        know = random.choice(KNOWS)
        if know == 'know':
            texts = (": Chyba znam poprawną odpowiedź na to pytanie. Według mnie jest to odpowiedź ", ": Na szczęście wiem, jak Ci pomóc. Prawidłowa odpowiedź to ", ": Ha! To akurat pamiętam ze studiów! To na pewno ", ": To był jeden z niewielu wykładów, które pamiętam. Odpowiedź to ")
            print(" " + str(random_name.upper()) + str(random.choice(texts)) + str(correct.upper()) + ".")
        elif know == 'not_know':
            rand_group = ('A', 'B', 'C', 'D')
            texts = (": Nie mam pewności co do odpowiedzi na to pytanie. Obstawiam odpowiedź ", ": Kurczę, wybacz mi, ale nie pamiętam tego dokładnie. Ale coś kojarzę, że to będzie ", ": Fuck! Akurat na tych zajęciach mnie nie było. Ale może zaznacz ", ": Wstyd się przyznać, ale nie mam pewności. Ale raczej odpowiedź to ")
            print(" " + str(random_name.upper()) + str(random.choice(texts)) + str(random.choice(rand_group)) + ".")
        time.sleep(3)
        print("\n\n Dobrze. Jaka jest Twoja decyzja, " + str(name.capitalize()) + "?")


def interpret_answer(correct, i, answers, good_answers, name):
    """ interpretacja wpisanej odpowiedzi """
    while True:
        key = input(" Twoja decyzja: ")
        if key.lower() not in ('a', 'b', 'c', 'd', 'p', 'h', 't', 'q'):
            print("\n\a Nie rozumiem tego polecenia. Powtórz, proszę.")
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
                print("\n TAK! TAK! TAK! To była prawidłowa odpowedź! Wygrałeś " + Fore.CYAN + "MILION" + Fore.RESET + " złotych!")
                time.sleep(4)
                good_answers += 1
                sum_up(good_answers)
                break
            else:
                time.sleep(2)
                print("\n\n BRAWO! To jest poprawna odpowiedź!")
                time.sleep(1)
                print("\n Wygrywasz " + Fore.CYAN + str(MONEY[i]) + Fore.RESET + " zł!\n")
                time.sleep(2)
                print(" Aby przejść do następnego pytania, wciśnij Enter.")
                good_answers += 1
                input()
                break
        if key != correct and key not in ('q', 't', 'p', 'h'):
            time.sleep(2)
            print("\n\n\a Niestety, ale to niepoprawna odpowiedź.")
            time.sleep(1)
            print("\n Prawidłowa odpowiedź to: " + str(correct.upper()))
            time.sleep(2)
            sum_up(good_answers)
            break
        if key.lower() == 'q':
            time.sleep(1)
            print("\n Szkoda, że zdecydowałes się zrezygnować z dalszej gry! Ale szanuję Twoją decyzję.")
            time.sleep(2)
            print("\n Wygrałeś w Milionerach " + Fore.CYAN + str(MONEY[good_answers - 1]) + Fore.RESET + " zł. Na pewno przyda się to na projekty badawcze!")
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
            print("\n Niestety tym razem nie udało się nic wygrać.")
            break
        elif good_answers >= 2 and good_answers < 7 :
            prize = MONEY_SAFE[1]
        elif good_answers >= 7 and good_answers < 12:
            prize = MONEY_SAFE[2]
        elif good_answers == 12:
            prize = MONEY_SAFE[3]
        print("\n Wygrałeś w naszej grze " + Fore.CYAN + str(prize) + Fore.RESET + " zł! Na pewno przyda się to na projekty badawcze.")
        break
    time.sleep(4)
    end_game()


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    print("\n Do zobaczenia następnym razem!")
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
                print("\n\n Gramy o " + Fore.CYAN + str(MONEY[i]) + Fore.RESET + " zł.")
                display_quest(question, answers)
                time.sleep(2)
                good_answers = interpret_answer(correct, i, answers, good_answers, name)

main()