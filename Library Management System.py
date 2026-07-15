def lms(book):
    ch=1
    n=4
    while ch!=n:
        print("1. For Show all book list")
        print("2. For Borrow Book")
        print("3. For Return Book")
        print("4. Exit")
        ch = int(input("Enter your choice:"))
        if (ch==1):
            for i in book:
               print(i,book[i])
               print("     ----------      ")
        elif(ch==2):
            u_book=input("Enter name of book:")
            if u_book in book:
                if (books[u_book]>0):
                    print("Book Issued Successfully")
                    books[u_book]-=1
                else:
                    print("Book Not Avliable")
            else:
                    print("Book Not Found")        
            print("     ----------      ")
        elif(ch==3):
            u_book=input("Enter book name:")
            if(u_book in book):
                books[u_book]+=1
            else:
                book[u_book]=1
                u_book=1
            print("     ----------      ")
        elif(ch==4):
            print("Good bye")
            print("     ----------      ")
        else:
            print("Invalid choice")
            print("     ----------      ")
books={"Python":5,"C++": 3,"Java": 2,"AI": 4}
lms(books)