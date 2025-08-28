def color(a, b):
    if a == b:
        return a
    s = {'🟨', '🟥', '🟦'}
    return (s - {a, b}).pop()

def bottom_color(row):
    return color(row[0], row[-1])

def next_row(row):
    return ''.join(color(row[i], row[i+1]) for i in range(len(row)-1))

def tricolor_triangle(row):
    triangle = [row]
    while len(row) > 1:
        row = next_row(row)
        triangle.append(row)
    return triangle