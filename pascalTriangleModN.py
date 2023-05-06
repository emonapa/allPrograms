import time

modN = 2

def generate_next_row(previous_row):
    row = [1] + [previous_row[i] + previous_row[i+1] for i in range(len(previous_row)-1)] + [1]
    row = [num % modN for num in row]
    return row

def print_triangle(rows):
    print("-".center(150))
    for row in rows:
        row = [str(num % modN) for num in row]
        print(" ".join(row).center(150))
    print("\n" * 2)

previous_row = [1]
rows = [previous_row]

# Ctrl-C for stopping
while True:
    next_row = generate_next_row(previous_row)
    rows.append(next_row)
    print_triangle(rows)
    time.sleep(0.3)
    previous_row = next_row
