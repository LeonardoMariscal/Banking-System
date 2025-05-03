import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")
root.title("BankingSystemGUI")
root.configure(bg="#eaeaea")

# TITLE
title_label = tk.Label(root, text="Prime Bank", font=('Arial', 60), bg="#eaeaea")
title_label.grid(row=0, column=0, columnspan=2, pady=(50, 40))

# Username label
username_label = tk.Label(root, text="Username:", font=('Arial', 20), bg="#eaeaea")
username_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

username_entry = tk.Entry(root, font=('Arial', 20), width=30)
username_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Password
password_label = tk.Label(root, text="Password:", font=('Arial', 20), bg="#eaeaea")
password_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

password_entry = tk.Entry(root, font=('Arial', 20), width=30, show="*")
password_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

# Button
login_button = tk.Button(root, text="Enter", font=('Arial', 18), width=10)
login_button.grid(row=3, column=0, columnspan=2, pady=40)

root.mainloop()
