def center_point(a, b, c, d):
    if a == c and b == d:
        return f"({a:.0f}, {b:.0f})"

    if a > c and b > d:
        return f"({c:.0f}, {d:.0f})"
    else:
        return f"({a:.0f}, {b:.0f})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))

# fail
