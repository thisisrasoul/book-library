import tkinter as tk
from tkinter import *

class book_class():
    book = []
    solds_book = []

root=tk.Tk()
root.title("book")
root.geometry("800x400")

name_var=tk.StringVar()
author_var=tk.StringVar()
sold_customer_var=tk.StringVar()
price_var=tk.IntVar()
count_var=tk.IntVar()

name_var.set("")
author_var.set("")
price_var.set("")
count_var.set("")
sold_customer_var.set("")

def report():
        if book_class.book:
            output.delete('1.0',END)
            for books in book_class.book:
                output.insert('1.0',"name: "+books["name"] + " - author: " + books["author"]+" - price: "+str(books["price"])+" - count: "+str(books["count"]) + ". \n")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")
               
        else:
            output.delete('1.0',END)
            output.insert(END,"you haven't enter any books")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")

def sell_report():
    if book_class.solds_book:
        output.delete('1.0',END)
        for books in book_class.solds_book:
            output.insert('1.0',"name: "+books["name"] + " - price: "+str(books["price"])+ "buyername: "+ books["buyername"] + ". \n")          
        name_var.set("")
        author_var.set("")
        price_var.set("")
        count_var.set("")
        sold_customer_var.set("")

    else:
        output.delete('1.0',END)
        output.insert(END,"there isnt any sold books")
        name_var.set("")
        author_var.set("")
        price_var.set("")
        count_var.set("")
        sold_customer_var.set("")

def add_button():
    # root1=tk.Tk()
    # root1.title("add book")
    # root1.geometry("500x200")
    name=name_var.get()
    author=author_var.get()
    price=price_var.get()
    count=count_var.get()
    books = {"name": name, "author": author, "price": price,"count": count}
    book_class.book.append(books)
            
    name_var.set("")
    author_var.set("")
    price_var.set("")
    count_var.set("")
    sold_customer_var.set("")
   # root1.mainloop()
def sell_button():
    name=name_var.get()
    buyername=sold_customer_var.get()
    for books in book_class.book: 
        if books["name"].lower() == name.lower() and int(books["count"]) == 1:
            soldbooks = {"name": name, "author": books["author"], "price": books["price"], "buyername":buyername } 
            book_class.solds_book.append(soldbooks) 
            book_class.book.remove(books)
            output.delete('1.0',END)
            output.insert(END,"book sold")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")
            break
        elif books["name"].lower() == name.lower() and int(books["count"]) >=2 :
            updatebook = {"name": name, "author": books["author"], "price": books["price"], "count":(books["count"] - 1)}
            soldbooks = {"name": name, "author": books["author"], "price": books["price"], "buyername":buyername } 
            book_class.solds_book.append(soldbooks) 
            book_class.book.append(updatebook)
            book_class.book.remove(books)
            output.delete('1.0',END)
            output.insert(END,"book sold")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")
             
        else:
            output.delete('1.0',END)
            output.insert(END,"worng entries")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")

def search_button():
    found_book = []
    name=name_var.get()
    author=author_var.get()
    for books in book_class.book:
        if books["name"].lower() == name.lower() or books["author"].lower() == author.lower():
                book1 = {"name": books["name"], "author": books["author"], "price": books["price"],"count": books["count"]}
                found_book.append(book1)

        if found_book: 
            print("Matching book found:\n")
            output.delete('1.0',END)
            for book2 in found_book:
                output.insert('1.0',"name: "+book2["name"] + " - author: " + book2["author"]+" - price: "+str(book2["price"])+" - count: "+str(book2["count"]) + ". \n")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")
        else:
            output.delete('1.0',END)
            output.insert(END,"there isn't this book")
            name_var.set("")
            author_var.set("")
            price_var.set("")
            count_var.set("")
            sold_customer_var.set("")

def clear_button():
     print("")

name_label = tk.Label(root, text = 'book name')
name_entry = tk.Entry(root,textvariable = name_var)

author_label = tk.Label(root, text = 'author')
author_entry=tk.Entry(root, textvariable = author_var)

price_lable=tk.Label(root,text= 'price')
price_entry=tk.Entry(root,textvariable= price_var)

count_lable=tk.Label(root,text= 'count')
count_entry=tk.Entry(root,textvariable= count_var)

