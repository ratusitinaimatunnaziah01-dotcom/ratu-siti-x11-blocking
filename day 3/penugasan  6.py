import turtle

t = turtle.Turtle()
t.speed(3)

# Warna perisai
t.color("darkblue", "lightblue")

# Gambar perisai
t.begin_fill()
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(80, 40)
t.goto(60, -80)
t.goto(0, -120)
t.goto(-60, -80)
t.goto(-80, 40)
t.goto(0, 100)
t.end_fill()

# Gambar bintang sederhana
t.penup()
t.goto(0, 10)
t.color("yellow")
t.write("★", align="center", font=("Arial", 40, "bold"))

# Teks sekolah
t.penup()
t.goto(0, -150)
t.color("black")
t.write("SMK Prestasi Prima", align="center", font=("Arial", 14, "bold"))

turtle.done()