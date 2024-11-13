import tkinter as tk
from tkinter import ttk


def hasil_prediksi():
    
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.configure(bg="#73EC8B")


judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.pack(pady=10)
root.configure(bg="#73EC8B")


nilai_frame = tk.Frame(root)
nilai_frame.pack(pady=20)


nilai_entries = []
for i in range(10):
    mata_pelajaran_label = tk.Label(nilai_frame, text=f"Nilai Mata Pelajaran {i+1}")
    mata_pelajaran_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    nilai_entry = tk.Entry(nilai_frame)
    nilai_entry.grid(row=i, column=1, padx=5, pady=5)
    nilai_entries.append(nilai_entry)


prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)
root.configure(bg="#73EC8B")


hasil_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil_label.pack(pady=10)

root.mainloop()
