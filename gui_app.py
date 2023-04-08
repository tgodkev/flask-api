import tkinter as tk
from tkinter import ttk
import requests

def send_request():
    url = url_entry.get()
    method = request_method.get()

    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url)

    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, response.text)

app = tk.Tk()
app.title("HTTP Request Tester")

url_label = ttk.Label(app, text="URL:")
url_label.grid(column=0, row=0)
url_entry = ttk.Entry(app, width=50)
url_entry.grid(column=1, row=0)

request_method = ttk.Combobox(app, values=["GET", "POST"], state="readonly")
request_method.set("GET")
request_method.grid(column=2, row=0)

send_button = ttk.Button(app, text="Send", command=send_request)
send_button.grid(column=3, row=0)

response_text = tk.Text(app, wrap=tk.WORD, width=80, height=25)
response_text.grid(column=0, row=1, columnspan=4)

app.mainloop()
