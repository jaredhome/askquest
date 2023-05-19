"""
main.py

This module sets up the graphical user interface of the application using tkinter.
It creates the main window, frames, text boxes, scrollbar and the submit button.
It also binds the events to the user input and submit button.
"""

import tkinter as tk
from tkinter import ttk
from itertools import cycle
from gui import *
import events
from config import profile

# Initialize options for GPT versions
gpt_versions = cycle(['GPT-3.5', 'GPT-4'])

# Create root window and configure its grid
root = create_window()
config_grid(root, row_weights={0: 1, 1: 99}, col_weights={0: 2, 1: 8})

# Create top_frame and configure its grid
top_frame = create_frame(root, 0, 0, colspan=2, bg=profile.colors.base02)
config_grid(top_frame, row_weights={0: 1}, col_weights={0: 2, 1: 7, 2: 1})

# Add widgets to top_frame
new_chat_button = create_button(top_frame, 0, 0, text="+ New Chat")
gpt_toggle_button = create_toggle_button(top_frame, 0, 1, options=gpt_versions)
preferences_button = create_button(top_frame, 0, 2, text="Preferences")

# Create left_frame and configure its grid
left_frame = create_frame(root, 1, 0, rowspan=1, border=False, padx=(15, 0), pady=15, bg=profile.colors.base02)
config_grid(left_frame, row_weights={0: 1}, col_weights={0: 1})

# Create right_frame and configure its grid
right_frame = create_frame(root, 1, 1, rowspan=1, border=False, padx=(15,15), pady=15, bg=profile.colors.base02)
config_grid(right_frame, row_weights={0: 1, 1: 1}, col_weights={0: 8})

# Create dialog_frame, progress_frame, and input_frame, and configure their grids
dialog_frame = create_frame(right_frame, 0, 0, bg=profile.colors.base03)
config_grid(dialog_frame, row_weights={0: 1}, col_weights={0: 1})

progress_frame = create_frame(right_frame, 1, 0, bg=profile.colors.base03)
config_grid(progress_frame, row_weights={0: 1}, col_weights={0: 1})

input_frame = create_frame(right_frame, 2, 0, bg=profile.colors.base03)
config_grid(input_frame, row_weights={0: 1}, col_weights={0: 1})

# Add Progress Bar Widget to progress_frame
progress = ttk.Progressbar(progress_frame, length=100, mode='indeterminate')
progress.grid(row=0, column=0, sticky='ew', padx=15, pady=15)

# Create a style object
style = ttk.Style()

# Configure the 'TProgressbar' layout to show only the moving bar (by matching the background with the trough color)
style.configure('TProgressbar', background=profile.colors.base03, troughcolor=profile.colors.base03)

# Then apply the style to the progress bar
progress = ttk.Progressbar(progress_frame, length=100, mode='indeterminate', style='TProgressbar')
progress.grid(row=0, column=0, sticky='ew', padx=15, pady=15)


# Add Scrollbar Widget to dialog_frame
scrollbar = create_scrollbar(dialog_frame)

# Add Text Box Widget to dialog_frame
dialog_text = create_text_box(dialog_frame, yscrollcommand=scrollbar.set, bg=profile.colors.base02, fg=profile.colors.base00)

# Add Text Box Widget to input_frame
input_box = create_input_box(input_frame, height=1)
input_box.config(bg=profile.colors.base03, fg=profile.colors.base00)

# Bind Return key to handle_return event
input_box.bind("<Return>", lambda event: events.handle_return(event, input_box, dialog_text, progress))

# Execute the main loop to run the program
root.mainloop()

