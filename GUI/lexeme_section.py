import tkinter as tk
import tkinter as ttk

from data_structures import Lexeme


class LexemesSection:
    def __init__(self, parent, callback):
        self.description_var = None
        self.parent = parent
        self.callback = callback
        self.lexemes = []  # List to hold Lexeme objects

        self.setup_section()

    def setup_section(self):


        self.lexeme_listbox = tk.Listbox(self.parent)
        #self.lexeme_listbox.pack(fill="both", expand=True)
        self.lexeme_listbox.bind('<<ListboxSelect>>', self.on_lexeme_selected)
        self.lexeme_listbox.configure(background="grey")
        self.lexeme_listbox.pack(side="top", fill="both", expand=True)

        self.entry_var = tk.StringVar()
        self.lexeme_entry = ttk.Entry(self.parent, textvariable=self.entry_var)
        self.lexeme_entry.pack(ipady=5)

        self.add_btn = ttk.Button(self.parent, text="Add Lexeme", command=self.add_lexeme)
        self.add_btn.pack(ipady=5)
        # Description Entry
        self.description_var = tk.StringVar()
        self.description_entry = ttk.Entry(self.parent, textvariable=self.description_var)
        ttk.Label(self.parent, text="Description:").pack(ipady=5)
        self.description_entry.pack(ipady=5)

    def add_lexeme(self):
        lexeme_text = self.entry_var.get()
        description = self.description_var.get()
        translation = "dummy_translation"

        # Check for duplicates
        if any(l.lexeme == lexeme_text for l in self.lexemes):
            tk.messagebox.showwarning("Duplicate Entry", "This lexeme already exists!")
            return

        new_lexeme = Lexeme(lexeme_text, translation, description)
        self.lexemes.append(new_lexeme)
        self.lexeme_listbox.insert(tk.END, lexeme_text)

    def on_lexeme_selected(self, event):
        selected_index = self.lexeme_listbox.curselection()
        if selected_index:
            selected_lexeme = self.lexemes[selected_index[0]]
            self.callback(selected_lexeme)
