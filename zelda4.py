POSSIBLE_MOVES = ["up", "down", "left", "right"]

def read_dungeon(filename):
    dungeon = []  # initialize
    with open(filename, 'r') as file:  # open file
        for line in file:  # read file and append to empty list
            row = list(line.strip())
            dungeon.append(row)
    return dungeon

def get_emoji(char):
    emoji_map = {
        'L': '🧝',  # Link
        '#': '🗿',  # Wall/obstacle
        '*': '🌿',  # Empty space
        'E': '🚪'   # Exit
    }
    return emoji_map.get(char, char)  # Return the character if it's not one of the above

def display_dungeon(dungeon):
    for row in dungeon:  # Iterate over each row in the dungeon
        a_row = ''  # Initialize an empty string for this row
        for col in row:  # Iterate over each column in the row
            a_row += get_emoji(col) + ' '  # Replace each character with its corresponding emoji
        print(a_row.strip())  # Print the row, removing the trailing space

def find_link(dungeon):
    for row_index in range(len(dungeon)):
        for col_index in range(len(dungeon[row_index])):
            if dungeon[row_index][col_index] == 'L':  # If the specific index equals an L (for Link)
                return (row_index, col_index)  # Returns the position of Link (row_index, col_index)

def find_exit(dungeon):
    for row_index in range(len(dungeon)):
        for col_index in range(len(dungeon[row_index])):
            if dungeon[row_index][col_index] == "E":  # If the specific index equals an E (for Exit)
                return (row_index, col_index)  # Returns the position of the exit (row, col)
    return None  # If no exit is found

def get_valid_moves(dungeon, pos):
    valid_moves = []
    row, col = pos
    
    # Check the move upwards (row - 1)
    if row > 0 and (dungeon[row - 1][col] == '*' or dungeon[row - 1][col] == 'E'):
        valid_moves.append((row - 1, col))
    
    # Check the move downwards (row + 1)
    if row < len(dungeon) - 1 and (dungeon[row + 1][col] == '*' or dungeon[row + 1][col] == 'E'):
        valid_moves.append((row + 1, col))
    
    # Check the move left (col - 1)
    if col > 0 and (dungeon[row][col - 1] == '*' or dungeon[row][col - 1] == 'E'):
        valid_moves.append((row, col - 1))
    
    # Check the move right (col + 1)
    if col < len(dungeon[row]) - 1 and (dungeon[row][col + 1] == '*' or dungeon[row][col + 1] == 'E'):
        valid_moves.append((row, col + 1))
    
    return valid_moves

def get_move(valid_moves, pos):
    while True:
        # Ask the user for their move
        move = input("Enter move: ").strip().lower()
        
        # Check if the move is valid (must be in POSSIBLE_MOVES)
        if move in POSSIBLE_MOVES:
            # Calculate the new position based on user input
            if move == "up":
                new_pos = (pos[0] - 1, pos[1])  # Move up means decrease the row index
            elif move == "down":
                new_pos = (pos[0] + 1, pos[1])  # Move down means increase the row index
            elif move == "left":
                new_pos = (pos[0], pos[1] - 1)  # Move left means decrease the column index
            elif move == "right":
                new_pos = (pos[0], pos[1] + 1)  # Move right means increase the column index
                
            # Check if the new position is in the list of valid moves
            if new_pos in valid_moves:
                return new_pos  # If valid, return the new position
            else:
                print("Invalid move. ",end="")
        else:
            print("Invalid move. ",end="")

def move_link(dungeon, pos, converted_move):
    current_row, current_col = pos
    new_row, new_col = converted_move

    # Update the dungeon: Remove Link from the old position and place him at the new position
    dungeon[current_row][current_col] = '*'
    dungeon[new_row][new_col] = 'L'

def main():
    filename = input('Enter filename: ')  # Get user input for the filename

    dungeon = read_dungeon(filename)  # Call read_dungeon to get dungeon as a 2D list
    display_dungeon(dungeon)  # Display the dungeon

    # Find Link's position in the dungeon
    link_position = find_link(dungeon)

    # Find the exit position
    exit_pos = find_exit(dungeon)
    

    # Game loop: Continue until Link reaches the exit
    while link_position != exit_pos:
        # Get the valid moves from Link's current position
        valid_moves = get_valid_moves(dungeon, link_position)
        
        # Get the next move from the user
        converted_move = get_move(valid_moves, link_position)
        
        # Move Link to the new position
        move_link(dungeon, link_position, converted_move)
        
        # Update Link's position
        link_position = converted_move
        
        # Display the updated dungeon
        display_dungeon(dungeon)

    # Once Link reaches the exit
    print("You have reached the exit!")
    

if __name__ == "__main__":
    main()


