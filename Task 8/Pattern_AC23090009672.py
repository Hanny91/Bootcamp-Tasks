# Prints an increasing and decreasing pattern of stars of variable size.

max_stars = 5

# Loop through rows from 1 to double max_stars.
for i in range(1, 2 * max_stars):
    # Decide wether to incerase or decrease num of stars.
    if i <= max_stars:
        num_stars = i
    else:
        num_stars = 2 * max_stars - i

    # Print the stars for the current row.
    print('*' * num_stars)