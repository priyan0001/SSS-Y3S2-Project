import tkinter as tk
from tkinter import filedialog
from subprocess import Popen, PIPE, STDOUT
import threading

# global variable to store the running process
process = None

# functions for handling file selection and scan execution
def select_file():
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def run_xss_scan():
    filename = entry.get()
    run_scan(["python", "xss_test.py", filename])

def run_sqli_scan():
    filename = entry.get()
    run_scan(["python", "sqli_test.py", filename])

def run_scan(command):
    global process
    output.config(state='normal')  # Enable the text widget
    process = Popen(command, stdout=PIPE, stderr=STDOUT)

    def stream_output():
        for line in iter(process.stdout.readline, b''):
            output.insert(tk.END, line.decode())
            output.see(tk.END)
            root.update()

    threading.Thread(target=stream_output).start()

# close the application
def close_app():
    global process
    if process:
        process.terminate()  # stop the running process
    root.destroy()

# create the GUI
root = tk.Tk()

root.title("TEST!!!")
root.geometry('1000x600')
root.configure(bg='light grey')  # set background color

# Banner
banner = tk.Label(root, text="Python Codebase Vulnerability Detection", font=('Comic Sans MS', 32, 'bold'), fg="green", bg='light grey')
banner.pack()

banner_sss = tk.Label(root, text="S.S.S", font=('Comic Sans MS', 22, 'bold'), fg="green", bg='light grey')
banner_sss.pack()

# File selection row
file_select_frame = tk.Frame(root, bg='light grey')
file_select_frame.pack(pady=10, fill=tk.X)

label = tk.Label(file_select_frame, text="Python file:", font=('Comic Sans MS', 16), bg='light grey')
label.pack(side=tk.LEFT, padx=10)

entry = tk.Entry(file_select_frame, font=('Helvetica', 16))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

select_button = tk.Button(file_select_frame, text="Select File", command=select_file, font=('Courier', 16, 'bold'), bg='light grey', fg='black', relief='raised', bd=5)
select_button.pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(root, bg='light grey')
button_frame.pack(pady=10)

xss_button = tk.Button(button_frame, text="Scan for XSS", command=run_xss_scan, font=('Courier', 16, 'bold'), bg='light grey', fg='black', relief='raised', bd=5)
xss_button.pack(side=tk.LEFT, padx=10)

sqli_button = tk.Button(button_frame, text="Scan for SQLi", command=run_sqli_scan, font=('Courier', 16, 'bold'), bg='light grey', fg='black', relief='raised', bd=5)
sqli_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(root, text="Exit", command=close_app, font=('Courier', 16, 'bold'), bg='red', fg='black', relief='raised', bd=5)
exit_button.pack(pady=10)

output = tk.Text(root, state='disabled', bg='grey', fg='black')
output.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()
