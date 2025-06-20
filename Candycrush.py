<<<<<<< HEAD
import random

candies = ['🍬', '🍭', '🍫', '🍩', '🧁']
size = 5
score = 0
moves = 8
lives = 3

# Fixed board for testing
board = [
    ['🍬', '🍬', '🍭', '🍬', '🍩'],
    ['🍭', '🍫', '🍩', '🍫', '🍭'],
    ['🍫', '🍭', '🍫', '🍬', '🍫'],
    ['🍩', '🍩', '🍭', '🍩', '🍬'],
    ['🍫', '🍬', '🍬', '🍭', '🍬']
]

# Displaying the board
def show():
    for row in board:
        print(' '.join(row))
    print()

# Swap two candies(swap function)
def swap(r1, c1, r2, c2):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]

# Check for matches and return points(match function)
def match():
    points = 0
    # Horizontal match
    for r in range(size):
        for c in range(size - 2):
            if board[r][c] == board[r][c+1] == board[r][c+2] != '⬜':
                board[r][c] = board[r][c+1] = board[r][c+2] = '⬜'
                points += 3
    # Vertical match
    for c in range(size):
        for r in range(size - 2):
            if board[r][c] == board[r+1][c] == board[r+2][c] != '⬜':
                board[r][c] = board[r+1][c] = board[r+2][c] = '⬜'
                points += 3
    return points

# Refilling empty spaces after matches(refill function)
def refill():
    for c in range(size):
        for r in range(size - 1, -1, -1):
            if board[r][c] == '⬜':
                for k in range(r, 0, -1):
                    board[k][c] = board[k - 1][c]
                board[0][c] = random.choice(candies)

# Get user input
def get_position():
    row = int(input(" Row (0-4): "))
    col = int(input(" Col (0-4): "))
    return row, col

# Main Game loop
print("Candy Crush -Mini Version Game")

while moves > 0 and lives > 0:
    show()
    print("Score:", score, "| Moves Left:", moves, "| Lives:", lives)
    
    try:
        print("Swap from:")
        r1, c1 = get_position()
        print("Swap to:")
        r2, c2 = get_position()
    except:
        print("❌ Invalid input. Please enter numbers between 0 and 4.")
        continue 

    swap(r1, c1, r2, c2)
    points = match()

    if points == 0:
        print("❌ No match! Swapping back.")
        swap(r1, c1, r2, c2)
        lives -= 1
    else:
        score += points
        print(f"✅ Matched! +{points} points")
        refill()

        # Handle chain matches
        while True:
            chain = match()
            if chain == 0:
                break
            score += chain
            print(f" Chain match! +{chain} points")
            refill()

    moves -= 1

# Game over
print("\n🛑 Game Over!")
show()
print("🏆 Final Score:", score)
if lives == 0:
    print("You ran out of lives!")
elif moves == 0:
=======
import random

candies = ['🍬', '🍭', '🍫', '🍩', '🧁']
size = 5
score = 0
moves = 8
lives = 3

# Fixed board for testing
board = [
    ['🍬', '🍬', '🍭', '🍬', '🍩'],
    ['🍭', '🍫', '🍩', '🍫', '🍭'],
    ['🍫', '🍭', '🍫', '🍬', '🍫'],
    ['🍩', '🍩', '🍭', '🍩', '🍬'],
    ['🍫', '🍬', '🍬', '🍭', '🍬']
]

# Displaying the board
def show():
    for row in board:
        print(' '.join(row))
    print()

# Swap two candies(swap function)
def swap(r1, c1, r2, c2):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]

# Check for matches and return points(match function)
def match():
    points = 0
    # Horizontal match
    for r in range(size):
        for c in range(size - 2):
            if board[r][c] == board[r][c+1] == board[r][c+2] != '⬜':
                board[r][c] = board[r][c+1] = board[r][c+2] = '⬜'
                points += 3
    # Vertical match
    for c in range(size):
        for r in range(size - 2):
            if board[r][c] == board[r+1][c] == board[r+2][c] != '⬜':
                board[r][c] = board[r+1][c] = board[r+2][c] = '⬜'
                points += 3
    return points

# Refilling empty spaces after matches(refill function)
def refill():
    for c in range(size):
        for r in range(size - 1, -1, -1):
            if board[r][c] == '⬜':
                for k in range(r, 0, -1):
                    board[k][c] = board[k - 1][c]
                board[0][c] = random.choice(candies)

# Get user input
def get_position():
    row = int(input(" Row (0-4): "))
    col = int(input(" Col (0-4): "))
    return row, col

# Main Game loop
print("Candy Crush -Mini Version Game")

while moves > 0 and lives > 0:
    show()
    print("Score:", score, "| Moves Left:", moves, "| Lives:", lives)
    
    try:
        print("Swap from:")
        r1, c1 = get_position()
        print("Swap to:")
        r2, c2 = get_position()
    except:
        print("❌ Invalid input. Please enter numbers between 0 and 4.")
        continue 

    swap(r1, c1, r2, c2)
    points = match()

    if points == 0:
        print("❌ No match! Swapping back.")
        swap(r1, c1, r2, c2)
        lives -= 1
    else:
        score += points
        print(f"✅ Matched! +{points} points")
        refill()

        # Handle chain matches
        while True:
            chain = match()
            if chain == 0:
                break
            score += chain
            print(f" Chain match! +{chain} points")
            refill()

    moves -= 1

# Game over
print("\n🛑 Game Over!")
show()
print("🏆 Final Score:", score)
if lives == 0:
    print("You ran out of lives!")
elif moves == 0:
>>>>>>> 80bb0d3f29114eb20b86ce4bfa04390291fa2355
    print("You ran out of moves!")