# -*- coding: cp1250 -*-
# jednokartowa gra w wojnę
# gracze otrzymują po 1 karcie, wygrywa ten z najwyższą kartą

import random
import time


class Card(object):
    """ jakakolwiek karta """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = self.rank + self.suit

    def __str__(self):
        return self.card

    @property
    def value(self):
        if "J" in self.card:
            value = 11
        elif "Q" in self.card:
            value = 12
        elif "K" in self.card:
            value = 13
        elif "A" in self.card:
            value = 14
        else:
            index = Card.RANKS.index(self.rank)
            value = index + 1
        return value


class PlayerHand(object):
    """ Gracz i to, to co trzyma w ręce """
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.points = 0

    def __str__(self):
        x = "Karta gracza " + str(self.name) + ": "
        if self.cards:
            for i in self.cards:
                x += str(i) + "\t"
        else:
            x = "<brak>"
        return x

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, other_hand):
        """ przekazywanie sobie kart """
        self.cards.remove(card)
        other_hand.add(card)


class Deck(PlayerHand):
    """ talia kart """
    def populate(self):
        """ zapełnienie talii """
        for i in Card.RANKS:
            for x in Card.SUITS:
                card = Card(i, x)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """ rozdawanie kart """
        if len(self.cards) >= len(hands):
            for i in range(per_hand):
                for hand in hands:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
        elif len(self.cards) <= len(hands):
            print("W talii nie ma wystarczającej liczby kart!")
            Game.EMPTY = True


class Game(object):
    EMPTY = False

    def __init__(self, names):
        self.players = []
        for i in names:
            player = PlayerHand(i)
            self.players.append(player)
        self.deck = Deck("Komputer")
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        while not Game.EMPTY:
            time.sleep(2)
            print("\nRozdajemy karty!")
            print("Liczba kart w talii: " + str(len(self.deck.cards)) + str("\n"))
            time.sleep(1)
            self.deck.deal(self.players)
            if Game.EMPTY:
                break
            total_values = []
            for player in self.players:
                print(player)
                time.sleep(1)
                total_value = player.cards[0].value
                total_values.append(total_value)
            max_value = max(total_values)
            max_player_index = total_values.index(max_value)
            time.sleep(1)
            if total_values.count(max_value) > 1:
                print("\nMamy remis!")
            else:
                print("\nTę rundę wygrywa gracz " + str(self.players[max_player_index].name) + "!")
                self.players[max_player_index].points += 1
            for player in self.players:
                player.clear()

    def end(self):
        points = []
        for player in self.players:
            total_points = player.points
            points.append(total_points)
        win_points = max(points)
        amount_win = points.count(win_points)
        time.sleep(1)
        if win_points == 0:
            print("\nNikt nie wygrał!")
        elif amount_win > 1:
            winners = []
            print("\nMamy kilku zwycięzców!")
            for player in self.players:
                if player.points == win_points:
                    winners.append(player.name)
            print("Wygrali gracze: ")
            for i in winners:
                print(str(i) + ", ")
        elif amount_win == 1:
            winner_index = points.index(win_points)
            winner = self.players[winner_index].name
            print("\nMamy zwycięzcę! Jest nim gracz " + str(winner) + ".")
        time.sleep(1)
        print("\nPunkty uzyskane przez wszystkich graczy: ")
        for player in self.players:
            print("Gracz " + str(player.name) + ":\t" + str(player.points))


def main():
    again = ""
    while again.lower() != 'q':
        time.sleep(1)
        print("\nRozpoczynamy grę w Wojnę!\n")
        time.sleep(1)
        while True:
            try:
                number_players = int(input("Wprowadź liczbę graczy: "))
                break
            except (ValueError, TypeError):
                print("Wprowadzono nieprawidłową wartość.")
        names = []
        for i in range(number_players):
            name = input("Poda imię " + str(i+1) + " gracza: ")
            names.append(name.capitalize())
        game = Game(names)
        Game.EMPTY = False
        while True:
            game.play()
            if Game.EMPTY:
                game.end()
                break
        time.sleep(1)
        again = input("\nCzy chcesz zagrać jeszcze raz? ")


main()
time.sleep(1)
input("Aby zakończyć grę, wciśnij Enter.")
