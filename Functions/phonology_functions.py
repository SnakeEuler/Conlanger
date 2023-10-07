# phonology_functions.py

def add_phoneme(phonemes, new_phoneme):
    # Add a new phoneme to the list.
    if not new_phoneme:
        return "Please enter a phoneme."
    if new_phoneme in phonemes:
        return "Phoneme already exists."
    phonemes.append(new_phoneme)
    return None  # No error


def delete_phoneme(phonemes, phoneme_to_delete):
    # Delete a phoneme from the list.
    if phoneme_to_delete in phonemes:
        phonemes.remove(phoneme_to_delete)
