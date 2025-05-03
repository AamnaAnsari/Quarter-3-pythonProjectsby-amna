import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Rename logic
def rename_files():
    folder_path = folder_entry.get()
    prefix = prefix_entry.get()

    if not folder_path or not prefix:
        messagebox.showerror("Error", "Please select a folder and enter a file prefix.")
        return

    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        for index, file in enumerate(files):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{index+1}{ext}"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

        messagebox.showinfo("Success", "Files have been renamed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Browse for folder
def browse_folder():
    folder = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder)

# ---------------- GUI ----------------
app = tk.Tk()
app.title("Bulk File Renamer")
app.geometry("450x250")
app.configure(bg="#006400")  # Green theme

tk.Label(app, text="Bulk File Renamer", bg="#006400", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

# Folder path
tk.Label(app, text="Select Folder:", bg="#006400", fg="white", font=("Arial", 12)).pack()
folder_entry = tk.Entry(app, width=40, font=("Arial", 10))
folder_entry.pack(pady=5)
tk.Button(app, text="Browse", command=browse_folder, bg="white", fg="#006400").pack()

# Prefix input
tk.Label(app, text="File Name Prefix:", bg="#006400", fg="white", font=("Arial", 12)).pack(pady=(10, 0))
prefix_entry = tk.Entry(app, width=30, font=("Arial", 10))
prefix_entry.pack(pady=5)

# Rename button
tk.Button(app, text="Rename Files", command=rename_files, bg="white", fg="#006400", font=("Arial", 12)).pack(pady=15)

app.mainloop()
