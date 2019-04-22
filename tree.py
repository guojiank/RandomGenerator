import turtle as turtle


def draw_tree():
    pass


def generate_tree(length, min_length=5):
    rote = 0.7
    turtle.forward(length)
    if length > min_length:
        turtle.left(45)
        generate_tree(rote * length)
        turtle.right(90)
        generate_tree(rote * length)
        turtle.left(45)
    turtle.back(length)


if __name__ == "__main__":
    turtle.left(90)
    generate_tree(100)
    turtle.exitonclick()
