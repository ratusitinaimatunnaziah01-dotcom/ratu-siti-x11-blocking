import tkinter as tk
from tkinter import ttk, messagebox

TARIF_PER_JAM = 2000
data_parkir = []

def hitung_biaya():
    try:
        no_plat = entry_plat.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        if keluar <= masuk:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk!")
            return

        lama = keluar - masuk
        biaya = lama * TARIF_PER_JAM
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))

        data = (no_plat, masuk, keluar, biaya)
        data_parkir.append(data)

        update_table()

    except ValueError:
        messagebox.showerror("Error", "Masukkan waktu dalam angka (jam)!")

def update_table():
    # Hapus isi tabel
    for item in tree_terakhir.get_children():
        tree_terakhir.delete(item)

    for item in tree_terbanyak.get_children():
        tree_terbanyak.delete(item)

    # Urut berdasarkan waktu keluar (terakhir keluar)
    urut_keluar = sorted(data_parkir, key=lambda x: x[2], reverse=True)
    for data in urut_keluar:
        tree_terakhir.insert("", tk.END, values=data)

    # Urut berdasarkan biaya terbesar
    urut_biaya = sorted(data_parkir, key=lambda x: x[3], reverse=True)
    for data in urut_biaya:
        tree_terbanyak.insert("", tk.END, values=data)

# ================= GUI =================
root = tk.Tk()
root.title("Aplikasi Parkir")
root.geometry("900x500")

tk.Label(root, text="Aplikasi Parkir", font=("Arial", 16, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=0, column=1)

tk.Label(frame_input, text="Waktu Masuk (jam)").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Keluar (jam)").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1)

tk.Label(frame_input, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=3, column=1)

tk.Button(frame_input, text="Hitung", command=hitung_biaya).grid(row=4, column=0, columnspan=2, pady=10)

# Label Tarif
tk.Label(root, text="Biaya Per Jam Rp. 2.000", 
         font=("Arial", 18, "bold"), fg="red").pack(pady=10)

# ================= TABLE =================
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("No Plat", "Masuk", "Keluar", "Biaya")

# Tabel Terakhir Keluar
tk.Label(frame_table, text="List Pelanggan Urut Terakhir Keluar",
         fg="blue").grid(row=0, column=0)

tree_terakhir = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)
for col in columns:
    tree_terakhir.heading(col, text=col)
tree_terakhir.grid(row=1, column=0, padx=10)

# Tabel Biaya Terbesar
tk.Label(frame_table, text="List Pelanggan Banyak Bayar",
         fg="blue").grid(row=0, column=1)

tree_terbanyak = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)
for col in columns:
    tree_terbanyak.heading(col, text=col)
tree_terbanyak.grid(row=1, column=1, padx=10)

root.mainloop()