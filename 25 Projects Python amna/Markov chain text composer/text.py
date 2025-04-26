import tkinter as tk
from tkinter import filedialog, messagebox
import random

class MarkovChainTextComposer:
    def __init__(self, root):
        self.root = root
        self.root.title("Markov Chain Text Composer")

        self.markov_chain = {}
        self.input_text = ""

        # GUI Components
        self.label = tk.Label(root, text="Markov Chain Text Generator", font=("Arial", 18))
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(root, width=400, height=200, bg="lightgray")
        self.canvas.pack(pady=10)

        self.text_box = tk.Text(root, height=6, width=50)
        self.text_box.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        upload_btn = tk.Button(btn_frame, text="Upload Text File", command=self.upload_text_file, width=15, bg="lightgreen")
        upload_btn.grid(row=0, column=0, padx=10)

        generate_btn = tk.Button(btn_frame, text="Generate Text", command=self.generate_text, width=15)
        generate_btn.grid(row=0, column=1, padx=10)

        clear_btn = tk.Button(btn_frame, text="Clear Text", command=self.clear_text, width=15, bg="lightcoral")
        clear_btn.grid(row=1, column=0, padx=10, pady=10)

    def upload_text_file(self):
        # Let the user upload a text file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.input_text = file.read()
                self.create_markov_chain()
                messagebox.showinfo("Success", "Text loaded and Markov Chain generated!")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading file: {e}")

    def create_markov_chain(self):
        # markov chain create hogi based on user input 
        words = self.input_text.split()
        self.markov_chain = {}

        for i in range(len(words) - 1):
            if words[i] not in self.markov_chain:
                self.markov_chain[words[i]] = []
            self.markov_chain[words[i]].append(words[i + 1])

    def generate_text(self):
        # Generate text based on the Markov Chain
        if not self.markov_chain:
            messagebox.showwarning("No Text", "Please upload a text file first.")
            return

        current_word = random.choice(list(self.markov_chain.keys()))
        generated_text = [current_word]

        for _ in range(100):  # Generate up to 100 words
            if current_word not in self.markov_chain:
                break
            next_word = random.choice(self.markov_chain[current_word])
            generated_text.append(next_word)
            current_word = next_word

        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, ' '.join(generated_text))

    def clear_text(self):
        # Clear the text box
        self.text_box.delete(1.0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = MarkovChainTextComposer(root)
    root.mainloop()
