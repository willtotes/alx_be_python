# Object-Oriented Programming in Python

Through this comprehensive OOP project, I've gained hands-on experience with advanced Python concepts that have fundamentally changed how I approach software design. This project challenged me to move beyond basic programming and embrace the powerful paradigms that makes Python an elegant language for building complex applications

---

## What I Learned

### Magic Methods and Python's Special Behaviors

I've learned to harness Python's magic methods to create classes that feel natural and intuitive to use. Working with `__init__`, `__del__`, `__str__`, and `__repr__` taught me how python objects can seamlessly integrate with built-in functions and operators. The Book class I built demonstrates how proper implementation of these methods creates objects that behaves exactly as users expect.

### Inheritance - Building on Solid Foundations

Through implementing the library system, I've mastered how inheritance allows me to create specialized classes while maintaining code reusability. I learned to:
    - Create robust base that serves as blueprints for derived classes.
    - Properly call parent constructors while extending functionality.
    - Design class hierarchies that make logical sense and promote maintainability.
The relationship between **Book**, **Ebook**, and **PrintBook** classes showed me how inheritance models real-world relationships in code.

### Composition - When "Has-A" Beats "Is-A"

The Library class taught me that not all relationships should be inheritance-based. Sometimes composition; where one class contains instances of other classes creates more flexible and maintainable designs. I learned to recognize when to use composition over inheritance and how it leads to cleaner, more modular code.

### Polymorphism - Writing Code That Adapts

Creating the shape calculation system was an eye opening experience in polymorphism. I learned how:
    - Method overriding allows different classes to implement the same interface in their own way.
    - Polymorphism behavior enables me to write code that works with objects regardless of their specific type.
    - The NotImplementedError pattern enforces that subclasses provide their own implementations.
Seeing how the same area() method call could calculate areas for rectangles and circles differently, while being called through the same interface, showed me the true power of polymorphism design.

### Class Methods vs Static Methods

I learned the crucial distinction between `@classmethod` and `@staticmethod` decorations and when to use each. Static methods are utility functions that logically belong to a class but don't need a class or instance data. Class methods access class-level attributes and can modify class state, receiving cls as their first parameter. This knowledge helped me organize code more effectively and choose the right method type for each situation.

---

### OOP's Significance in Professional Development

I discovered why advanced OOP concepts are crucial for enterprise-level software development. These patterns enables building systems that can evolve and scale without breaking existing functionality. Proper inheritance and polymorphism create extensible frameworks that other developers can build upon.

Magic methods make custom classes behave like built-in Python types, improving user experience. Understanding these concepts prepares me for working with popular frameworks like Django and Flask.

---

## Projects I Completed

- `book_class.py` - Magic methods implementations with constructor, destructor and representation methods demonstrating Python's special method system.
- `library_systems.py` - Complete inheritance and composition showcase featuring Base Book class, derived Ebook and PrintBook classes, and a Library class managing collections.
- `polymorphism_demo.py` - Method overriding and polymorphic behavior through Shape base class with Rectangle and Circle implementations showing uniform interfaces.
- `class_static_methods_demo.py` - Clear demonstration of @classmethod and @staticmethod decorations with a Calculator class showing practical usage scenarios.
- `main.py` - Testing scripts demonstrating practical application of all implemented classes and methods.

---

## Tools I used

- Python 3.13+
- VS Code
- Git & GitHub
- Command line interface
- Python's built-in math module

---

## Author

WIll Tsotetsi
GitHub: @willtotes