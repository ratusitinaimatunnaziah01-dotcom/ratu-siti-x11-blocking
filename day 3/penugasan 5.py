import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.title("Night Landscape")

art = turtle.Turtle()
art.speed(0)
art.hideturtle()

# -----------------------
# Fungsi gambar lingkaran
# -----------------------
def draw_circle(color, x, y, radius):
    art.penup()
    art.goto(x, y - radius)
    art.pendown()
    art.color(color)
    art.begin_fill()
    art.circle(radius)
    art.end_fill()

# -----------------------
# Gambar bulan
# -----------------------
draw_circle("light yellow", 150, 150, 50)

# -----------------------
# Gambar bintang acak
# -----------------------
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-50, 300)
    draw_circle("white", x, y, 2)

# -----------------------
# Gambar tanah
# -----------------------
art.penup()
art.goto(-400, -100)
art.pendown()
art.color("dark green")
art.begin_fill()
for _ in range(2):
    art.forward(800)
    art.right(90)
    art.forward(300)
    art.right(90)
art.end_fill()

# -----------------------
# Fungsi gambar pohon
# -----------------------
def draw_tree(x, y):
    art.penup()
    art.goto(x, y)
    art.pendown()
    
    # Batang
    art.color("saddlebrown")
    art.begin_fill()
    for _ in range(2):
        art.forward(20)
        art.left(90)
        art.forward(60)
        art.left(90)
    art.end_fill()
    
    # Daun
    art.penup()
    art.goto(x - 40, y + 60)
    art.pendown()
    art.color("forest green")
    art.begin_fill()
    art.circle(50)
    art.end_fill()

# Gambar beberapa pohon
draw_tree(-200, -100)
draw_tree(-50, -100)
draw_tree(100, -100)

# Selesai
screen.mainloop()