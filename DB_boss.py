# -*- coding: utf-8 -*-
"""
DB Boss (DB)
Tim Veenstra
"""

import tkinter
import sqlite3
from tkinter.filedialog import askopenfilename

""" ------------------------- SELECTING THE DB ---------------------------- """

current_db = "fiets"


def select_db_name(current_db_label):
    global current_db
    current_db = askopenfilename(filetype=[("*.db", "db")])
    if current_db is "" or current_db is None:
        return 0
    current_db_label = tkinter.Label(window, bg="#FFFFFF",
                                     pady = 4,
                                     text="Current database is:\n"+current_db
                                     ).grid(
                                                     row=3,
                                                     column=1,
                                                     columnspan=3)
    return 1

""" ------------------------- HANDELING THE SQL ----------------------------"""


def execute_query(input_textbox):
    text = input_textbox.get("1.0", "end-1c")
    print(text)

""" ------------------------- CREATING A WINDOW ----------------------------"""


def create_start_window(window):

    """ Title of the application """
    header = tkinter.Label(window, text="DB Boss",  font=("", "24", "bold"),
                           padx=500, bg="#FFFFFF", pady=10).grid(
                                                   row=0,
                                                   column=1,
                                                   columnspan=8
                                                   )

    """ Subheader of the database selection """
    select_db_header = tkinter.Label(window, text="Select a database",
                                     bg="#FFFFFF",
                                     pady=10,
                                     font=("", "14", "bold")).grid(row=2,
                                                                   column=1,
                                                                   columnspan=3
                                                                   )

    """ Section db selection """
    current_db_label = tkinter.Label(window, bg="#FFFFFF",
                                     pady=4,
                                     text="No database has been opened\n")\
                                                            .grid(
                                                                 row=3,
                                                                 column=1,
                                                                 columnspan=3
                                                                 )
    select_db_button = tkinter.Button(window, text="Open db",  width=40,
                                      pady=8,
                                      command=lambda: \
                                              select_db_name(current_db_label))
    select_db_button.grid(row=4, column=1, columnspan=3)
    
    """Horizontal line between sections """
    seperator_label = tkinter.Label(window, bg="white").grid(row=5)
    seperator = tkinter.Frame(window, pady=10, width=400, height=1, bg="black")
    seperator.grid(row=6, column=0, columnspan=4)
    
    """ Subheader of the sql section """
    query_header = tkinter.Label(window, text="Execute your sql",
                                     bg="#FFFFFF",
                                     pady=10,
                                     font=("", "14", "bold")).grid(row=7,
                                                                   column=1,
                                                                   columnspan=3
                                                                   )
    
    """ SQL section """
    query_input= tkinter.Text(window, width=50, height=20, bg="#FFFFF0")
    query_input.grid(row=8, column=1, columnspan=3)
    seperator_label_2 = tkinter.Label(window, bg="white").grid(row=9)
    submit_query = tkinter.Button(window, text="Execute", width=57, pady=8,
                                  command=lambda: execute_query(query_input))
    submit_query.grid(row=10, column=0, columnspan=4)
    seperator_label_2 = tkinter.Label(window, bg="white").grid(row=11)


window = tkinter.Tk()
window.title("DB Boss")
create_start_window(window)
window.configure(background="#FFFFFF")
window.mainloop()
