# -*- coding: utf-8 -*-
# gra w kó³ko i krzy¿yk

import random
import time
import os

amount = 0 # liczba wszystkich rozgrywek
won_h = 0 # liczba rozgrywek wygranych przez człowieka
won_c = 0 # liczba rozgrywek wygranych przez komputer
ties = 0 # liczba remisów
X = 'X' # reprezentacja ¿etonu X
O = 'O' # reprezentacja ¿etonu O
EMPTY = '' # reprezentacja pustego miejsca na planszy
TIE = 'REMIS'
NUM_SQ = 9 # liczba pól planszy


def begin():
    """ powitanie """
    print("\n\t\t*** KÓŁKO I KRZYŻYK ***\n")
    time.sleep(1)
    print("\nWitaj!")
    time.sleep(1)
    print("\nZagrajmy w grę.")
    time.sleep(2)
    print("Zobaczymy, czy jesteś lepszy od komputera w 'Kółko i Krzyżyk'.")
    time.sleep(2)
    print("Jesteś gotowy?")
    time.sleep(2)
    print("Aby rozpocząć grę, wciśnij dowolny klawisz.")
    print("Aby się poddać lub zrezygnować, wciśnij q.")
    key = input("Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    else:
        instructions()
    return key


def next_exmpl():
    """ przejœcie do nastêpnej rozgrywki + bie¿¹ce podsumowanie """
    print("\nCzy przejść do następnego przykładu? Jeśli tak, wciśnij dowolny klawisz. Jeśli chcesz zakończyć grę, wciśnij q.")
    print("Liczba wszystkich rozgrywek: " + str(amount))
    print("Liczba wygranych rozgrywek: " + str(won_h))
    print("Liczba przegranych rozgrywek: " + str(won_c))
    print("Liczba nierozstrzygniętych rozgrywek: " + str(ties))
    key = input("Twoja decyzja: ")
    if key.lower() == 'q':
        end_game()
    return key


def end_game():
    """ koniec gry + podsumowanie """
    time.sleep(1)
    os.system('cls')
    print("\nGra została zakończona.")
    print("Liczba wszystkich rozgrywek: " + str(amount))
    print("Liczba wygranych rozgrywek: " + str(won_h))
    print("Liczba przegranych rozgrywek: " + str(won_c))
    print("Liczba nierozstrzygniętych rozgrywek: " + str(ties))
    print("Dziękujemy za udział w grze.")
    input("Aby wyjść z programu, wciśnij Enter.")


def instructions():
    """ instrukcja """
    os.system('cls')
    time.sleep(1)
    print("\nA więc zaczynajmy!")
    time.sleep(1)
    print("\nPozwól, że przedstawię Ci instrukcję gry.")
    time.sleep(1)
    print("Aby wygrać rundę, musisz ustawić trzy swoje żetony (X lub O) w rzędzie: pionowo, poziomo lub po przekątnej.")
    time.sleep(3)
    print("Do dyspozycji masz planszę z dziewięcioma polami, ponumerowanymi w sposób przedstawiony poniżej:\n")
    time.sleep(2)
    print("""
                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
    """)
    time.sleep(1)
    print("\nRuchy wykonujemy na zmianę, wprowadzając numer pola, na które chcemy postawiæ swój żeton (o ile pole nie jest już zajęte).")
    time.sleep(1)
    print("Grę zawsze rozpoczyna gracz z żetonem X.")
    time.sleep(1)
    input("Jeśli jesteś gotowy zacząć rozgrywkę, wciśnij Enter.")
    time.sleep(1)


def first_move():
    """ ustala, kto rozpoczyna grê """
    os.system('cls')
    time.sleep(1)
    response = input(u"\nCzy chcesz wykonać ruch jako pierwszy?\nJeśli tak, wpisz 't', a jeśli nie, wpisz 'n'(wtedy rozgrywkę zacznie komputer)")
    while response.lower() not in ("t", "n"):
        print("\nNie rozumiem, co masz na myśli. Odpowiedz jeszcze raz.")
        response = input()
    if response.lower() == 't':
        time.sleep(1)
        print(u"\nDobrze. Twój żeton to X. Rozpoczynasz grę.")
        human = X
        computer = O
    elif response.lower() == 'n':
        time.sleep(1)
        print(u"\nDobrze. Twój żeton to O. Grę rozpoczyna Komputer.")
        human = O
        computer = X
    time.sleep(1)
    return human, computer


def new_board():
    """ tworzy pust¹ planszê do gry """
    board = []
    for i in range(NUM_SQ):
        board.append(EMPTY)
    return board


def disp_board(board):
    """ wyœwietla planszê"""
    print("\n\n\t\t\t  ", board[0], "|", board[1], "|", board[2])
    print("\t\t\t  ", "--------")
    print("\t\t\t  ", board[3], "|", board[4], "|", board[5])
    print("\t\t\t  ", "--------")
    print("\t\t\t  ", board[6], "|", board[7], "|", board[8])


def poss_moves(board):
    """ mo¿liwe ruchy - tylko puste pola"""
    moves = []
    for i in range(NUM_SQ):
        if board[i] == EMPTY:
            moves.append(i)
    return moves


def human_move(board):
    """ ruch cz³owieka """
    poss_move = poss_moves(board) # okreœlenie mo¿liwych posuniêæ
    range = (0,1,2,3,4,5,6,7,8)
    move = None
    while move not in poss_move:
        try:
            move = int(input("\nPodaj pole, na które chcesz położyć swój żeton: "))
            if move not in poss_move:
                print("\nTo pole jest już zajęte. Wybierz inne.")
        except ValueError:
            print("\nChyba wprowadziłeś nieprawidłową wartość. Popraw się.")
    print("Wybrałeś pole: "+ str(move))
    return move


def comp_move(board, computer, human):
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    board = board[:] # kopia tablicy do symulacji ruchów
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
    """ ustala zwyciê¿cê rozgrywki """
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
    """ podsumowanie o zwyciêzcy """
    time.sleep(1)
    if the_winner != TIE:
        print("\nMamy zwycięzcę!")
        if the_winner == human:
            print("Gratulacje! Wygrałeś tę rozgrywkę!")
            global won_h
            won_h += 1
        elif the_winner == computer:
            print("Niestety, ale tę rozgrywkę wygrał Komputer.")
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
