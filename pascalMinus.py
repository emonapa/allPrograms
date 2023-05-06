import time

def generate_next_row(previous_row):
    row = ["-"] * (len(previous_row) + 1)
    for i in range(1, len(row)-1):
        if previous_row[i-1] == previous_row[i]:
            row[i] = "+"
    return row

def print_triangle(rows):
    print("-".center(150))
    for row in rows:
        print(" ".join(str(i) for i in row).center(150))
    print("\n" * 2)

previous_row = ["-", "-"]
rows = [previous_row]

# Ctrl-C for stopping
while True:
    next_row = generate_next_row(previous_row)
    rows.append(next_row)
    print_triangle(rows)
    time.sleep(0.5)
    previous_row = next_row


