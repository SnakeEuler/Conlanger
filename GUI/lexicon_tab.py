from tkinter import ttk

from GUI.lexeme_section import LexemesSection


class LexiconTab:

    def __init__(self, notebook):
        # Main frame for the Lexicon tab
        self.frame = ttk.Frame(notebook)
        self.feature_frames = {}
        # Set up the main horizontal layout
        self.top_frame = ttk.Frame(self.frame)
        self.top_frame.pack(side='top', fill='both', expand=True)

        # Set up Monitor pane (Left pane within top_frame)
        self.monitor_pane = ttk.Frame(self.top_frame, relief='solid', borderwidth=1)
        self.monitor_pane.pack(side='left', fill='y', padx=5, pady=5, ipadx=5, ipady=5)
        self.setup_monitor_content()

        # Set up Editor pane (Central pane within top_frame)
        self.editor_pane = ttk.Frame(self.top_frame, relief='solid', borderwidth=1)
        self.editor_pane.pack(side='left', fill='both', expand=True, ipadx=5, ipady=5)
        # self.setup_editor_content()

        # Set up Inspector pane (Bottom pane with adjusted height)
        self.inspector_pane = ttk.Frame(self.frame, relief='solid', borderwidth=1, height=150)
        self.inspector_pane.pack(side='bottom', fill='x', padx=5, pady=5, ipadx=5, ipady=5)
        self.inspector_pane.pack_propagate(0)  # Prevent children from altering the pane's size
        self.setup_inspector_content()

    def setup_monitor_content(self):
        # Create sections for the Lexicon
        sections = ["Lexemes", "Word Forms", "Search"]
        for section in sections:
            btn = ttk.Button(self.monitor_pane, text=section, command=lambda s=section: self.show_section(s))
            btn.pack(fill="x", ipady=5)

    def show_section(self, section):
        # Hide all section frames
        for frame in self.feature_frames.values():
            frame.pack_forget()

        # Display the selected section frame
        if section == "Lexemes" and not hasattr(self, "lexemes_section"):
            self.lexemes_section = LexemesSection(self.editor_pane, self.update_inspector)
            self.feature_frames[section] = self.lexemes_section.parent
        elif section in self.feature_frames:
            self.feature_frames[section].pack(fill="both", expand=True)
        else:
            # For sections other than "Lexemes" that don't have a frame yet
            frame = ttk.Frame(self.editor_pane, relief='solid', borderwidth=1)
            label = ttk.Label(frame, text=f"Welcome to the {section} section. Content coming soon!")
            label.pack(pady=20)
            frame.pack(fill="both", expand=True)
            self.feature_frames[section] = frame

    def setup_inspector_content(self):
        # For now, just adding a label to indicate the inspector pane
        self.details_label = ttk.Label(self.inspector_pane, text="Details will appear here.")
        self.details_label.pack(pady=5)

    def update_inspector(self, selected_lexeme=None):
        # Clear current details in the inspector
        for widget in self.inspector_pane.winfo_children():
            widget.destroy()

        if selected_lexeme:
            # Using Entry fields for editable data
            lexeme_label = ttk.Label(self.inspector_pane, text="Lexeme:")
            lexeme_label.pack(pady=5)
            lexeme_entry = ttk.Entry(self.inspector_pane)
            lexeme_entry.insert(0, selected_lexeme.lexeme)
            lexeme_entry.pack(pady=5)

            description_label = ttk.Label(self.inspector_pane, text="Description:")
            description_label.pack(pady=5)
            description_entry = ttk.Entry(self.inspector_pane)
            description_entry.insert(0, selected_lexeme.description)
            description_entry.pack(pady=5)

            # Add a save/update button if needed
            update_btn = ttk.Button(self.inspector_pane, text="Update",
                                    command=lambda: self.save_edits(lexeme_entry, description_entry,
                                                                    selected_lexeme))
            update_btn.pack(pady=5)
        else:
            ttk.Label(self.inspector_pane, text="Details will appear here.").pack(pady=5)

    def save_edits(self, lexeme_entry, description_entry, selected_lexeme):
            # Update the lexeme object with new data
            selected_lexeme.lexeme = lexeme_entry.get()
            selected_lexeme.description = description_entry.get()
            # Optionally update other data structures or save to file
