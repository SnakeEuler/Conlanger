import re
import tkinter as tk
from tkinter import ttk

from Functions.phonology_functions import delete_phoneme
from data_structures import Phoneme


class PhonologyTab:
    def __init__(self, notebook):
        # Main frame for the Phonology tab
        style = ttk.Style()
        style.configure('PhonemeButton.TButton', font=('Helvetica', 16))
        style.configure('TButton', relief="raised", foreground="white")
        style.map('TButton', background=[('pressed', 'black'), ('active', 'white')])

        self.selected_phoneme = None
        self.selected_button = None

        self.phonemes = []
        self.phoneme_buttons = []

        self.frame = ttk.Frame(notebook)
        self.frame.pack(fill="both", expand=True)

        # Set up the main horizontal layout
        self.top_frame = ttk.Frame(self.frame)
        self.top_frame.pack(side='top', fill='both', expand=True)

        # Set up Monitor pane (Left pane within top_frame)
        self.monitor_pane = ttk.Frame(self.top_frame, relief='solid', borderwidth=1)
        self.monitor_pane.pack(side='left', fill='y', padx=5, pady=5, ipadx=5, ipady=5)
        self.setup_monitor_content()

        # Set up Editor pane (Central pane within top_frame)
        self.editor_pane = ttk.Frame(self.top_frame, relief='solid', borderwidth=1)
        self.editor_pane.pack(side='left', fill='both', expand=True, padx=5, pady=5, ipadx=5, ipady=5)
        self.setup_editor_content()

        # Set up Inspector pane (Bottom pane with adjusted height)
        self.inspector_pane = ttk.Frame(self.frame, relief='solid', borderwidth=1, height=150)
        self.inspector_pane.pack(side='bottom', fill='x', padx=5, pady=5, ipadx=5, ipady=5)
        self.inspector_pane.pack_propagate(0)  # Prevent children from altering the pane's size
        self.setup_inspector_content()

        self.new_phoneme = None
        self.create_phoneme_grid()

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

    def setup_monitor_content(self):
        # Adding sections for features in the Monitor pane
        features = ["Phonemes", "Syllable Structure", "Stress", "Feature Geometry", "Tone", "Intonation"]
        for feature in features:
            btn = ttk.Button(self.monitor_pane, text=feature)
            btn.pack(fill="x", ipady=5)

    def setup_editor_content(self):
        # Grid for phonemes (to be created in create_phoneme_grid)
        self.phoneme_frame = ttk.Frame(self.editor_pane)
        self.phoneme_frame.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)  # Spans all three columns
        self.editor_pane.grid_rowconfigure(0, weight=1)  # Allow phoneme frame to expand

        # Adding a search bar
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.editor_pane, textvariable=self.search_var)
        self.search_entry.grid(row=1, column=2, ipady=10, ipadx=30)  # Placed in the middle column
        self.search_entry.bind('<Return>', lambda event=None: self.add_phoneme_logic())

        # Add and delete phoneme buttons
        self.add_phoneme_btn = ttk.Button(self.editor_pane, text="+", command=self.add_phoneme_logic)
        self.add_phoneme_btn.grid(row=1, column=0, ipady=10, ipadx=30)  # Placed in the leftmost column

        self.delete_phoneme_btn = ttk.Button(self.editor_pane, text="-", command=self.delete_phoneme_logic)
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

    def setup_inspector_content(self):
        # Details for the selected phoneme
        ttk.Label(self.inspector_pane, text="Phoneme Details:").grid(row=0, column=0, pady=5, sticky='w', columnspan=2)

        # Display phoneme's symbol
        ttk.Label(self.inspector_pane, text="Symbol:").grid(row=1, column=0, pady=5, sticky='w')
        self.symbol_entry = ttk.Entry(self.inspector_pane)
        self.symbol_entry.grid(row=1, column=1, pady=5, sticky='ew')

        # Display phoneme's type
        ttk.Label(self.inspector_pane, text="Type:").grid(row=2, column=0, pady=5, sticky='w')
        self.type_entry = ttk.Entry(self.inspector_pane)
        self.type_entry.grid(row=2, column=1, pady=5, sticky='ew')

        # Display phoneme's IPA symbol
        ttk.Label(self.inspector_pane, text="IPA Symbol:").grid(row=3, column=0, pady=5, sticky='w')
        self.ipa_entry = ttk.Entry(self.inspector_pane)
        self.ipa_entry.grid(row=3, column=1, pady=5, sticky='ew')

        # Display phoneme's description
        ttk.Label(self.inspector_pane, text="Description:").grid(row=4, column=0, pady=5, sticky='w')
        self.description_entry = ttk.Entry(self.inspector_pane)
        self.description_entry.grid(row=4, column=1, pady=5, sticky='ew')

        # Save button
        self.save_btn = ttk.Button(self.inspector_pane, text="Save Changes", command=self.save_changes)
        self.save_btn.grid(row=5, column=1, pady=10, sticky='e')

    def save_changes(self):
        if self.selected_phoneme:
            self.selected_phoneme.symbol = self.symbol_entry.get()
            self.selected_phoneme.phoneme_type = self.type_entry.get()
            self.selected_phoneme.ipa_symbol = self.ipa_entry.get()
            self.selected_phoneme.description = self.description_entry.get()
            self.refresh_phoneme_display()

    def on_phoneme_selected(self, index):
        # Deselect previously selected button

        selected_phoneme = self.phonemes[index]
        self.selected_phoneme = selected_phoneme
        self.selected_button = self.phoneme_buttons[index]

        # Populate the entry widgets with the selected phoneme details
        self.symbol_entry.delete(0, tk.END)
        self.symbol_entry.insert(0, selected_phoneme.symbol)

        self.type_entry.delete(0, tk.END)
        self.type_entry.insert(0, selected_phoneme.phoneme_type)

        self.ipa_entry.delete(0, tk.END)
        self.ipa_entry.insert(0, selected_phoneme.ipa_symbol)

        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, selected_phoneme.description)

    def update_inspector(self, index):
        # Here, fetch the details of the selected phoneme and display them in the inspector pane
        # For now, I'll just update the self.detail_label, but you can expand this to show more details
        # self.detail_label.config(text=self.selected_phoneme)
        # Here, update the inspector with the selected phoneme's details
        selected_phoneme_obj = self.phonemes[index]  # Assuming self.phonemes now contains Phoneme objects
        self.symbol_label.config(text=f"Symbol: {selected_phoneme_obj.symbol}")
        self.type_label.config(text=f"Type: {selected_phoneme_obj.phoneme_type}")
        self.ipa_label.config(text=f"IPA Symbol: {selected_phoneme_obj.ipa_symbol}")
        self.description_label.config(text=f"Description: {selected_phoneme_obj.description}")
