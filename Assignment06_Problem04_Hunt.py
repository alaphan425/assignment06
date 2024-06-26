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
        if self.checked_out == False:
            self.checked_out = True
            print("Checking out the book:",self.title)
        else:
            raise ValueError("The book",self.title,"is already checked out.")
            
    def return_item(self):
        if self.checked_out == True:
            self.checked_out = False
            print("Returning the book:",self.title)
        else:
            raise ValueError("The book '"+str(self.title)+"' is already in the library.")
         
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
        if self.checked_out == False:
            self.checked_out = True
            print("Checking out the DVD:",self.title)
        else:
            raise ValueError("The DVD '"+str(self.title)+"' is already checked out.")
            
    def return_item(self):
        if self.checked_out == True:
            self.checked_out = False
            print("Returning the DVD:",self.title)
        else:
            raise ValueError("The DVD'"+str(self.title)+"'is already in the library.")
            
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
        if self.checked_out == False:
            self.checked_out = True
            print("Checking out volume "+str(self.volume)+" of the journal '"+str(self.title)+"' with issue number"+str(self.issue_number)+".")
        else:
            raise ValueError("Volume "+str(self.volume)+" of the journal '"+str(self.title)+"' with issue number",self.issue_number,"is already checked out.")
            
    def return_item(self):
        if self.checked_out == True:
            self.checked_out = False
            print("Returning volume "+str(self.volume)+" of the journal '"+str(self.title)+"' with issue number"+str(self.issue_number)+".")
        else:
            raise ValueError("Volume "+str(self.volume)+" of the journal '"+str(self.title)+"' with issue number",self.issue_number,"is already in the library.")
            
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
        else:
            raise ValueError("No such item found in in catalog.")
        
    def find_item_by_title(self, title):
        item_found = False
        for item in self.lib_items:
            if item.title == title:
                print("The item titled '"+str(item.title)+"' is located at "+str(item.location)+".")
                item_found = True
                break
        if item_found == False:
            raise ValueError("No item with such title found in catalog.")

    def check_out_item(self, item):
        if item in self.lib_items:
            item.check_out()
        else:
            raise ValueError("No such item found in catalog.")

    def return_item(self, item):
        if item in self.lib_items:
            item.return_item()
        else:
            raise ValueError("No such item found in catalog.")