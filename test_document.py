from document import Document
from character import Character


d = Document()
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print(d.string)

d.cursor.home()
d.delete()
d.insert('W')
print(d.string)

d.characters[0].underline = True
print(d.string)
