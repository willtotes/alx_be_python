from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)

    print(repr(my_book))

    del my_book

if __name__ == "__main__":
    main()


from library_system import Book
from library_system import Ebook
from library_system import PrintBook
from library_system import Library

def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = Ebook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ == "__main__":
    main()


from polymorphism_demo import Shape
from polymorphism_demo import Rectangle
from polymorphism_demo import Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()


from class_static_methods_demo import Calculator

def main():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()