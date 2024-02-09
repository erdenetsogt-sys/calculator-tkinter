import tkinter as tk

class Calculator:

    def __init__(self, text_result):
        self.calculation = ""
        self.text_result = text_result

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.remove_and_replace()
    
    def evaluate_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
            self.remove_and_replace()
        except:
            self.clear_field()
            self.text_result.insert(1.0, "ERROR")

    def clear_field(self):
        self.calculation = ""
        self.remove_and_replace()

    def remove_and_replace(self):
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)

root = tk.Tk()
root.title("calculator")
root.geometry("235x320")
root.configure(bg="#505050")

text_result = tk.Text(root, height=2.3, width=16, font=("Arial", 24), bg="#1C1C1C", fg="white")
text_result.grid(columnspan=5, padx=0, pady=0)  # Set padx and pady to 0
calculus = Calculator(text_result)

# Buttons
btn_1 = tk.Button(root, text="1", command=lambda: calculus.add_to_calculation(1), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_1.grid(row=2, column=1, padx=0, pady=0)
btn_1.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_2 = tk.Button(root, text="2", command=lambda: calculus.add_to_calculation(2), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_2.grid(row=2, column=2, padx=0, pady=0)
btn_2.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_3 = tk.Button(root, text="3", command=lambda: calculus.add_to_calculation(3), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_3.grid(row=2, column=3, padx=0, pady=0)
btn_3.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_4 = tk.Button(root, text="4", command=lambda: calculus.add_to_calculation(4), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_4.grid(row=3, column=1, padx=0, pady=0)
btn_4.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_5 = tk.Button(root, text="5", command=lambda: calculus.add_to_calculation(5), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_5.grid(row=3, column=2, padx=0, pady=0)
btn_5.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_6 = tk.Button(root, text="6", command=lambda: calculus.add_to_calculation(6), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_6.grid(row=3, column=3, padx=0, pady=0)
btn_6.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_7 = tk.Button(root, text="7", command=lambda: calculus.add_to_calculation(7), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_7.grid(row=4, column=1, padx=0, pady=0)
btn_7.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_8 = tk.Button(root, text="8", command=lambda: calculus.add_to_calculation(8), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_8.grid(row=4, column=2, padx=0, pady=0)
btn_8.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_9 = tk.Button(root, text="9", command=lambda: calculus.add_to_calculation(9), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_9.grid(row=4, column=3, padx=0, pady=0)
btn_9.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_0 = tk.Button(root, text="0", command=lambda: calculus.add_to_calculation(0), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_0.grid(row=5, column=2, padx=0, pady=0)
btn_0.configure(highlightbackground="#505050", takefocus=False, padx=0, pady=0)

btn_plus = tk.Button(root, text="+", command=lambda: calculus.add_to_calculation("+"), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_plus.grid(row=2, column=4, padx=0, pady=0)
btn_plus.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_minus = tk.Button(root, text="-", command=lambda: calculus.add_to_calculation("-"), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_minus.grid(row=3, column=4, padx=0, pady=0)
btn_minus.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_mul = tk.Button(root, text="*", command=lambda: calculus.add_to_calculation("*"), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_mul.grid(row=4, column=4, padx=0, pady=0)
btn_mul.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_div = tk.Button(root, text="/", command=lambda: calculus.add_to_calculation("/"), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_div.grid(row=5, column=4, padx=0, pady=0)
btn_div.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_open = tk.Button(root, text="(", command=lambda: calculus.add_to_calculation("("), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_open.grid(row=5, column=1, padx=0, pady=0)
btn_open.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_close = tk.Button(root, text=")", command=lambda: calculus.add_to_calculation(")"), width=6, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_close.grid(row=5, column=3, padx=0, pady=0)
btn_close.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_equal = tk.Button(root, text="=", command=calculus.evaluate_calculation, width=13, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_equal.grid(row=6, column=3, padx=0, pady=0, columnspan=2)
btn_equal.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

btn_clear = tk.Button(root, text="AC", command=calculus.clear_field, width=13, height=3, font=("Arial", 14), fg="white", relief=tk.FLAT)
btn_clear.grid(row=6, column=1, padx=0, pady=0, columnspan=2)
btn_clear.configure(highlightbackground="#FF9500", takefocus=False, padx=0, pady=0)

root.mainloop()
