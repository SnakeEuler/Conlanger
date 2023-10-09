
class Phoneme:
    def __init__(self, symbol, phoneme_type, ipa_symbol=None, description=None):
        self.symbol = symbol
        self.phoneme_type = phoneme_type
        self.ipa_symbol = ipa_symbol
        self.description = description


class Word:
    def __init__(self, proto_representation, english_translation, part_of_speech):
        self.proto_representation = proto_representation
        self.english_translation = english_translation
        self.part_of_speech = part_of_speech  # e.g., "noun", "verb"

class GrammarRule:
    def __init__(self, rule_type, description):
        self.rule_type = rule_type  # e.g., "verb conjugation"
        self.description = description
        self.examples = []

class Lexeme:
    def __init__(self, lexeme, translation, description):
        self.lexeme = lexeme
        self.translation = translation
        self.description = description
        # You can add more attributes as needed
