class Character:
    def __init__(self, character, bold=False, italic=False,
                 underline=False):
        """
        inits a new instance of Character class with attributes character,
        bold, italic and underline
        """
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        updates how the char will be represented
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character
