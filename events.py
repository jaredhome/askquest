"""
This module contains event handlers for the tkinter interface.
It provides handlers for "Return" key and "Submit" button click events.
It also includes utility functions to handle user inputs and display the output.
"""

import tkinter as tk
import threading  # import the threading module
from chatbot import main  # import your chatbot main function

# the function to be run in a new thread
def run_main(user_input, dialog_text, progress):
    answer = main(user_input)  # run main function with user input

    # Stop the progress bar and update the dialog text
    # We are using 'after' to ensure these operations happen on the main thread
    dialog_text.after(0, progress.stop)
    dialog_text.after(0, update_dialog_text, dialog_text, user_input, answer)

# function to update the dialog text
def update_dialog_text(dialog_text, user_input, answer):
    dialog_text.configure(state='normal')  # enable editing of the dialog_text
    dialog_text.insert(tk.END, 'User: ' + user_input + '\n')  # add user input to the dialog_text
    dialog_text.insert(tk.END, 'Assistant: ' + answer + '\n')  # add assistant's response to the dialog_text
    dialog_text.configure(state='disabled')  # disable editing
    dialog_text.see(tk.END)  # auto-scroll the scrollbar to the end

def handle_return(event, input_box, dialog_text, progress):
    user_input = input_box.get("1.0", "end-1c")  # get user input from input box
    input_box.delete("1.0", 'end')  # clear input box after getting the input

    # Start the progress bar
    progress.start()

    # Run main function in a new thread
    thread = threading.Thread(target=run_main, args=(user_input, dialog_text, progress))
    thread.start()


