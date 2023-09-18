#!/usr/bin/env python3
class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count

        # title = Book ("Shannara") 
        # title.Shannara


    def page_count_set(self,page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer") 
    
            
    def get_page_count(self):
        return self._page_count
    
    page_count = property(get_page_count, page_count_set)

    def turn_page(self):

       print("Flipping the page...wow, you read fast!")
