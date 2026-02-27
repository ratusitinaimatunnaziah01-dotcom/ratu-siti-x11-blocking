import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = f"""
    Nama Lengkap : {entry_nama.get()}
    Tanggal Lahir: {entry_tgl.get()}
    Asal Sekolah : {entry_asal.get()}
    NISN         : {entry_nisn.get()}
    Nama Ayah    : {entry_ayah.get()}
    Nama Ibu     : {entry_ibu.get()}
    No HP        : {entry_hp.get()}
    Alamat       : {text_alamat.get("1.0", tk.END).strip()}
    """
    messagebox.showinfo("Data Tersimpan", data)

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_asal.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# ================= WINDOW =================
root = tk.Tk()
root.title("DATA SISWA BARU")
root.geometry("700x650")
root.configure(bg="#d9d9d9")

# ================= HEADER =================
header = tk.Frame(root, bg="#7ec8c9", height=80)
header.pack(fill="x")

tk.Label(header, text="DATA SISWA BARU",
         font=("Arial", 22, "bold"),
         bg="#7ec8c9").pack(pady=20)

# ================= FORM =================
frame = tk.Frame(root, bg="#d9d9d9")
frame.pack(padx=40, pady=20, fill="both", expand=True)

def buat_label_entry(text, row):
    tk.Label(frame, text=text, bg="#d9d9d9",
             font=("Arial", 11)).grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, width=60)
    entry.grid(row=row+1, column=0, pady=5)
    return entry

entry_nama = buat_label_entry("Nama Lengkap", 0)
entry_tgl = buat_label_entry("Tanggal Lahir", 2)
entry_asal = buat_label_entry("Asal Sekolah", 4)
entry_nisn = buat_label_entry("NISN", 6)
entry_ayah = buat_label_entry("Nama Ayah", 8)
entry_ibu = buat_label_entry("Nama Ibu", 10)
entry_hp = buat_label_entry("Nomor Telepon / HP", 12)

# Alamat (Text Area)
tk.Label(frame, text="Alamat", bg="#d9d9d9",
         font=("Arial", 11)).grid(row=14, column=0, sticky="w", pady=5)

text_alamat = tk.Text(frame, width=60, height=5)
text_alamat.grid(row=15, column=0, pady=5)

# ================= FOOTER BUTTON =================
footer = tk.Frame(root, bg="#7ec8c9", height=80)
footer.pack(fill="x", side="bottom")

btn_hapus = tk.Button(footer, text="Hapus", width=12,
                      bg="#c96f4a", fg="white",
                      command=hapus_data)
btn_hapus.pack(side="right", padx=20, pady=20)

btn_simpan = tk.Button(footer, text="Simpan", width=12,
                       bg="#c96f4a", fg="white",
                       command=simpan_data)
btn_simpan.pack(side="right", pady=20)

root.mainloop()