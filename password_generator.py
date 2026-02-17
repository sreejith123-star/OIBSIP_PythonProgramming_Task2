import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- WINDOW SETUP ---------------- #

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("450x550")
root.resizable(False, False)

# ---------------- FUNCTIONS ---------------- #

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak", "red"
    elif score <= 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6")
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        if exclude_similar_var.get():
            for ch in "O0l1I":
                characters = characters.replace(ch, "")

        password = "".join(random.choice(characters) for _ in range(length))

        password_output.delete(0, tk.END)
        password_output.insert(0, password)

        strength, color = check_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg=color)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


def copy_to_clipboard():
    password = password_output.get()

    if password == "":
        messagebox.showwarning("Warning", "No password to copy")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- UI DESIGN ---------------- #

title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()
exclude_similar_var = tk.IntVar()

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Symbols (!@#)", variable=symbols_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Exclude Similar Characters (O,0,l,1,I)", variable=exclude_similar_var).pack(anchor="w", padx=40)

password_output = tk.Entry(root, width=35, font=("Arial", 12))
password_output.pack(pady=20)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
strength_label.pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

# ---------------- RUN ---------------- #

root.mainloop()