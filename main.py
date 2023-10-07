from ttkthemes import ThemedTk
from GUI.main_gui import App

def main():
    root = ThemedTk(theme="equilux")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
