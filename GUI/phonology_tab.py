import tkinter as tk
from tkinter import ttk

from GUI.phonemes_section import PhonemesSection


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

        self.feature_frames = {}
        self.phonemes_section = None

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

        # Set up Inspector pane (Bottom pane with adjusted height)
        self.inspector_pane = ttk.Frame(self.frame, relief='solid', borderwidth=1, height=150)
        self.inspector_pane.pack(side='bottom', fill='x', padx=5, pady=5, ipadx=5, ipady=5)
        self.inspector_pane.pack_propagate(0)  # Prevent children from altering the pane's size
        self.setup_inspector_content()

        self.new_phoneme = None

    def setup_monitor_content(self):
        # Adding sections for features in the Monitor pane
        features = ["Phonemes", "Syllable Structure", "Stress", "Feature Geometry", "Tone", "Intonation"]
        for feature in features:
            btn = ttk.Button(self.monitor_pane, text=feature, command=lambda f=feature: self.show_feature(f))
            btn.pack(fill="x", ipady=5)

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

    def update_inspector(self, selected_phoneme_obj=None):
        # Update the selected_phoneme
        self.selected_phoneme = selected_phoneme_obj

        # Clear current details in the inspector
        self.symbol_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.ipa_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

        if selected_phoneme_obj:
            self.symbol_entry.insert(0, selected_phoneme_obj.symbol)
            self.type_entry.insert(0, selected_phoneme_obj.phoneme_type)
            self.ipa_entry.insert(0, selected_phoneme_obj.ipa_symbol)
            self.description_entry.insert(0, selected_phoneme_obj.description)

    def save_changes(self):
        if self.selected_phoneme:
            # Update the Phoneme object's attributes with values from the inspector fields
            self.selected_phoneme.symbol = self.symbol_entry.get()
            self.selected_phoneme.phoneme_type = self.type_entry.get()
            self.selected_phoneme.ipa_symbol = self.ipa_entry.get()
            self.selected_phoneme.description = self.description_entry.get()

            # Update the display of phonemes (this may be necessary if the phoneme's symbol changes)
            if hasattr(self, "phonemes_section") and self.phonemes_section:
                self.phonemes_section.refresh_phoneme_display()

    def on_phoneme_selected(self, selected_phoneme):
        self.selected_phoneme = selected_phoneme

        self.symbol_entry.delete(0, tk.END)
        self.symbol_entry.insert(0, selected_phoneme.symbol)
        self.type_entry.delete(0, tk.END)
        self.type_entry.insert(0, selected_phoneme.phoneme_type)
        self.ipa_entry.delete(0, tk.END)
        self.ipa_entry.insert(0, selected_phoneme.ipa_symbol)
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, selected_phoneme.description)

    def show_feature(self, feature):
        # Hide all feature frames
        for frame in self.feature_frames.values():
            frame.pack_forget()

        # Display the selected feature frame
        if feature == "Phonemes" and not self.phonemes_section:
            # Initialize and pack the PhonemesSection only when selected for the first time
            self.phonemes_section = PhonemesSection(self.editor_pane, self.update_inspector,
                                                    self.symbol_entry, self.type_entry,
                                                    self.ipa_entry, self.description_entry)
            self.feature_frames[feature] = self.phonemes_section.parent
        elif feature in self.feature_frames:
            self.feature_frames[feature].pack(fill="both", expand=True)
        else:
            # For features other than "Phonemes" that don't have a frame yet
            frame = ttk.Frame(self.editor_pane, relief='solid', borderwidth=1)
            label = ttk.Label(frame, text=f"Welcome to the {feature} section. Content coming soon!")
            label.pack(pady=20)
            frame.pack(fill="both", expand=True)
            self.feature_frames[feature] = frame
