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

""" ------------------------ SYNTAX HIGHLIGHTING ---------------------------"""

def highlight_pattern(textbox, pattern, tag, start="1.0", end="end",
                      regexp=False):
    '''Apply the given tag to all text that matches the given pattern

    If 'regexp' is set to True, pattern will be treated as a regular
    expression.
    
    Original code:
        https://stackoverflow.com/questions/34818960/how-to-highlight-a-specific-word-in-tkinter
    '''

    start = textbox.index(start)
    end = textbox.index(end)
    textbox.mark_set("matchStart", start)
    textbox.mark_set("matchEnd", start)
    textbox.mark_set("searchLimit", end)

    count = tkinter.IntVar()
    while True:
        index = textbox.search(pattern, "matchEnd","searchLimit",
                            count=count, regexp=regexp)
        if index == "": break
        textbox.mark_set("matchStart", index)
        textbox.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
        textbox.tag_add(tag, "matchStart", "matchEnd")

def highlight(textbox):
    textbox.tag_configure("blue", foreground="blue")
    textbox.tag_configure("orange", foreground="orange")
    
    highlight_pattern(textbox, "SELECT", "blue")
    highlight_pattern(textbox, "IN", "blue")
    highlight_pattern(textbox, "FROM", "blue")
    highlight_pattern(textbox, "IS", "blue")
    highlight_pattern(textbox, "WHERE", "blue")
    highlight_pattern(textbox, "AND", "blue")
    highlight_pattern(textbox, "OR", "blue")
    highlight_pattern(textbox, "JOIN", "blue")
    highlight_pattern(textbox, "UNION", "blue")
    highlight_pattern(textbox, "CASE", "blue")
    highlight_pattern(textbox, "WHEN", "blue")
    highlight_pattern(textbox, "\.\w*", "orange", regexp=True)
    

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
    query_input.bind("<KeyRelease>", lambda event: highlight(query_input))
    seperator_label_2 = tkinter.Label(window, bg="white").grid(row=9)
    submit_query = tkinter.Button(window, text="Execute", width=57, pady=8,
                                  command=lambda: execute_query(query_input))
    submit_query.grid(row=10, column=0, columnspan=4)
    seperator_label_2 = tkinter.Label(window, bg="white").grid(row=11)


window = tkinter.Tk()
window.title("DB Boss")
create_start_window(window)
window.configure(background="#FFFFFF")
window.iconbitmap(r"C:\Users\Tim\Downloads\database-16(2).ico")
window.mainloop()
