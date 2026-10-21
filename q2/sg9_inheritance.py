class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @property
    def title(self):
        return self.title
    @property
    def author(self):
        return self.author
    
class Book(Publication):
    def

class Magazine(Publication):
    def 


# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Printing the information
print("Publication Information")
pub1.display_info()

print("\nBook Information")
book1.set_number_of_pages(-310) #setting invalid