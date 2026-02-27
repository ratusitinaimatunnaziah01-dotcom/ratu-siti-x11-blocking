import turtle

def draw_logo():
    screen = turtle.Screen()
    screen.setup(600, 600)
    t = turtle.Turtle()
    t.speed(0) # Kecepatan maksimal
    t.hideturtle()

    # --- 1. Lingkaran Luar (Hitam) ---
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.pensize(4)
    t.color("black")
    t.circle(250)

    # --- 2. Lingkaran Biru Tua (Background Tengah) ---
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.color("#1a3a6c") # Warna biru tua
    t.begin_fill()
    t.circle(180)
    t.end_fill()

    # --- 3. Gambar Tangan (Sederhana) ---
    # Pergelangan tangan
    t.penup()
    t.goto(-40, -130)
    t.pendown()
    t.color("white", "red")
    t.begin_fill()
    t.pensize(2)
    t.setheading(90)
    t.forward(40)
    
    # Jempol
    t.setheading(150)
    t.circle(-30, 90)
    t.forward(20)
    t.circle(-15, 180)
    t.forward(20)
    
    # Jari Telunjuk (Menunjuk ke atas)
    t.setheading(90)
    t.forward(120)
    t.circle(-20, 180)
    t.forward(120)
    
    # Jari lainnya (disederhanakan menjadi satu lengkungan)
    t.setheading(270)
    t.forward(60)
    t.circle(-40, 150)
    t.goto(40, -130)
    t.goto(-40, -130)
    t.end_fill()

    # --- 4. Lingkaran di Ujung Jari ---
    t.penup()
    t.goto(0, 70)
    t.setheading(0)
    t.pendown()
    t.color("black")
    t.pensize(3)
    t.circle(25)

    # --- 5. Teks Melingkar ---
    def draw_arc_text(text, radius, start_angle, direction):
        t.penup()
        angle_step = direction * (180 / len(text)) # Estimasi penyebaran huruf
        current_angle = start_angle
        
        for char in text:
            # Hitung posisi x, y berdasarkan sudut
            import math
            x = radius * math.cos(math.radians(current_angle))
            y = radius * math.sin(math.radians(current_angle))
            t.goto(x, y - 15) # Penyesuaian offset y
            t.setheading(current_angle + (90 if direction < 0 else -90))
            t.write(char, align="center", font=("Arial", 22, "bold"))
            current_angle += angle_step

    # Teks Atas: SEKOLAH MENENGAH KEJURUAN
    draw_arc_text("SEKOLAH MENENGAH KEJURUAN", 210, 165, -0.85)

    # Teks Bawah: PRESTASI PRIMA
    draw_arc_text("PRESTASI PRIMA", 210, 225, 0.9)

    # --- 6. Bintang Kiri & Kanan ---
    t.color("black")
    for angle in [180, 0]:
        t.penup()
        import math
        x = 215 * math.cos(math.radians(angle))
        y = 215 * math.sin(math.radians(angle))
        t.goto(x, y - 10)
        t.begin_fill()
        for _ in range(5):
            t.forward(20)
            t.right(144)
        t.end_fill()

    screen.mainloop()

if _name_ == "_main_":
    draw_logo()