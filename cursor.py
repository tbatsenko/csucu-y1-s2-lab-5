import exceptions


class Cursor:
    def __init__(self, document):
        """
        inits a new instance of Cursor class with attributes document
        and position
        """
        self.document = document
        self.position = 0

    def forward(self):
        """
        moves cursor one character forward
        """
        self.position += 1
        if self.position > len(self.document.characters):
            raise CursorEndError

    def back(self):
        """
        moves cursor one character back
        """
        self.position -= 1
        if self.position > len(self.document.characters):
            raise CursorTopError

    def home(self):
        """
        moves cursor to the top of the document
        """
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """
        moves cursor to the end of the document
        """
        while self.position < len(self.document.characters
                                  ) and self.document.characters[
                                      self.position].character != '\n':
            self.position += 1
