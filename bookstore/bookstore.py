def create_bookstore(name):
    store = { 'name':name,
              'author':[],
              'book':[]}
    return store

def add_author(bookstore, name, nationality):
    author={'name':name,                    ## create a dict name author, have 3 items
            'nationality':nationality,
            'id':len(bookstore['author'])}   ## instead of adding a counter
    bookstore['author'].append(author)      ## add this dict inside the list author in the bookstore dict
    return author
    
    


def get_author_by_name(bookstore, name):     
    for author in bookstore['author']:      ## look in list author in bookstore 
        if author['name']==name:            ## match author name
            return author                   ## return all author dict 


def get_author_by_id(bookstore, author_id): 
   for author in bookstore['author']:       ## look in list author in dict bookstore
      if author['id']==author_id:           ## match author id
          return author                     ## return all author dict
            


def add_book(bookstore, title, isbn, author_id):
    book = { 'title':title,
            'isbn':isbn,
            'author_id':author_id,
            'id':len(bookstore['book'])}
    bookstore['book'].append(book)
    return book
          


def get_book_by_title(bookstore, title):
    for book in bookstore['book']:
        if book['title']==title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['book']:
        if book['id']==book_id:
            return book


def get_books_by_author(bookstore, author_id):
    all_books_by_author=[]
    for book in bookstore['book']:
        if book['author_id']==author_id:
            all_books_by_author.append(book)
        
    return all_books_by_author
