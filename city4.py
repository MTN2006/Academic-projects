def create_city_grid(filename):
    # Open the file to read
    with open(filename, 'r') as file:
        # Read the first two lines for rows and columns count
        rows = int(file.readline().strip())
        columns = int(file.readline().strip())
        
        # Initialize an empty list to store the grid
        city_grid = []
        
        # Read each line of the city grid data
        for i in range(rows):
            # Read the next line and split into integers, then append it to city_grid
            row = list(map(int, file.readline().strip().split()))
            city_grid.append(row)
    
    # Return the city grid (2D list)
    return city_grid

def display_city_grid(city_grid):
    # Loop through each row in the city grid
    for row in city_grid:
        # Use a list comprehension to format each value in the row
        formatted_row = [f"{value:>5}" for value in row]
        
        # Join the formatted values with a space and print the row
        print(" ".join(formatted_row))

def find_skyscrapers(city_grid, height_threshold):
    skyscrapers = []  # Initialize an empty list for skyscrapers
    
    # Iterate through the rows of the city grid
    for row_index in range(len(city_grid)):
        # Iterate through the columns of the current row
        for col_index in range(len(city_grid[row_index])):
            height = city_grid[row_index][col_index]

            # If the building's height exceeds the threshold, add it to the skyscrapers list
            if height > height_threshold:
                skyscrapers.append([row_index, col_index, height])

    return skyscrapers  # Return the list of skyscrapers


        


def main():
    # Prompt the user for the filename
    filename = input("Enter filename: ")
    
    # Call create_city_grid to obtain the 2D list (city grid)
    city_grid = create_city_grid(filename)
    
    # Call display_city_grid to display the city grid
    print()
    print('Metropolis Skyline Building Heights:')
    display_city_grid(city_grid)
    print()

    height_threshold = int(input('Enter a height threshold: '))#user input
    print()

    skyscrapers= find_skyscrapers(city_grid, height_threshold)

    print(f'Skyscrapers taller than {height_threshold}m:')
    for skyscraper in skyscrapers:
        row, col, height= skyscraper
        print(f'Row: {row}, Column: {col}, Height: {height}m')
    
    # Call the create_classification_grid function to get the classified grid
    classified_grid = create_classification_grid(city_grid)
    
    # Print the classified grid
    print()
    print("Classified Grid:")
    print(classified_grid)

    # Extract columns from the classified grid
    columns = extract_columns(classified_grid)
    
    # Print the columns for debugging purposes
    print("\nColumns:")
    print(columns)
    
    # Check if any column has all identical values
    if is_same(columns):
        print("Has visual appeal.")  # At least one column has all identical values
    else:
        print("Does not have visual appeal.")  # No columns with all identical values


def extract_columns(classified_grid):
    # Get the number of columns from the first row
    num_columns = len(classified_grid[0])

    # Initialize an empty list to store columns
    columns = []

    # Loop over each column index
    for col_index in range(num_columns):
        column = []  # Initialize an empty list to store the current column

        # Loop through each row and add the element at the current column index to the column list
        for row in classified_grid:
            column.append(row[col_index])

        # Append the column to the columns list
        columns.append(column)

    return columns  # Return the list of columns (2D list)

def is_same(columns):
    # Loop through each column in the list of columns
    for column in columns:
        # Check if all elements in the column are the same (i.e., set has length 1)
        if len(set(column)) == 1:
            return True  # If all values are the same, return True

    return False  # Return False if no column has all identical values


def create_classification_grid(city_grid):
    # Initialize 
    classified_grid = []

    for row in city_grid:#calculating average
        row_average= sum(row)//len(row)

        classified_row=[]

        for height in row:
            if height== row_average:
                classified_row.append(0) #if the row average=height classify as 0
            elif height <row_average: 
                classified_row.append(-1) #if height is less than row average classify as -1
            else:
                classified_row.append(1) #if height is greater than row average classify as 1
        classified_grid.append(classified_row) #append to classified grid
    return classified_grid




if __name__ == "__main__":
    main()
