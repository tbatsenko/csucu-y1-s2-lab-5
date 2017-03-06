from cursor import Cursor
from character import Character


class Document:
    def __init__(self):
        """
        inits a new instance of Document class with attributes characters,
        cursor and filename
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    @property
    def string(self):
        """
        returns a string of styled chars
        """
        return "".join((str(c) for c in self.characters))

    def insert(self, character):
        """
        insters the character to the position, where the cursor is
        located now
        """
        if not hasattr(character, 'character'):
            character = Character(character)

        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        deletes the character from the position, where the cursor is
        located now
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        saves the document to the file with its filename
        """
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
