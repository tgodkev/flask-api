import tkinter as tk

def on_button_click():
    label.config(text="Hello Tkinter!")

root = tk.Tk()
root.title("Simple Tkinter GUI")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Welcome to Tkinter!")
label.grid(row=0, column=0, columnspan=2)

button = tk.Button(frame, text="Click me!", command=on_button_click)
button.grid(row=1, column=0)

quit_button = tk.Button(frame, text="Quit", command=root.quit)
quit_button.grid(row=1, column=1)

root.mainloop()
