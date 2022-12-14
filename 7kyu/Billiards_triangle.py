"""
Remember the triangle of balls in billiards? To build a classic triangle
(5 levels) you need 15 balls. With 3 balls you can build a 2-level triangle,
etc.

For more examples,

pyramid(1) == 1

pyramid(3) == 2

pyramid(6) == 3

pyramid(10) == 4

pyramid(15) == 5
Write a function that takes number of balls (≥ 1) and calculates how many
levels you can build a triangle.
"""
"""
def pyramid(n):
    i = 1
    while i<= n:
        n = n -i
        i += 1
    return i-1
"""


def pyramid(balls):
    return int((1 + 8 * balls) ** 0.5 * 0.5 - 0.5)
