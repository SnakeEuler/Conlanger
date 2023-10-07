import re
import tkinter as tk
from tkinter import ttk

from Functions.phonology_functions import delete_phoneme
from data_structures import Phoneme


class PhonemesSection:
    def __init__(self, parent, callback, symbol_entry, type_entry, ipa_entry, description_entry):
        self.parent = parent
        self.callback = callback
        self.symbol_entry = symbol_entry
        self.type_entry = type_entry
        self.ipa_entry = ipa_entry
        self.description_entry = description_entry
        self.selected_phoneme = None
        self.selected_button = None
        self.phonemes = []
        self.phoneme_buttons = []

        # Initialize the phonemes content
        self.setup_editor_content()

    def add_phoneme_logic(self):
        phoneme_input = self.search_var.get().strip()  # Get the phonemes from the search bar
        phonemes_to_add = [p.strip() for p in re.split('[, ]', phoneme_input) if
                           p.strip()]  # Split by space and comma and remove any empty entries

        for new_phoneme_symbol in phonemes_to_add:
            # Check if the phoneme symbol already exists in the inventory
            if new_phoneme_symbol not in [phoneme.symbol for phoneme in self.phonemes]:
                # Create a Phoneme object
                new_phoneme = Phoneme(symbol=new_phoneme_symbol, phoneme_type="SomeType", ipa_symbol="IPA",
                                      description="Description")  # Adjust parameters as needed
                self.phonemes.append(new_phoneme)

        self.refresh_phoneme_display()

    def delete_phoneme_logic(self):
        if self.selected_phoneme:
            delete_phoneme(self.phonemes, self.selected_phoneme)
            self.refresh_phoneme_display()

            # Reset the selected state
            self.selected_phoneme = None
            self.selected_button = None

    def setup_editor_content(self):
        # Grid for phonemes (to be created in create_phoneme_grid)
        self.phoneme_frame = ttk.Frame(self.parent)
        self.phoneme_frame.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)  # Spans all three columns
        self.parent.grid_rowconfigure(0, weight=1)  # Allow phoneme frame to expand

        # Adding a search bar
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.parent, textvariable=self.search_var)
        self.search_entry.grid(row=1, column=2, ipady=10, ipadx=30)  # Placed in the middle column
        self.search_entry.bind('<Return>', lambda event=None: self.add_phoneme_logic())

        # Add and delete phoneme buttons
        self.add_phoneme_btn = ttk.Button(self.parent, text="+", command=self.add_phoneme_logic)
        self.add_phoneme_btn.grid(row=1, column=0, ipady=10, ipadx=30)  # Placed in the leftmost column

        self.delete_phoneme_btn = ttk.Button(self.parent, text="-", command=self.delete_phoneme_logic)
        self.delete_phoneme_btn.grid(row=1, column=4, ipady=10, ipadx=30)  # Placed in the rightmost column

        # Initialize the phoneme buttons grid
        self.phoneme_buttons = []
        self.create_phoneme_grid()

    def create_phoneme_grid(self):
        for widget in self.phoneme_frame.winfo_children():
            widget.destroy()  # Clear previous buttons

        for i in range(len(self.phonemes)):
            row, col = divmod(i, 4)
            phoneme_btn = ttk.Button(
                self.phoneme_frame,
                text=self.phonemes[i].symbol,
                style="PhonemeButton.TButton",
                command=lambda i=i: self.on_phoneme_selected(i)
            )
            phoneme_btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.phoneme_buttons.append(phoneme_btn)

    def refresh_phoneme_display(self):
        # Clear the current buttons
        for btn in self.phoneme_buttons:
            btn.destroy()

        # Clear the list of phoneme buttons
        self.phoneme_buttons = []

        # Re-create the phoneme buttons
        self.create_phoneme_grid()

    def on_phoneme_selected(self, index):
        self.callback(self.phonemes[index])

    def update_inspector(self, selected_phoneme_obj):
        self.symbol_label.config(text=f"Symbol: {selected_phoneme_obj.symbol}")
        self.type_label.config(text=f"Type: {selected_phoneme_obj.phoneme_type}")
        self.ipa_label.config(text=f"IPA Symbol: {selected_phoneme_obj.ipa_symbol}")
        self.description_label.config(text=f"Description: {selected_phoneme_obj.description}")