sold_customer_lable=tk.Label(root,text= 'buyer name (Enter just for sell option)')
sold_customer_entry=tk.Entry(root,textvariable= sold_customer_var)

add_but=tk.Button(root,text = 'Add', command = add_button)
sell_but=tk.Button(root,text = 'Sell', command = sell_button)
report_but=tk.Button(root,text = 'Report', command = report)
sell_rep_but=tk.Button(root,text = 'sell report', command = sell_report)
search_but=tk.Button(root,text= 'search',command = search_button)

output = tk.Text(root, height = 5, width = 65, bg = "gray",pady=30)

name_label.grid(row=0,column=0, sticky = W)
name_entry.grid(row=0,column=1)
author_label.grid(row=1,column=0, sticky = W)
author_entry.grid(row=1,column=1)
price_lable.grid(row=2,column=0, sticky = W)
price_entry.grid(row=2,column=1)
count_lable.grid(row=3,column=0, sticky = W)
count_entry.grid(row=3,column=1)
sold_customer_lable.grid(row=4,column=0, sticky = W)
sold_customer_entry.grid(row=4,column=1)
add_but.grid(row=0,column=3)
sell_but.grid(row=1,column=3)
report_but.grid(row=2,column=3)
sell_rep_but.grid(row=3,column=3,padx=20,sticky=E)
search_but.grid(row=4,column=3)
output.grid(row=7,column=0,pady=20)

root.mainloop()

def book_menu(): 
        print("Book Menu\n")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Update a book")
        print("4. sell a book")
        print("5. Display all book")
        print("6. Display sold book")
        print("7. Exit\n")

def sold_books_def(name,author,price,buyername):
        soldbooks = {"name": name, "author": author, "price": price, "buyername": buyername} 
        book_class.solds_book.append(soldbooks) 
        print("-------------------")

def add_book():
        name = input("Enter the book's name: ")
        author = input("Enter the book's author: ")
        price = input("Enter the book's price: ")
        count = input("Enter the book's count: ")
        books = {"name": name, "author": author, "price": price,"count": count}
        book_class.book.append(books) 
        print("book added successfully!")

def search_book():
        search_term = input("Enter the name or author of the books to search: ") 
        found_book = []
        for books in book_class.book:
            if search_term.lower() in books["name"].lower() or search_term.lower() in books["author"].lower():
                found_book.append(books)

        if found_book: 
            print("Matching book found:\n")
            for books in found_book: 
                print("name:", books["name"])
                print("author:", books["author"])
                print("price:", books["price"])
                print("count:", books["count"])
                print("-------------------")
        else:
            print("No matching book found.")

def update_book():
        name = input("Enter the name of the book to update: ")
        for books in book_class.book: 
            if books["name"].lower() == name.lower():
                found_contact = books
                break

        if found_contact:
            print("book found. Enter new details:\n")
            found_contact["name"] = input("Enter the new name: ")
            found_contact["author"] = input("Enter the new author: ")
            found_contact["price"] = input("Enter the new price: ")
            found_contact["count"] = input("Enter the new count: ")
            print("book updated successfully!")
        else:
            print("book not found.")

def sell_book():
        name = input("Enter the name of the book to sell: ")
        for books in book_class.book: 
            buyername = input("Enter the buyer name : ")
            if books["name"].lower() == name.lower():
                sold_books_def(books["name"],books["author"],books["price"],buyername)
                book_class.book.remove(books)
                print("book deleted successfully!")
                break
        else:
            print("book not found.")

def display_all_books():

        if book_class.book:
            print("All books:")
            for books in book_class.book:
                print("name:", books["name"])
                print("author:", books["author"])
                print("price:", books["price"])
                print("count:", books["count"])
                print("-------------------") 
        else:
            print("No book found.")

def dis_sold_books():

        if book_class.solds_book:
            print("All sold books:")
            for soldbooks in book_class.solds_book:
                print("name:", soldbooks["name"])
                print("author:", soldbooks["author"])
                print("price:", soldbooks["price"])
                print("-------------------") 
        else:
            print("No book sold.")

while True:
    
    book_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        sell_book()
    elif choice == "5":
        display_all_books()
    elif choice == "6":
        dis_sold_books()
    elif choice == "7":
        print("Exiting the program...")
        break 
    else:
            print("Invalid choice. Please enter a valid option (1-6).")