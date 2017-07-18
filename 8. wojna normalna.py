# -*- coding: utf-8 -*-
# gra w wojnê - ten kto wygrywa rundê, zabiera wszystkie karty z rundy do swojej talii
# gracze otrzymuj¹ po 1 karcie, wygrywa ten z najwy¿sz¹ kart¹
# jesli jest remis, to karty z rundy przechodz¹ do "poczekalni" i zgarnia je gracz, który wygra nastêpn¹ rundê

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
    """ Gracz i to, to co trzyma w rêce """
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.again = True

    def __str__(self):
        if self.cards:
            x = "Liczba kart gracza " + str(self.name) + ": " + str(len(self.cards))
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

    def is_playing(self):
        return len(self.cards) > 0


class Deck(PlayerHand):
    """ talia kart """
    def __init__(self):
        super().__init__("Komputer")
        self.rest_cards = []

    def __str__(self):
        if self.rest_cards:
            x = "Liczba kart w poczekalni: " + str(len(self.rest_cards))
        else:
            x = "Liczba kart w poczekalni: <brak>"
        return x

    def populate(self):
        """ zape³nienie talii """
        for i in Card.RANKS:
            for x in Card.SUITS:
                card = Card(i, x)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands):
        """ rozdanie wszystkich kart """
        for i in range(52):
            if len(self.cards) >= len(hands):
                for hand in hands:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
            elif len(self.cards) < len(hands):
                for card in self.cards:
                    self.rest_cards.append(card)
                    self.cards.remove(card)
        return self.rest_cards


class Game(object):
    EMPTY = False

    def __init__(self, names):
        self.players = []
        for i in names:
            player = PlayerHand(i)
            self.players.append(player)
        self.all_players = self.players
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()
        time.sleep(2)
        print("\nRozdajemy karty!\n")
        self.deck.deal(self.players)

    def play(self):
        while not Game.EMPTY:
            if len(self.players) <= 1:
                Game.Empty = True
            time.sleep(1)
            if Game.EMPTY:
                break
            total_values = []
            for player in self.players:
                if not player.is_playing():
                    total_value = 0
                    total_values.append(total_value)
                    player.again = None
                else:
                    print(player)
                    total_value = player.cards[0].value
                    total_values.append(total_value)
            print(self.deck)
            print("")
            for player in self.players:
                if not player.is_playing():
                    continue
                else:
                    print("Karta gracza " + str(player.name) + ":\t" + str(player.cards[0]))
                    time.sleep(1)
            max_value = max(total_values)
            max_player_index = total_values.index(max_value)
            time.sleep(1)
            if total_values.count(max_value) > 1:
                print("\nMamy remis!\n")
                for player in self.players:
                    if not player.is_playing():
                        continue
                    else:
                        self.deck.rest_cards.append(player.cards[0])
                        player.cards.remove(player.cards[0])
            elif total_values.count(max_value) == 1:
                print("\nTê rundê wygrywa gracz " + str(self.players[max_player_index].name) + "!\n")
                for player in self.players:
                    if not player.is_playing():
                        continue
                    else:
                        self.players[max_player_index].cards.append(player.cards[0])
                        player.cards.remove(player.cards[0])
                for i in self.deck.rest_cards:
                    self.players[max_player_index].cards.append(i)
                self.deck.rest_cards = []
            time.sleep(1)
            for player in self.players:
                if not player.is_playing() and player.again:
                    print("Gracz " + str(player.name) + " odpada z gry!")
                    player.again = None

    def end(self):
        winners = []
        for player in self.players:
            winner = self.players[player]
            winners.append(winner)
        if len(winners) == 0:
            print("\nNikt nie wygra³")
        elif len(winners) == 1:
            print("\nMamy zwyciêzcê! Jest nim gracz " + str(winners[0]) + ".")
        time.sleep(1)


def main():
    again = ""
    while again.lower() != 'q':
        time.sleep(1)
        print("\nRozpoczynamy grê w Wojnê!\n")
        time.sleep(1)
        while True:
            try:
                number_players = int(input("WprowadŸ liczbê graczy: "))
                break
            except (ValueError, TypeError):
                print("Wprowadzono nieprawid³ow¹ wartoœæ.")
        names = []
        for i in range(number_players):
            name = input("Poda imiê " + str(i+1) + " gracza: ")
            names.append(name.capitalize())
        game = Game(names)
        Game.EMPTY = False
        while True:
            game.play()
            if Game.EMPTY:
                game.end()
                break
        time.sleep(1)
        again = input("\nCzy chcesz zagraæ jeszcze raz? ")


main()
time.sleep(1)
input("Aby zakoñczyæ grê, wciœnij Enter.")
