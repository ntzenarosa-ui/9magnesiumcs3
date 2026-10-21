#making a parent class
class Publication:
    def __init__(self, title, author): #initialize
        self.__title = title
        self.__author = author
    @property
    def title(self):
        return self.__title
        
    @property
    def author(self):
        return self.__author
#child class
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages
    @property
    def get_num(self):
        return self.__number_of_pages

    @property
    def set_num(self):
        if number_of_pages >= 0:
            return number_of_pages
        else:
            print("Number of pages must be positive.")
#child class
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number
        
# Creating objects
pub1 = Publication("Love as", "Ethan David P. Solano")
book1 = Book("Guyabano", "Ethan Jer S. Ecal", 310)
mag1 = Magazine("Mgasin", "Magnesium", 202)

#Printing the information
print("Publication Information:") #Header
print(f"Title: {pub1.title}") #prints the title
print(f"Author: {pub1.author}") #prints the author's name

print("\nBook Information:")
print(set_num)
print(f"Title: {book1.title}")
print(f"Author: {book1.author}")
print(f"Number of pages: {book1.get_num}")
