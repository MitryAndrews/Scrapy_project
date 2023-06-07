import tkinter as tk
import tkinter.ttk as ttk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter", foreground="white",  # Set the text color to white
                          background="#34A2FE",  # Set the background color to black)
                          width=30,
                          height=1
                    )
button = tk.Button(text="Click me!", width=10, height=2, bg="blue", fg="yellow")
entry = tk.Entry(fg="yellow", bg="blue", width=20)
frame = tk.Frame()
text_box = tk.Text()
#'wow hello etc'
name = entry.get()
entry.insert(0, 'name')
print(name)
text_box.insert('1.0', name)
# text_box.get('1.0', '1.5')
greeting.pack()
button.pack()
entry.pack()
text_box.pack()
frame.pack()
window.mainloop()

# window.destroy()