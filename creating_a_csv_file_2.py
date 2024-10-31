import csv

field_names = ["Name", "Author", "Publisher", "Price"]
book1 ={"Name": "Computer Programming", "Author": "Tamim Shariar Subeen", "Publisher": "Onnorokom Prokashoni", "Price": "240.00"}
book2 = {"Name": "Computer Programming Part 2", "Author": "Tamim Shariar Subeen", "Publisher": "Dimik Prokashoni", "Price": "250.00"}
book3 = {"Name": "Learn Programming with Python", "Author": "Tamim Shariar Subeen", "Publisher": "Dimik Prokashoni", "Price": "200.00"}

book_list = [book1, book2, book3]

with open("books2.csv", "w") as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)
   