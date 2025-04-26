import tkinter as tk
from tkinter import messagebox
import time

# Binary Search Function (Returns steps)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = []

    while low <= high:
        mid = (low + high) // 2
        steps.append(mid)

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps

# bars ko draw krta hai ye function 
def draw_bars(arr, highlight_indices=[]):
    canvas.delete("all")
    c_width = 400
    c_height = 200
    bar_width = c_width // len(arr)
    max_height = max(arr)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = c_height - (val / max_height) * (c_height - 20)
        x1 = (i + 1) * bar_width
        y1 = c_height

        color = "skyblue"
        if i in highlight_indices:
            color = "orange"

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text((x0+x1)//2, y0-10, text=str(val), font=("Helvetica", 10))

    window.update()

# Function to perform search and visualize
def perform_search():
    try:
        array = list(map(int, entry_array.get().split()))
        target = int(entry_target.get())

        array.sort()
        draw_bars(array)

        index, steps = binary_search(array, target)

        for mid in steps:
            draw_bars(array, highlight_indices=[mid])
            time.sleep(0.8)

        if index != -1:
            messagebox.showinfo("Result", f"Element {target} found at index {index}!")
        else:
            messagebox.showinfo("Result", f"Element {target} not found!")

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers only.")

# Create GUI Window
window = tk.Tk()
window.title("Binary Search Visualizer with Graphs 👑")
window.geometry("450x450")
window.resizable(False, False)

# Labels
label_array = tk.Label(window, text="Enter numbers (space separated):", font=("Helvetica", 12))
label_array.pack(pady=10)

entry_array = tk.Entry(window, width=40)
entry_array.pack(pady=5)

label_target = tk.Label(window, text="Enter number to search:", font=("Helvetica", 12))
label_target.pack(pady=10)

entry_target = tk.Entry(window, width=20)
entry_target.pack(pady=5)

# Search Button
search_button = tk.Button(window, text="Search 🔍", font=("Helvetica", 12), command=perform_search)
search_button.pack(pady=20)

# Canvas for drawing bars
canvas = tk.Canvas(window, width=400, height=200, bg="white")
canvas.pack(pady=10)

# Start the GUI loop
window.mainloop()
