import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fibonacci Tree")

tree = turtle.Turtle()
tree.left(90)   # Menghadap ke atas
tree.speed(0)
tree.color("green")

# Fungsi Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Fungsi menggambar Fibonacci Tree
def draw_fib_tree(n, length):
    if n <= 0:
        return
    
    tree.forward(length)
    
    # Cabang kiri
    tree.left(30)
    draw_fib_tree(n-1, fibonacci(n-1) * 2)
    
    # Cabang kanan
    tree.right(60)
    draw_fib_tree(n-2, fibonacci(n-2) * 2)
    
    # Kembali ke posisi sebelumnya
    tree.left(30)
    tree.backward(length)

# Pindahkan posisi awal
tree.penup()
tree.goto(0, -250)
tree.pendown()

# Panggil fungsi (ubah angka untuk kedalaman pohon)
draw_fib_tree(7, 50)

tree.hideturtle()
screen.mainloop()