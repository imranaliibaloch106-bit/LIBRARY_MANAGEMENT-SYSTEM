import database

def main():
    database.connect()
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            database.insert(title, author, year)
            print("✅ Book added successfully!")

        elif choice == '2':
            books = database.view()
            print("\n--- All Books ---")
            for b in books:
                print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Year: {b[3]}, Status: {b[4]}")

        elif choice == '3':
            title = input("Search by title: ")
            author = input("Search by author: ")
            year = input("Search by year: ")
            results = database.search(title, author, year)
            print("\n--- Search Results ---")
            for r in results:
                print(f"ID: {r[0]}, Title: {r[1]}, Author: {r[2]}, Year: {r[3]}, Status: {r[4]}")

        elif choice == '4':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new year: ")
            status = input("Enter status (Available/Borrowed): ")
            database.update(book_id, title, author, year, status)
            print("✅ Book updated successfully!")

        elif choice == '5':
            book_id = int(input("Enter book ID to delete: "))
            database.delete(book_id)
            print("🗑️ Book deleted successfully!")

        elif choice == '6':
            book_id = int(input("Enter book ID to borrow: "))
            database.borrow_book(book_id)
            print("📚 Book borrowed!")

        elif choice == '7':
            book_id = int(input("Enter book ID to return: "))
            database.return_book(book_id)
            print("📗 Book returned!")

        elif choice == '8':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
