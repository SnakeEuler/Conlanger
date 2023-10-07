import tkinter as tk

from tkinter import ttk


class MorphologyTab:

    def __init__(self, notebook):
        # Main frame for the Lexicon tab
        self.frame = ttk.Frame(notebook)

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
    def setup_monitor_content(self):
        # Adding some mock buttons to the Monitor pane
        self.add_word_btn = ttk.Button(self.monitor_pane, text="Add Word")
        self.add_word_btn.pack(pady=5)

        self.delete_word_btn = ttk.Button(self.monitor_pane, text="Delete Word")
        self.delete_word_btn.pack(pady=5)

        self.search_entry = ttk.Entry(self.monitor_pane)
        self.search_entry.pack(pady=5, padx=10)

    def setup_editor_content(self):
        # Displaying words in the Listbox
        ttk.Label(self.editor_pane, text="Word in Proto-Language:").pack(pady=5)
        self.word_entry = ttk.Entry(self.editor_pane)
        self.word_entry.pack(pady=5)

        ttk.Label(self.editor_pane, text="English Translation:").pack(pady=5)
        self.translation_entry = ttk.Entry(self.editor_pane)
        self.translation_entry.pack(pady=5)

        self.lexicon_listbox = tk.Listbox(self.editor_pane)
        self.lexicon_listbox.pack(pady=10, fill="both", expand=True)

    def setup_inspector_content(self):
        # For now, just adding a label to indicate the inspector pane
        ttk.Label(self.inspector_pane, text="Details will appear here.").pack(pady=5)
