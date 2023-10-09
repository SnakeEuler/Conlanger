from tkinter import ttk

from ttkthemes import ThemedTk

from GUI.main_gui import App


def main():
    root = ThemedTk(theme="equilux")
    app = App(root)
    root.mainloop()
    style = ttk.Style()
    style.configure("TButton", padding=5, relief="flat", background="#ccc")
    style.configure("TEntry", padding=5, relief="flat")
    style.configure("TLabel", padding=5)


if __name__ == "__main__":
    main()
