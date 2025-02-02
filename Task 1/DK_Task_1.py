# Importing packages

import requests
import pandas as pd
from datetime import datetime


# Defining Contstants

URL = "https://raw.githubusercontent.com/dk-books/tech-interview/refs/heads/main/ae/books.json"
nonfiction_hobbies_books = []


# HTTP Request

book_data_req = requests.get(URL)


# Checking the response status code is OK

if book_data_req.status_code in (200, '200'):
    book_data = book_data_req.json()


    # Looping over the response to create a new list with 'Hobbies' and 'Nonfiction' category books

    for i in range(0, len(book_data)):
        book_data_temp = book_data[i]
        categories = book_data_temp['categories']
        if "Hobbies" in categories or "Nonfiction" in categories:


            # Checking release year and increasing price by 20%

            publication_date = book_data_temp['publication_date']
            release_year = datetime.strptime(publication_date, '%Y-%m-%d').date().year

            if release_year > 2020:
                new_price = book_data_temp['price']*1.2
                book_data_temp.update({'price': new_price})
            
            nonfiction_hobbies_books.append(book_data_temp)


    df = pd.DataFrame(nonfiction_hobbies_books)

    # Formatting Data Frame for readability

    df['categories'] = df['categories'].apply(lambda x: '; '.join(x))    # Separating multiple categories with a semicolon
    df['price'] = df['price'].apply(lambda x: '£' + f'{x:.2f}')    # Adding a pound sign to the front of the price, and displaying 2 decimal places
    df.columns = df.columns.str.replace('_', ' ').str.title()    # Replacing underscores with spaces and capitalising first letters in column headings
    df.rename(columns={'Isbn': 'ISBN'}, inplace=True)    # Capitalising the ISBN heading
    df.rename(columns={'Image Url': 'Image URL'}, inplace=True)    # Capitalising URL in the Image URL heading


    # Save as CSV

    df.to_csv("Task 1/Hobby and Nonfiction Books.csv", index=False)

else:

    print("Request not completed")