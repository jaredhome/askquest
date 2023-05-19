"""
Utility functions for creating and configuring tkinter widgets.
"""

import tkinter as tk
from itertools import cycle
from config import profile

class AutoHideScrollbar(tk.Scrollbar):
    """
    A scrollbar that hides itself if it's not needed. Only works if you use the grid geometry manager!
    """
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.grid_remove()  # Hide the Scrollbar
        else:
            self.grid()  # Show the Scrollbar
        tk.Scrollbar.set(self, low, high)

    def pack(self, **kw):
        raise tk.TclError("Cannot use pack with this widget.")

    def place(self, **kw):
        raise tk.TclError("Cannot use place with this widget.")


def config_grid(frame, row_weights, col_weights):
    for row, weight in row_weights.items():
        frame.grid_rowconfigure(row, weight=weight)
    for col, weight in col_weights.items():
        frame.grid_columnconfigure(col, weight=weight)

def create_window():
    root = tk.Tk()
    root.geometry('1600x900')
    root.configure(bg=profile.colors.base02)
    return root

def create_frame(parent, row, col, rowspan=1, colspan=1, border=False, bw=1, padx=0, pady=0, bg="white"):
    relief = "solid" if border else "flat"
    frame = tk.Frame(parent, relief=relief, borderwidth=bw, bg=bg)
    frame.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky='nsew', padx=padx, pady=pady)
    return frame

def create_scrollbar(parent):
    scrollbar = AutoHideScrollbar(parent)
    scrollbar.grid(row=0, column=1, sticky='nsew')
    return scrollbar

def create_text_box(parent, yscrollcommand=None, bg="white", fg="black"):
    text_box = tk.Text(parent, yscrollcommand=yscrollcommand, state='disabled', bg=bg, fg=fg,
                       insertbackground=profile.colors.base0, selectbackground=profile.colors.base01, borderwidth=0, highlightthickness=0)
    text_box.grid(row=0, column=0, sticky='nsew')
    return text_box

def create_input_box(parent, height=1, bg="white", fg="black"):
    input_box = tk.Text(parent, height=height, bg=bg, fg=fg, insertbackground=profile.colors.base0,
                        selectbackground=profile.colors.base0, borderwidth=0, highlightthickness=0)
    input_box.grid(row=0, column=0, sticky='nsew')
    return input_box

def create_button(parent, row, col, text="Button", cmd=None, bg="white"):
    button = tk.Button(parent, text=text, command=cmd, bg=bg)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    return button

def create_toggle_button(parent, row, col, options, bg="white"):
    options = cycle(options)
    button = tk.Button(parent, text=next(options), command=lambda: button.config(text=next(options)), bg=bg)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    return button

def create_submit_button(parent, cmd, bg="white"):
    submit_button = tk.Button(parent, text="Submit", command=cmd, bg=bg)
    submit_button.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
    return submit_button

