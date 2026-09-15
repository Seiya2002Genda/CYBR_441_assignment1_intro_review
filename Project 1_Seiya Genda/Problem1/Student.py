# Problem 1
# Step 1: Create a Student Class
class Student:

    # Each instance of this class should have a
    # name, age, and gpa field.
    # Ensure that you create and use the appropriate accessor,
    # mutator, and helper functions.
    __name = None
    __age = None
    __gpa = None

    __front = None
    __back = None
    __next = None
    __previous = None

    def __init__(self, name, age, gpa):
        self.set_name(name)
        self.set_age(age)
        self.set_gpa(gpa)

        self.__front = None
        self.__back = None
        self.__next = None
        self.__previous = None

    # Mutator functions
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gpa(self, gpa):
        self.__gpa = gpa

    # Accessor functions
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gpa(self):
        return self.__gpa

    # Step 2: Implement a Deque
    # Create Student Deque
    def Student_Deque(self):
        self.__front = None
        self.__back = None

    # Push to the front: addFront()
    def addFront(self, student):

        if self.__front is None:
            self.__front = student
            self.__back = student

            student.__previous = None
            student.__next = None
        else:
            student.__previous = None
            student.__next = self.__front
            self.__front.__previous = student
            self.__front = student

    # Push to the back: addBack()
    def addBack(self, student):
        if self.__back is None:
            self.__front = student
            self.__back = student
            student.__previous = None
            student.__next = None
        else:
            student.__previous = self.__back
            student.__next = None
            self.__back.__next = student
            self.__back = student

    # Pop from the front: removeFront()
    def removeFront(self):
        if self.__front is None:
            return None
        student = self.__front
        if self.__front == self.__back:
            self.__front = None
            self.__back = None
        else:
            self.__front = self.__front.__next
            self.__front.__previous = None
        student.__next = None
        student.__previous = None
        return student

    # Pop from the back: removeBack()
    def removeBack(self):
        if self.__back is None:
            return None
        student = self.__back
        if self.__front == self.__back:
            self.__front = None
            self.__back = None
        else:
            self.__back = self.__back.__previous
            self.__back.__next = None
        student.__next = None
        student.__previous = None
        return student

    # Search: search(name) -> returns boolean
    def search(self, name):
        current = self.__front
        while current is not None:
            if current.get_name() == name:
                return True
            current = current.__next
        return False

    # Remove: remove(name) -> returns boolean
    def remove(self, name):

        current = self.__front

        while current is not None:
            if current.get_name() == name:
                # Remove from front
                if current == self.__front:
                    self.removeFront()
                # Remove from back
                elif current == self.__back:
                    self.removeBack()
                # Remove from middle
                else:
                    current.__previous.__next = current.__next
                    current.__next.__previous = current.__previous
                    current.__next = None
                    current.__previous = None
                return True
            current = current.__next
        return False
