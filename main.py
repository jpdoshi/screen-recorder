import tkinter as tk
from tkinter.ttk import *

import tkinter.filedialog as fd

def open_file_dialog():
    location = fd.asksaveasfilename(title='Choose Destination', defaultextension='mkv', filetypes=[('All Files', '*')])
    text_field.delete(0, 100)
    text_field.insert(0, location)

root = tk.Tk()
root.title('Record Screen')
root.resizable(False, False)

root['padx'] = 12
root['pady'] = 12

frame = Frame(root)
frame.grid(row=0, column=0, columnspan=3, pady=8)

label_file = Label(frame, text='Filename')
label_file.grid(row=0, column=0, padx=4)

text_field = Entry(frame, width=32)
text_field.grid(row=0, column=1, padx=4)

file_dialog = Button(frame, text='Choose', command=open_file_dialog)
file_dialog.grid(row=0, column=2, padx=4)

frame1 = Frame(root)
frame1.grid(row=1, column=0, pady=8, columnspan=3, sticky='w')

label_res = Label(frame1, text='Resolution')
label_res.grid(row=0, column=0, padx=(4, 6))

label_x = Label(frame1, text='x')
label_x.grid(row=0, column=1, padx=(8, 2))

value_x = Entry(frame1, width=8)
value_x.grid(row=0, column=2, padx=2)

label_y = Label(frame1, text='y')
label_y.grid(row=0, column=3, padx=(8, 2))

value_y = Entry(frame1, width=8)
value_y.grid(row=0, column=4, padx=2)

value_x.insert(0, '1920')
value_y.insert(0, '1080')

frame2 = Frame(root)
frame2.grid(row=2, column=1, pady=(32, 8))

start_btn = Button(frame2, text='Start/Stop')
start_btn.grid(row=0, column=0, padx=4)

exit_btn = Button(frame2, text='Exit', command=root.destroy)
exit_btn.grid(row=0, column=1, padx=4)

root.mainloop()