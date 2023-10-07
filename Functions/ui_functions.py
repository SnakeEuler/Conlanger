# ui_functions.py
import tkinter as tk
from tkinter import ttk

def create_tooltip(widget, text):
    tooltip = ttk.ToolTip(widget)
    tooltip.configure(text=text)
    return tooltip

def create_tab_layout(parent_frame):
    # Monitor (Sidebar)
    monitor = ttk.Frame(parent_frame, borderwidth=2, relief="groove", width=200)
    monitor.grid(row=0, column=0, rowspan=2, sticky="nsew")

    # Editor (Main Area)
    editor = ttk.Frame(parent_frame, borderwidth=2, relief="groove")
    editor.grid(row=0, column=1, sticky="nsew")

    # Inspector (Bottom Area)
    inspector = ttk.Frame(parent_frame, borderwidth=2, relief="groove", height=100)
    inspector.grid(row=1, column=1, sticky="nsew")

    # Configure grid weights
    parent_frame.grid_rowconfigure(0, weight=3)  # 3:1 ratio for editor:inspector
    parent_frame.grid_rowconfigure(1, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=3)  # 3:1 ratio for editor:monitor

    # Sample content for demonstration
    ttk.Label(monitor, text="Monitor").pack(pady=20)
    ttk.Label(editor, text="Editor").pack(pady=20)
    ttk.Label(inspector, text="Inspector").pack(pady=20)

