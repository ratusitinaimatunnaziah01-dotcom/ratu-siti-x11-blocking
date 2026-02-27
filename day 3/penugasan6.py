import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ==============================
# FUNGSI LINGKARAN
# ==============================
def circle(radius, fill, outline, width):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.pensize(width)
    t.color(outline, fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# ==============================
# RING LUAR
# ==============================
circle(250, "white", "black", 6)

# Ring putih bagian dalam (area teks)
circle(210, "white", "black", 3)

# Lingkaran biru tengah
circle(170, "#2c3e75", "black", 3)

# ==============================
# FUNGSI TEKS MELINGKAR
# ==============================
def text_circle(text, radius, start_angle):
    angle = start_angle
    step = 360 / len(text)
    for char in text:
        t.penup()
        t.goto(0,0)
        t.setheading(angle)
        t.forward(radius)
        t.setheading(angle + 90)
        t.write(char, align="center", font=("Arial", 14, "bold"))
        angle -= step

# Teks atas
text_circle("SEKOLAH MENENGAH KEJURUAN", 230, 110)

# Teks bawah (dibalik agar terbaca benar)
def text_circle_bottom(text, radius, start_angle):
    angle = start_angle
    step = 360 / len(text)
    for char in text:
        t.penup()
        t.goto(0,0)
        t.setheading(angle)
        t.forward(radius)
        t.setheading(angle - 90)
        t.write(char, align="center", font=("Arial", 14, "bold"))
        angle -= step

text_circle_bottom("PRESTASI PRIMA", 230, -70)

# ==============================
# BINTANG
# ==============================
t.penup()
t.goto(-200, 0)
t.write("★", align="center", font=("Arial", 24, "bold"))

t.goto(200, 0)
t.write("★", align="center", font=("Arial", 24, "bold"))

# ==============================
# IKON TANGAN (LEBIH MIRIP FOAM FINGER)
# ==============================
t.penup()
t.goto(-40, -60)
t.setheading(90)
t.pendown()
t.pensize(8)
t.color("white", "red")

t.begin_fill()

# Telapak
t.forward(120)
t.right(90)
t.forward(80)
t.right(90)
t.forward(120)
t.right(90)
t.forward(80)

t.end_fill()

# Jari telunjuk
t.penup()
t.goto(-15, 60)
t.setheading(90)
t.pendown()

t.begin_fill()
t.forward(120)
t.right(90)
t.forward(30)
t.right(90)
t.forward(120)
t.right(90)
t.forward(30)
t.end_fill()

turtle.done()