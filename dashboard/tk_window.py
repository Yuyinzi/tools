import tkinter as tk
import requests
from tkinter import scrolledtext


def convert_base64():
    url = url_form.get()
    data = {"url": url}
    rsp = requests.post("http://localhost:5000/base64", json=data)
    res = rsp.json().get("data")
    src.insert(tk.END, res)


window = tk.Tk()
window.title("工具包")
window.geometry("1000x500")
s = tk.Scrollbar(window)
s.pack(side=tk.RIGHT, fill=tk.Y)
s1 = tk.Scrollbar(window, orient=tk.HORIZONTAL)
s1.pack(side=tk.BOTTOM, fill=tk.X)
window.resizable(width=True, height=True)
my_label = tk.Label(window, text="littlemay", fg="blue", font=("Arial", 20, "bold"), width=30, height=2)
my_label.pack()

url_form = tk.Entry(window, font=('Arial', 14))
url_form.pack()

convert_btn = tk.Button(window, text="转换", bg="green", font=("Arial", 12, "bold"), width=15, height=2,
                        command=convert_base64)
convert_btn.pack()

information = tk.Label(window, text="编码结果", bg="gray", font=("Arial", 12, "bold"), width=30, height=2)
information.pack()

# result = tk.Text(window, font=("Arial", 12), yscrollcommand=s.set, xscrollcommand=s1.set)
# result.pack()
src = scrolledtext.ScrolledText(window, width=70, height=13)
src.place(x=200, y=200)

window.mainloop()
