class Author:

    all = []

    def __init__(self,name):
        self.name = name
        self.contracts_list = []
    

    def contracts(self):
        return self.contracts_list
    
    def books(self):
        return [contract.book for contract in self.contracts_list]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts_list:
            total += contract.royalties
        return total


class Book:

    all = []

    def __init__(self,title):
        self.title = title
        self.contracts_list = []
        self.author_list = []
    
    def contracts(self):
        return self.contracts_list
    
    def authors(self):
        return self.author_list


class Contract:

    all = []

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.contracts_list.append(self)
        book.contracts_list.append(self)
        Contract.all.append(self)
        book.author_list.append(author)
    
    @classmethod
    def contracts_by_date(cls,date):
        matching = [contract for contract in cls.all if contract.date == date]
        return matching

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,name):
        if isinstance(name,Author):
            self._author = name
        else:
            raise Exception('not valid author')
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,name):
        if isinstance(name,Book):
            self._book = name
        else:
            raise Exception('not valid title')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,name):
        if isinstance(name,str):
            self._date = name
        else:
            raise Exception('not valid date')
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,name):
        if isinstance(name,int):
            self._royalties = name
        else:
            raise Exception('not valid royalties')