import turtle
from blackjack_szbi import SZBIBlackjackGame

def main():
    root = turtle.Screen()
    root.setup(width=600, height=600)
    app = SZBIBlackjackGame(root)
    turtle.mainloop()

if __name__ == "__main__":
    main()
