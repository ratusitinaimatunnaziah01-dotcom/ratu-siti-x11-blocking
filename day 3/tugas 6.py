import turtle

# Setup layar
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
t.hideturtle()

# =========================
# FUNGSI MEMBUAT PERISAI
# =========================
def perisai():
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()
    t.color("#0B3D91")  # biru tua
    t.begin_fill()

    t.forward(300)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(300)
    t.right(45)
    t.forward(127)
    t.right(90)
    t.forward(127)

    t.end_fill()

# =========================
# LINGKARAN TENGAH
# =========================
def lingkaran():
    t.penup()
    t.goto(0, -40)
    t.setheading(0)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(80)
    t.end_fill()

# =========================
# BINTANG
# =========================
def bintang():
    t.penup()
    t.goto(0, 40)
    t.setheading(90)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()

# =========================
# TEKS
# =========================
def teks():
    t.penup()
    t.goto(0, -20)
    t.color("white")
    t.write("SMK", align="center", font=("Arial", 28, "bold"))

    t.goto(0, -80)
    t.write("PRESTASI PRIMA", align="center", font=("Arial", 14, "bold"))

# =========================
# PANGGIL SEMUA FUNGSI
# =========================
perisai()
lingkaran()
bintang()
teks()

turtle.done()