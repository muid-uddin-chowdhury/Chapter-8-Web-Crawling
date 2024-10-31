import csv

field_names = ["Name", "Author", "Publosher", "Price", "Category"]
book1 = ["Computer Programming", "Tamim Shariar Subeen", "Onnorokom Prokashoni", "240.00", "Programming"]
book2 = ["Computer Programming Part 2", "Tamim Shariar Subeen", "Dimik Prokashoni", "250.00", "Programming"]
book3 = ["Learn Programming with Python", "Tamim Shariar Subeen", "Dimik Prokashoni", "200.00", "Programming"]

book_list = [book1, book2, book3]

with open("books.csv", "w") as csvf:
    csv_writer = csv.writer(csvf, delimiter = ',', quotechar = "\"", quoting = csv.QUOTE_MINIMAL)
    csv_writer.writerows(book_list)
   