print("<11_1>\n")

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")

class Book(Publication):

    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}, Page: {self.page}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.editor}")

p =[]
p.append( Magazine("Donald Duck", "Aki Hyyppä"))
p.append( Book("Compartment No. 6", "Rosa Liksom", 192))
for i in p:
    i.print_information()
