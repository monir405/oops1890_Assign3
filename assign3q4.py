import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
def calculate():
    try:
        side_a = int(side_a_entry.get())
        side_b = int(side_b_entry.get())
        if side_a <= 0 or side_b <= 0:
            messagebox.showerror("Please enter positive integers for sides A and B.")
            return
        side_c = round(math.sqrt(side_a**2 + side_b**2), 3)
        side_c_var.set(side_c)
    except ValueError:
        messagebox.showerror("Please enter valid integers for sides A and B.")

root = tk.Tk()
root.title("Right Triangle Calculator")
root.geometry("500x250")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

side_a_var = tk.StringVar()
side_b_var = tk.StringVar()
side_c_var = tk.StringVar()

input_frame = ttk.Frame(frame)
input_frame.pack(pady=10)


side_a_label = ttk.Label(input_frame, text="Side A:")
side_a_label.grid(row=0, column=0, padx=5, sticky=tk.E)
side_a_entry = ttk.Entry(input_frame, width=10, textvariable=side_a_var)
side_a_entry.grid(row=0, column=1, sticky=tk.W)


side_b_label = ttk.Label(input_frame, text="Side B:")
side_b_label.grid(row=1, column=0, padx=5, sticky=tk.E)
side_b_entry = ttk.Entry(input_frame, width=10, textvariable=side_b_var)
side_b_entry.grid(row=1, column=1, sticky=tk.W)


side_c_label = ttk.Label(input_frame, text="Side C:")
side_c_label.grid(row=2, column=0, padx=5, sticky=tk.E)
side_c_entry = ttk.Entry(input_frame, width=10, textvariable=side_c_var, state="readonly")
side_c_entry.grid(row=2, column=1, sticky=tk.W)


button_frame = ttk.Frame(frame)
button_frame.pack()


calculate_button = ttk.Button(button_frame, text="Calculate", command=calculate)
calculate_button.grid(row=0, column=0, padx=5)


exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.grid(row=0, column=1, padx=5)

frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

root.mainloop()
