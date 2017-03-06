from cursor import Cursor
from character import Character
import exceptions


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

    """
c. збереження файлу без імені
d. введення декількох символів

    """
    def insert(self, character):
        """
        insters the character to the position, where the cursor is
        located now
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        if len(character.character) > 1:
            raise NotChar
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        deletes the character from the position, where the cursor is
        located now
        """
        try:
            del self.characters[self.cursor.position]
        except:
            raise CharacterDontExist

    def save(self):
        """
        saves the document to the file with its filename
        """
        if not self.filename:
            raise NoFilename
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
