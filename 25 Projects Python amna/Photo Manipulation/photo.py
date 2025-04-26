import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageFilter, ImageTk

class PhotoEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Manipulation App - Tkinter + PIL")
        self.image = None

        self.label = tk.Label(root, text="Upload an image to start", font=("Arial", 16))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=400, bg='gray')
        self.canvas.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        upload_btn = tk.Button(btn_frame, text="Upload Image", command=self.upload_image, width=15, bg="lightgreen")
        upload_btn.grid(row=0, column=0, padx=10)

        contrast_btn = tk.Button(btn_frame, text="Increase Contrast", command=self.increase_contrast, width=15)
        contrast_btn.grid(row=0, column=1, padx=10)

        brightness_btn = tk.Button(btn_frame, text="Increase Brightness", command=self.increase_brightness, width=15)
        brightness_btn.grid(row=0, column=2, padx=10)

        blur_btn = tk.Button(btn_frame, text="Apply Blur", command=self.apply_blur, width=15, bg="lightblue")
        blur_btn.grid(row=1, column=0, padx=10, pady=10)

        save_btn = tk.Button(btn_frame, text="Save Image", command=self.save_image, width=15, bg="lightcoral")
        save_btn.grid(row=1, column=1, padx=10, pady=10)

        reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_image, width=15)
        reset_btn.grid(row=1, column=2, padx=10, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.image = self.original_image.copy()
            self.show_image()

    def show_image(self):
        if self.image:
            self.tk_image = ImageTk.PhotoImage(self.image.resize((400, 400)))
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def increase_contrast(self):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(1.5)
            self.show_image()

    def increase_brightness(self):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(1.3)
            self.show_image()

    def apply_blur(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.show_image()

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.image.save(save_path)
                messagebox.showinfo("Image Saved", "Your image has been saved successfully!")

    def reset_image(self):
        if hasattr(self, 'original_image'):
            self.image = self.original_image.copy()
            self.show_image()

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditor(root)
    root.mainloop()
