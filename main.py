import tkinter as tk
from tkinter.ttk import *

import tkinter.filedialog as fd
from tkinter.messagebox import showinfo

import pyautogui
import numpy as np
import cv2

import threading
import keyboard

def start_recording():
    out_file = file_entry.get()
    dimensions = (int(res_x.get()), int(res_y.get()))

    offset = (int(offset_x.get()), int(offset_y.get()))
    divisor = 2.5
    fps = float(fps_spin.get()) / divisor

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_file, fourcc, fps, dimensions)

    root.iconify()

    while True:
        img = pyautogui.screenshot(region=(offset[0], offset[1], dimensions[0], dimensions[1]))
        img = np.array(img)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out.write(img)

        if keyboard.is_pressed('f10'):
            break

    cv2.destroyAllWindows()
    out.release()

    showinfo(title='Success', message='File Saved Successfuly!')

def open_file_dialog():
    location = fd.asksaveasfilename(title='Choose Destination', initialfile='Output', defaultextension='mp4', filetypes=[('All Files', '*')])
    file_entry.delete(0, 100)
    file_entry.insert(0, location)

root = tk.Tk()
root.title('Record Screen')
root.resizable(False, False)

frame = Frame(root)
frame.pack(padx=8, pady=8)

file_lbl = Label(frame, text='Filename')
file_lbl.grid(row=0, column=0, padx=4, pady=4, sticky='w')

file_entry = Entry(frame, width=32)
file_entry.grid(row=0, column=1, pady=4)

file_dialog = Button(frame, text='...', width=4, command=open_file_dialog)
file_dialog.grid(row=0, column=2, padx=4, pady=4)

label_res = Label(frame, text='Dimension')
label_res.grid(row=1, column=0, padx=4, pady=4, sticky='w')

res_frame = Frame(frame)
res_frame.grid(row=1, column=1, pady=4, sticky='w')

res_lbl_x = Label(res_frame, text='X:')
res_lbl_x.grid(row=0, column=0, padx=4)

res_x = Entry(res_frame, width=8)
res_x.grid(row=0, column=1, padx=(0, 6))

res_lbl_y = Label(res_frame, text='Y:')
res_lbl_y.grid(row=0, column=2, padx=4)

res_y = Entry(res_frame, width=8)
res_y.grid(row=0, column=3, padx=(0, 6))

res_x.insert(0, '1920')
res_y.insert(0, '1080')

offset_lbl = Label(frame, text='Offset')
offset_lbl.grid(row=2, column=0, padx=4, pady=4, sticky='w')

offset_frame = Frame(frame)
offset_frame.grid(row=2, column=1, pady=4, sticky='w')

offset_lbl_x = Label(offset_frame, text='X:')
offset_lbl_x.grid(row=0, column=0, padx=4)

offset_x = Entry(offset_frame, width=8)
offset_x.grid(row=0, column=1, padx=(0, 8))

offset_lbl_y = Label(offset_frame, text='Y:')
offset_lbl_y.grid(row=0, column=2, padx=4)

offset_y = Entry(offset_frame, width=8)
offset_y.grid(row=0, column=3, padx=(0, 8))

offset_x.insert(0, '0')
offset_y.insert(0, '0')

fps_lbl = Label(frame, text='FPS')
fps_lbl.grid(row=3, column=0, padx=4, pady=4, sticky='w')

fps_spin = Spinbox(frame, width=4)
fps_spin.grid(row=3, column=1, padx=4, pady=4, sticky='w')
fps_spin.set(30)

action_btn_frame = Frame(frame)
action_btn_frame.grid(row=4, column=0, columnspan=3, pady=(24, 4))

is_recording = False
start_btn = Button(action_btn_frame, text='Start', command=threading.Thread(target=start_recording).start)
start_btn.grid(row=0, column=0, padx=2)

exit_btn = Button(action_btn_frame, text='Exit', command=root.destroy)
exit_btn.grid(row=0, column=1, padx=2)

hint_lbl = Label(frame, text='Press F10 to Stop recording', foreground='#d32f2f')
hint_lbl.grid(row=6, column=0, columnspan=3, padx=4)

root.mainloop()
