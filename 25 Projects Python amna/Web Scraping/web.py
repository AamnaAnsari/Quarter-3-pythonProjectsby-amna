import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

# function to show profile image
def fetch_profile_image():
    url = url_entry.get()
    if "github.com" not in url:
        messagebox.showerror("Invalid URL", "Please enter a valid GitHub profile URL.")
        return

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_img = soup.find('img', {'class': 'avatar-user'})

        if profile_img:
            img_url = profile_img['src']
            result_label.config(text=f"Image URL:\n{img_url}", fg='white')

            # Fetch and display image
            img_data = requests.get(img_url).content
            img = Image.open(BytesIO(img_data)).resize((150, 150))
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk  # refernce rkhta hai
        else:
            result_label.config(text="Profile image not found.", fg='red')
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ---------------- GUI Setup ----------------
app = tk.Tk()
app.title("GitHub Profile Scraper")
app.geometry("400x500")
app.configure(bg='#006400')  # Dark green

# Heading
heading = tk.Label(app, text="GitHub Profile Image Finder", bg='#006400', fg='white', font=('Arial', 16, 'bold'))
heading.pack(pady=10)

# URL Input
url_entry = tk.Entry(app, width=40, font=('Arial', 12))
url_entry.pack(pady=10)

# Button
search_btn = tk.Button(app, text="Fetch Profile Image", bg='white', fg='#006400', font=('Arial', 12), command=fetch_profile_image)
search_btn.pack(pady=10)

# Result label
result_label = tk.Label(app, text="", bg='#006400', fg='white', font=('Arial', 10), wraplength=350, justify='center')
result_label.pack(pady=10)

# Image display label
image_label = tk.Label(app, bg='#006400')
image_label.pack(pady=10)

# Run the GUI
app.mainloop()
