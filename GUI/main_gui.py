import tkinter as tk
from tkinter import ttk

from Functions.file_functions import load_language
from GUI.grammar_tab import GrammarTab
from GUI.lexicon_tab import LexiconTab
from GUI.morphology_tab import MorphologyTab
from GUI.phonology_tab import PhonologyTab
from GUI.start_tab import StartTab
from GUI.syntax_tab import SyntaxTab


class App:
    def __init__(self, root):
        self.root = root

        self.root.title("Conlang Evolution Tool")

        self.root.geometry("800x600")

        self.root.resizable(True, True)

        # Initialize the main container and notebook (tabs)

        self.container = ttk.Frame(self.root)

        self.nb = ttk.Notebook(self.root)

        self.nb.pack(fill="both", expand=True, ipady=10, ipadx=10)

        # Create Menu Bar

        self.create_menu()

        # Create Tabs

        self.create_phonology_tab()

        self.create_lexicon_tab()

        self.create_grammar_tab()

        self.create_morphology_tab()

        self.create_syntax_tab()

        self.create_start_tab()

        # Menu Bar
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        edit_menu = tk.Menu(menubar, tearoff=0)
        view_menu = tk.Menu(menubar, tearoff=0)
        help_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(label="New Language", command=self.create_new_language)
        file_menu.add_command(label="Load Language", command=load_language)
        file_menu.add_command(label="Settings", command=self.open_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="Edit", menu=edit_menu)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="View", menu=view_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def create_phonology_tab(self):
        self.phonology_tab = PhonologyTab(self.nb)  # Passing the correct notebook reference

        self.nb.add(self.phonology_tab.frame, text="Phonology")

    def create_start_tab(self):
        self.start_tab = StartTab(self.nb)
        self.nb.add(self.start_tab.frame, text='Setup')

    def create_lexicon_tab(self):
        self.lexicon_tab = LexiconTab(self.nb)  # Passing the correct notebook reference
        self.nb.add(self.lexicon_tab.frame, text='Lexicon')

    def create_grammar_tab(self):
        self.grammar_tab = GrammarTab(self.nb)  # Passing the correct notebook reference

        self.nb.add(self.grammar_tab.frame, text="Grammar")

    def create_morphology_tab(self):
        self.morphology_tab = MorphologyTab(self.nb)  # Passing the correct notebook reference

        self.nb.add(self.morphology_tab.frame, text="Morphology")

    def create_syntax_tab(self):
        self.syntax_tab = SyntaxTab(self.nb)  # Passing the correct notebook reference

        self.nb.add(self.syntax_tab.frame, text="Syntax")

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")

    def create_new_language(self):
        setup_window = tk.Toplevel()
        setup_window.title("New Language Setup")
        setup_window.geometry("400x400")
        setup_window.resizable(False, False)

        self.setup_frame = ttk.Frame(setup_window)
        self.setup_frame.pack(fill="both", expand=True)

        ttk.Label(self.setup_frame, text="Proto-Language Setup").pack(pady=10)
        ttk.Label(self.setup_frame, text="Enter Consonants (comma-separated):").pack(pady=5)

        self.consonants_entry = ttk.Entry(self.setup_frame)
        self.consonants_entry.pack(pady=5)

        ttk.Label(self.setup_frame, text="Enter Vowels (comma-separated):").pack(pady=5)

        self.vowels_entry = ttk.Entry(self.setup_frame)
        self.vowels_entry.pack(pady=5)

        self.phoneme_details_btn = ttk.Button(self.setup_frame, text="Proceed to Phoneme Details",
                                              command=self.show_phoneme_details)
        self.phoneme_details_btn.pack(pady=20)
