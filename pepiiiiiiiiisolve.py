   import numpy as np
import tkinter as tk
from tkinter import messagebox

print("(made by pepi)")

def ai_math_assistant():
    def calculate():
        user_input = entry.get()
        if user_input.lower() == 'exit':
            root.quit()
        try:
            result = eval(user_input)
            messagebox.showinfo("Answer", f"The result is: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("pep solve")

    label = tk.Label(root, text="pep solve")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Calculate", command=calculate)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    ai_math_assistant()
#https://cdn.discordapp.com/attachments/1249588372196818944/1260351290551042129/caption-6.gif 