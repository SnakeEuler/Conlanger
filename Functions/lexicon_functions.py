# lexicon_functions.py

import tkinter as tk

def add_word(lexicon_data, word_entry, translation_entry, lexicon_listbox):
    word = word_entry.get()
    translation = translation_entry.get()
    if word and translation:
        lexicon_data[word] = translation
        lexicon_listbox.insert(tk.END, word)

def delete_word(lexicon_data, lexicon_listbox):
    selected_word = lexicon_listbox.get(tk.ACTIVE)
    if selected_word:
        del lexicon_data[selected_word]
        lexicon_listbox.delete(tk.ACTIVE)


def on_word_select(lexicon_data, lexicon_listbox, word_entry, translation_entry, event):
    selected_word = lexicon_listbox.get(tk.ACTIVE)
    if selected_word:
        word_entry.delete(0, tk.END)
        word_entry.insert(0, selected_word)

        translation_entry.delete(0, tk.END)
        translation_entry.insert(0, lexicon_data[selected_word])


def add_lexeme():
    pass

def delete_lexeme():
    pass

def add_word_form():
    pass

def delete_word_form():
    pass

def search_lexicon():
    # Search the lexicon for a word, lexeme, or word form
    # Ability to search by word, lexeme, or word form
    # Ability to search by part of speech
    # Ability to search by English translation
    # Ability to search in English or Proto-Language or Conlang
    pass
