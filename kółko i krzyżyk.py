# -*- coding: cp1250 -*-
# gra w k�ko i krzy�yk

import random
import time
import os

amount = 0 # liczba wszystkich rozgrywek
won_h = 0 # liczba rozgrywek wygranych przez cz�owieka
won_c = 0 # liczba rozgrywek wygranych przez komputer
ties = 0 # liczba remis�w
X = 'X' # reprezentacja �etonu X
O = 'O' # reprezentacja �etonu O
EMPTY = '' # reprezentacja pustego miejsca na planszy
TIE = 'REMIS'
NUM_SQ = 9 # liczba p�l planszy


def begin():
    """ powitanie """
    print(u"\n\t\t*** KӣKO I KRZY�YK ***\n")
    time.sleep(1)
    print("\nWitaj!")
    time.sleep(1)
    print(u"\nZagrajmy w gr�.")
    time.sleep(2)
    print(u"Zobaczymy, czy jeste� lepszy od komputera w 'K�ko i Krzy�yk'.")
    time.sleep(2)
    print(u"Jeste� gotowy?")
    time.sleep(2)
    print(u"Aby rozpocz�� gr�, wci�nij dowolny klawisz.")
    print(u"Aby si� podda� lub zrezygnowa�, wci�nij q.")
    key = input(u"Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    else:
        instructions()
    return key


def next_exmpl():
    """ przej�cie do nast�pnej rozgrywki + bie��ce podsumowanie """
    print(u"\nCzy przej�� do nast�pnego przyk�adu? Je�li tak, wci�nij dowolny klawisz. Je�li chcesz zako�czy� gr�, wci�nij q.")
    print(u"Liczba wszystkich rozgrywek: " + str(amount))
    print(u"Liczba wygranych rozgrywek: " + str(won_h))
    print(u"Liczba przegranych rozgrywek: " + str(won_c))
    print(u"Liczba nierozstrzygni�tych rozgrywek: " + str(ties))
    key = input("Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    return key


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    os.system('cls')
    print(u"\nGra zosta�a zako�czona.")
    print(u"Liczba wszystkich rozgrywek: " + str(amount))
    print(u"Liczba wygranych rozgrywek: " + str(won_h))
    print(u"Liczba przegranych rozgrywek: " + str(won_c))
    print(u"Liczba nierozstrzygni�tych rozgrywek: " + str(ties))
    print(u"Dzi�kujemy za udzia� w grze.")
    input("Aby wyj�� z programu, wci�nij Enter.")


def instructions():
    """ instrukcja """
    os.system('cls')
    time.sleep(1)
    print(u"\nA wi�c zaczynajmy!")
    time.sleep(1)
    print("\nPozw�l, �e przedstawi� Ci instrukcj� gry.")
    time.sleep(1)
    print(u"Aby wygra� rund�, musisz ustawi� trzy swoje �etony (X lub O) w rz�dzie: pionowo, poziomo lub po przek�tnej.")
    time.sleep(3)
    print(u"Do dyspozycji masz plansz� z dziewi�cioma polami, ponumerowanymi w spos�b przedstawiony poni�ej:\n")
    time.sleep(2)
    print("""
                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
    """)
    time.sleep(1)
    print(u"\nRuchy wykonujemy na zmian�, wprowadzaj�c numer pola, na kt�re chcemy postawi� sw�j �eton (o ile pole nie jest ju� zaj�te).")
    time.sleep(1)
    print(u"Gr� zawsze rozpoczyna gracz z �etonem X.")
    time.sleep(1)
    input(u"Je�li jeste� gotowy zacz�� rozgrywk�, wci�nij Enter.")
    time.sleep(1)


def first_move():
    """ ustala, kto rozpoczyna gr� """
    os.system('cls')
    time.sleep(1)
    response = input(u"\nCzy chcesz wykona� ruch jako pierwszy?\nJe�li tak, wpisz 't', a je�li nie, wpisz 'n'(wtedy rozgrywk� zacznie komputer)")
    while response.lower() not in ("t", "n"):
        print("\nNie rozumiem, co masz na my�li. Odpowiedz jeszcze raz.")
        response = input()
    if response.lower() == 't':
        time.sleep(1)
        print(u"\nDobrze. Tw�j �eton to X. Rozpoczynasz gr�.")
        human = X
        computer = O
    elif response.lower() == 'n':
        time.sleep(1)
        print(u"\nDobrze. Tw�j �eton to O. Gr� rozpoczyna Komputer.")
        human = O
        computer = X
    time.sleep(1)
    return human, computer


def new_board():
    """ tworzy pust� plansz� do gry """
    board = []
    for i in range(NUM_SQ):
        board.append(EMPTY)
    return board


def disp_board(board):
    """ wy�wietla plansz�"""
    print("\n\n\t\t\t  ", board[0], "|", board[1], "|", board[2])
    print("\t\t\t  ", "--------")
    print("\t\t\t  ", board[3], "|", board[4], "|", board[5])
    print("\t\t\t  ", "--------")
    print("\t\t\t  ", board[6], "|", board[7], "|", board[8])


def poss_moves(board):
    """ mo�liwe ruchy - tylko puste pola"""
    moves = []
    for i in range(NUM_SQ):
        if board[i] == EMPTY:
            moves.append(i)
    return moves


def human_move(board):
    """ ruch cz�owieka """
    poss_move = poss_moves(board) # okre�lenie mo�liwych posuni��
    range = (0,1,2,3,4,5,6,7,8)
    move = None
    while move not in poss_move:
        try:
            move = int(input(u"\nPodaj pole, na kt�re chcesz po�o�y� sw�j �eton: "))
            if move not in poss_move:
                print(u"\nTo pole jest ju� zaj�te. Wybierz inne.")
        except ValueError:
            print("\nChyba wprowadzi�e� nieprawid�ow� warto��. Popraw si�.")
    print(u"Wybra�e� pole: "+ str(move))
    return move


def comp_move(board, computer, human):
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    board = board[:] # kopia tablicy do symulacji ruch�w
    time.sleep(2)
    for move in poss_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(u"\n\nKomputer wybiera pole: " + str(move))
            return move
        board[move] = EMPTY
    for move in poss_moves(board):
        board[move] = human
        if winner(board) == human:
            print(u"\n\nKomputer wybiera pole: " + str(move))
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in poss_moves(board):
            print(u"\n\nKomputer wybiera pole: " + str(move))
            return move


def next_turn(turn):
    """ zmiana wykonawcy ruchu """
    time.sleep(1)
    if turn == X:
        return O
    else:
        return X


def winner(board):
    """ ustala zwyci�c� rozgrywki """
    WIN_WAYS =  (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6),
    )
    for i in WIN_WAYS:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def win_end(the_winner, human, computer):
    """ podsumowanie o zwyci�zcy """
    time.sleep(1)
    if the_winner != TIE:
        print(u"\nMamy zwyci�zc�!")
        if the_winner == human:
            print(u"Gratulacje! Wygra�e� t� rozgrywk�!")
            global won_h
            won_h += 1
        elif the_winner == computer:
            print(u"Niestety, ale t� rozgrywk� wygra� Komputer.")
            global won_c
            won_c += 1
    else:
        print("\nMamy remis!")
        global ties
        ties += 1
    key = next_exmpl()
    return key


def main():
    key = begin()
    while key.lower() != 'q':
        os.system('cls')
        global amount
        amount += 1
        human, computer = first_move() # kto jest X, a kto O
        os.system('cls')
        board = new_board()
        disp_board(board)
        turn = X # zawsze zaczyna X
        while not winner(board):
            if turn == human:
                    move = human_move(board)
                    board[move] = human
            else:
                move = comp_move(board, computer, human)
                board[move] = computer
            disp_board(board)
            turn = next_turn(turn)
        the_winner = winner(board)
        key = win_end(the_winner, human, computer)

main()