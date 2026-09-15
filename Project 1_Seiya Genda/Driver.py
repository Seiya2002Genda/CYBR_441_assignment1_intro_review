from Problem1.Student import Student
from Problem2.binary_search_tree import Node, BinarySearchTree

def main():

    # Create a new student
    getName = input("Enter the name of the student: ")
    getAge = input("Enter the age of the student: ")
    getGPA = input("Enter the GPA of the student: ")
    student = Student(getName, getAge, getGPA)
    print(student.get_name())
    print(student.get_age())
    print(student.get_gpa())

    # Create a new node
    node = Node(50)

    print("\nNode Test")
    print("Payload:", node.get_payload())
    print("Left:", node.get_left())
    print("Right:", node.get_right())


    # Test Student Deque
    print("\nStudent Deque Test")

    student.Student_Deque()

    student2 = Student("John", 20, 3.5)
    student3 = Student("Emma", 21, 3.8)
    student4 = Student("Mike", 22, 3.2)

    student.addFront(student2)
    student.addBack(student3)
    student.addBack(student4)

    print("Search John:", student.search("John"))
    print("Search Emma:", student.search("Emma"))
    print("Search Alex:", student.search("Alex"))

    removedFront = student.removeFront()

    if removedFront is not None:
        print("Removed from front:", removedFront.get_name())

    removedBack = student.removeBack()

    if removedBack is not None:
        print("Removed from back:", removedBack.get_name())

    print("Remove Emma:", student.remove("Emma"))
    print("Search Emma:", student.search("Emma"))


    # Test Binary Search Tree
    print("\nBinary Search Tree Test")

    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Search 40:", tree.search(40))
    print("Search 100:", tree.search(100))

    print("\nTree Traversals")
    tree.Traversal()

    print("\nDelete 30")
    tree.delete(30)

    print("\nTree After Deletion")
    tree.Traversal()


if __name__ == '__main__':
    main()