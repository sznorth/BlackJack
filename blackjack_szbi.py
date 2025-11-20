import turtle
import random
import time


RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]


def szbi_create_deck():
    deck = []
    for r in RANKS:
        for s in SUITS:
            deck.append((r, s))
    return deck


def szbi_calculate_hand_value(hand):
    total = 0
    aces = 0
    for rank, suit in hand:
        if rank in ["J", "Q", "K"]:
            total += 10
        elif rank == "A":
            total += 1
            aces += 1
        else:
            total += int(rank)
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1
    return total


class SZBIBlackjackGame:
    def __init__(self, screen):
        self.screen = screen
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.screen.bgcolor("darkgreen")
        self.screen.title("SZBI BlackJack v0.7")
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.message = ""
        self.game_over = True
        self.player_stood = False
        self.screen.tracer(0, 0)
        self.bind_keys()
        self.szbi_new_game()

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.szbi_new_game, "n")
        self.screen.onkey(self.player_hit, "h")
        self.screen.onkey(self.player_stand, "s")
        self.screen.onkey(self.exit_game, "Escape")

    def szbi_new_game(self):
        self.deck = szbi_create_deck()
        random.shuffle(self.deck)
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.game_over = False
        self.player_stood = False
        self.message = "Új játék: N, Lapot kérek: H, Megállok: S, Kilépés: Esc"
        self.redraw()

    def player_hit(self):
        if self.game_over:
            return
        if len(self.deck) == 0:
            return
        self.player_hand.append(self.deck.pop())
        player_value = szbi_calculate_hand_value(self.player_hand)
        if player_value > 21:
            self.game_over = True
            self.message = "Vesztettél, túlmentél a 21-en. Új játék: N"
        self.redraw()

    def player_stand(self):
        if self.game_over:
            return
        self.player_stood = True
        self.dealer_play()

    def dealer_play(self):
        while szbi_calculate_hand_value(self.dealer_hand) < 17:
            if len(self.deck) == 0:
                break
            self.dealer_hand.append(self.deck.pop())
            self.redraw()
            self.screen.update()
            time.sleep(0.5)
        self.decide_winner()
        self.redraw()

    def decide_winner(self):
        player_value = szbi_calculate_hand_value(self.player_hand)
        dealer_value = szbi_calculate_hand_value(self.dealer_hand)
        if dealer_value > 21 and player_value > 21:
            self.message = "Mindketten túlléptetek a 21-en. Döntetlen. Új játék: N"
        elif player_value > 21:
            self.message = "Vesztettél, túlmentél a 21-en. Új játék: N"
        elif dealer_value > 21:
            self.message = "Nyertél, a DEALER túllépte a 21-et. Új játék: N"
        elif player_value > dealer_value:
            self.message = "Nyertél. Új játék: N"
        elif dealer_value > player_value:
            self.message = "Vesztettél. Új játék: N"
        else:
            self.message = "Döntetlen. Új játék: N"
        self.game_over = True

    def exit_game(self):
        self.screen.bye()

    def redraw(self):
        self.t.clear()
        self.draw_layout()
        self.draw_hands()
        self.draw_values_and_message()
        self.screen.update()

    def draw_layout(self):
        self.t.penup()
        self.t.goto(-300, 0)
        self.t.pendown()
        self.t.forward(600)
        self.t.penup()

    def draw_hands(self):
        self.draw_hand(self.dealer_hand, 110, "DEALER")
        self.draw_hand(self.player_hand, -160, "Játékos")

    def draw_hand(self, hand, y, label):
        start_x = -220
        step_x = 70
        self.t.penup()
        self.t.goto(start_x, y + 120)
        self.t.write(label, align="left", font=("Arial", 14, "bold"))
        for i, card in enumerate(hand):
            x = start_x + i * step_x
            self.draw_card(x, y, card)

    def draw_card(self, x, y, card):
        rank, suit = card
        w = 50
        h = 80
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.fillcolor("white")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(w)
            self.t.left(90)
            self.t.forward(h)
            self.t.left(90)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(x + w / 2, y + h / 2 - 10)
        text = rank + suit
        self.t.write(text, align="center", font=("Arial", 12, "normal"))

    def draw_values_and_message(self):
        player_value = szbi_calculate_hand_value(self.player_hand)
        dealer_value = szbi_calculate_hand_value(self.dealer_hand)
        self.t.penup()
        self.t.goto(-280, -230)
        self.t.write("Játékos pont: " + str(player_value), align="left", font=("Arial", 14, "normal"))
        self.t.goto(-280, 200)
        self.t.write("Dealer pont: " + str(dealer_value), align="left", font=("Arial", 14, "normal"))
        self.t.goto(-280, -270)
        self.t.write(self.message, align="left", font=("Arial", 12, "normal"))