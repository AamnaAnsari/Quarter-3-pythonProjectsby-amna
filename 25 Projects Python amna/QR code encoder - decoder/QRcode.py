import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

qr_img = None  # Global variable for storing QR image

def generate_qr():
    global qr_img
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter text or URL!")
        return

    qr = qrcode.make(data)
    qr.save("qr_code.png")
    qr_img = qr

    img = Image.open("qr_code.png").resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Done ✅", "QR Code Generated Successfully!")

def save_qr():
    global qr_img
    if qr_img is None:
        messagebox.showerror("No QR Found", "Generate a QR code first!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code As")
    if file_path:
        qr_img.save(file_path)
        messagebox.showinfo("Saved", "QR Code saved successfully!")

# GUI setup
root = tk.Tk()
root.title("👑 QR Code Generator - By Queen")
root.geometry("400x530")
root.configure(bg="#fff8f0")

title = tk.Label(root, text="✨ QR Code Generator ✨", font=("Helvetica", 18, "bold"), bg="#fff8f0", fg="#2c3e50")
title.pack(pady=20)

entry = tk.Entry(root, width=40, font=("Helvetica", 12), bd=2, relief="groove")
entry.pack(pady=10)

generate_btn = tk.Button(root, text="Generate QR", font=("Helvetica", 12, "bold"),
                         bg="#6a1b9a", fg="white", padx=10, pady=5, command=generate_qr)
generate_btn.pack(pady=10)

save_btn = tk.Button(root, text="💾 Save QR As", font=("Helvetica", 12, "bold"),
                     bg="#27ae60", fg="white", padx=10, pady=5, command=save_qr)
save_btn.pack(pady=5)

qr_label = tk.Label(root, bg="#fff8f0")
qr_label.pack(pady=20)

footer = tk.Label(root, text="Made with 💜 by The Python Queen", font=("Helvetica", 10), bg="#fff8f0", fg="#7f8c8d")
footer.pack(pady=10)

root.mainloop()
