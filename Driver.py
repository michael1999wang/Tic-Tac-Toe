from Board import Board

b = Board()
turn = True

while (not b.win()):
    if (turn):
        print("Player 1: Enter the row for your X:")
        x = input()
        print("Player 1: Enter the column for your X:")
        y = input()
        b.mark_X(int(x) - 1, int(y) - 1)
        if (b.win()):
            print("Player 1 wins!!!")
    else:
        print("Player 2: Enter the row for your O:")
        x = input()
        print("Player 2: Enter the column for your O:")
        y = input()  
        b.mark_O(int(x) - 1, int(y) - 1)
        if (b.win()):
            print("Player 2 wins!!!")
    b.display()

    turn = not turn