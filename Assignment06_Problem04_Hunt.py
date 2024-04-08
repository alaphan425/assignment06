class LibraryItem():
    def __init__(self, title, subject, location):
        self.title = title
        self.subject = subject
        self.location = location
        self.checked_out = False
        
    def check_out(self):
        pass
        
    def return_item(self):
        pass
        
    def get_details(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, subject, location, author, ISBN):    
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN
    
    def check_out(self):
        if not self.checkout_out:
            self.checked_out = True
            print("Checking out the book:",self.title)
        else:
            print("The book",self.title,"is already checked out.")
            
    def return_item(self):
        if not self.checkout_out:
            self.checked_out = False
            print("Returning the book:",self.title)
        else:
            print("The book'"+str(self.title)+"'is already in the library.")
         
    def get_details(self):
        print("Title:",self.title)
        print("Subject:",self.subject)
        print("Author:",self.author)
        print("ISBN:",self.ISBN)
        print("Location:",self.location)
        print("Checked Out:",self.checked_out)


class DVD(LibraryItem):
    def __init__(self, title, subject, location, director, genre, run_time):    
        super().__init__(title, subject, location)
        self.director = director
        self.genre = genre
        self.run_time = run_time
        
    def check_out(self):
        if not self.checkout_out:
            self.checked_out = True
            print("Checking out the DVD:",self.title)
        else:
            print("The DVD",self.title,"is already checked out.")
            
    def return_item(self):
        if not self.checkout_out:
            self.checked_out = False
            print("Returning the DVD:",self.title)
        else:
            print("The DVD'"+str(self.title)+"'is already in the library.")
            
    def get_details(self):
        print("Title:",self.title)
        print("Subject:",self.subject)
        print("Director:",self.director)
        print("Genre:",self.genre)
        print("Run Time:",self.run_time)
        print("Location:",self.location)
        print("Checked Out:",self.checked_out)

class Journal(LibraryItem):
    def __init__(self, title, subject, location, volume, issue_number):
        super().__init__(title, subject, location)
        self.volume = volume
        self.issue_number = issue_number
        
    def check_out(self):
        if not self.checkout_out:
            self.checked_out = True
            print("Checking out the journal'"+str(self.title)+"' with issue number"+str(self.issue_number)+".")
        else:
            print("The journal'"+str(self.title)+"' with issue number",self.issue_number,"is already checked out.")
            
    def return_item(self):
        if not self.checkout_out:
            self.checked_out = False
            print("Returning the journal'"+str(self.title)+"' with issue number"+str(self.issue_number)+".")
        else:
            print("The journal'"+str(self.title)+"' with issue number",self.issue_number,"is already in the library.")
            
    def get_details(self):
        print("Title:",self.title)
        print("Subject:",self.subject)
        print("Volume:",self.volume)
        print("Issue Number:",self.issue_number)
        print("Location:",self.location)
        print("Checked Out:",self.checked_out)
        
class LibraryCatalog():
    def __init__(self):
        self.lib_items = []
    
    def add_item(self, item):
        self.lib_items.append(item)
        print("Item added to library catalog.")
        
    def remove_item(self, item):
        if item in self.lib_items:
            self.lib_items.remove(item)
            print("Item removed from library catalog.")
        self.catalog.append(item)