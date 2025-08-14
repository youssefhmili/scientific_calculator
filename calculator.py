import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self.root, bd=0, highlightbackground="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(
            input_frame,
            font=('arial', 18, 'bold'),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=tk.RIGHT
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        # Buttons
        btns_frame = tk.Frame(self.root, bg="lightgrey")
        btns_frame.pack()

        scientific_buttons = [
            ("sin", "math.sin("), ("cos", "math.cos("), ("tan", "math.tan("), ("log", "math.log10("),
            ("ln", "math.log("), ("√", "math.sqrt("), ("^", "**"), ("π", "math.pi"),
            ("e", "math.e"), ("(", "("), (")", ")"), ("C", "CLEAR"),
        ]
        basic_buttons = [
            ("7", "7"), ("8", "8"), ("9", "9"), ("/", "/"),
            ("4", "4"), ("5", "5"), ("6", "6"), ("*", "*"),
            ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
            ("0", "0"), (".", "."), ("=", "EQUAL"), ("+", "+"),
        ]

        # Create scientific buttons
        row, col = 0, 0
        for (text, value) in scientific_buttons:
            self.add_button(btns_frame, text, row, col, value)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create basic buttons
        for (text, value) in basic_buttons:
            self.add_button(btns_frame, text, row, col, value, bg="#f5f5f5" if text.isdigit() else "#ddd")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_button(self, frame, text, row, col, value, bg="white", fg="black"):
        btn = tk.Button(
            frame, text=text, fg=fg, width=10, height=3, bd=0, bg=bg,
            cursor="hand2", command=lambda: self.press(value)
        )
        btn.grid(row=row, column=col, padx=1, pady=1)

    def press(self, value):
        if value == "CLEAR":
            self.expression = ""
            self.input_text.set("")
        elif value == "EQUAL":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
