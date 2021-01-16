#Creating a class librabry
class Library:
    # class takes an input as list of books available and name of the library
    def __init__(self,listofbooks,name):
        self.listofbooks=list(listofbooks)
        self.name=name
    # variable action ask visitor to make his choice

    borrowersdetail={}

    # Display print's a list of books available with us
    def display(self):
        print(f"We have {self.listofbooks} available with us.")
    # oprates only when visitor wants to lend a book

    def lend(self):
        bookname=input("Enter the name of the book you are lending").capitalize()

        # check whether the book is available in library or not.

        if bookname not in self.listofbooks :
            if bookname not in  self.borrowersdetail:
                print("Sorry currently this book is not available ,we will arrange it shortly.")
            else:
                print(f"Sorry this book's is currently borrowed by {self.borrowersdetail[bookname]}")


        # makes an entry of the person name and book name while lending


        else:
            self.borrowersdetail[bookname]=[input("Please enter your name")]
            self.listofbooks.remove(bookname)
    # oprates when someone wants to donate a book to library
    def donate(self):
        # add's the book in the list of available book list
        addbook=input("Please enter the name of the book you want to add.")
        self.listofbooks.append(addbook)
        return ("Thanks for your contribution.")

    # oprates when someone comes to return the book
    def _return(self):
        bookname = input("Enter the name of the book you are returning")
        # add's the book back to the available list
        self.listofbooks.append(bookname)
        # remove the name from borrower's list
        self.borrowersdetail.pop(bookname)

# Defining a funcion to run the class smoothly
def start():
    if __name__ == '__main__':

        lst=['C++','C','Python','Java','PHP']
        lib_name="Programing"
        a=Library(lst,lib_name)
        stop=False
        while stop==False:
            a.display()
            allowed=['l','r','d','ex']
            action=input("Please enter your choice (l:lend a book) (r:return a book) (d:donate a book) (ex:exit library.)").lower()
            if action not in allowed:
                print("Please give a valid input")
            else:
                if action=="ex":
                    stop=True
                elif action=="l":
                    a.lend()
                elif action=="r":
                    a._return()
                elif action=='d':
                    a.donate()
start()