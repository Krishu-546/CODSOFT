import random

#create empty board
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" " + board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except:
            print("Please enter valid number.")

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

def play_game():
    print("🎮 Tic Tac Toe - You (X) vs Computer (O)")
    print_board()

    while True:
        player_move()
        print_board()

        if check_winner("X"):
            print("🎉 Congratulations! You win!")
            break

        if is_draw():
            print("🤝 It's a draw!")
            break

        print("Computer's turn...")
        computer_move()
        print_board()

        if check_winner("O"):
            print("💻 Computer wins!")
            break

        if is_draw():
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
