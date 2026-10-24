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
    @property
    def get_issue(self):
        return self.__issue_number
        
# Creating objects
pub1 = Publication("Love as", "Ethan David P. Solano")
book1 = Book("Guyabano", "Ethan Jer S. Ecal", 310)
mag1 = Magazine("Mgasin", "Magnesium", 202)

#Printing the information
print("Publication Information:") #Header
print(f"Title: {pub1.title}") #prints the title
print(f"Author: {pub1.author}") #prints the author's name

print("\nBook Information:")
book1.set_num(-110) #testing data validation with negative number
print(f"Title: {book1.title}") #prints book's title
print(f"Author: {book1.author}") #prints book's author
print(f"Number of pages: {book1.get_num}") #prints book's number of pages

print("\nMagazine Information:") 
print(f"Title: {mag1.title}") #prints magazine's title
print(f"Author: {mag1.author}") #prints magazines's author
print(f"Number of pages: {mag1.get_issue}") #prints magazine's number of pages
