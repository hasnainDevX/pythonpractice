# Qno: 01                                                                                                                                                      
# Write a program that simulates how websites ensure that everyone has a unique username• Make 
# a list of five or more usernames called current_users.• Make another list of five usernames called 
# new_users. Make sure one or two of the new usernames are also in the current_users list. • Loop 
# through the new_users list to see if each new username has already been used. If it has, print a 
# message that the person will need to enter a new username. If a username has not been used, print 
# a message saying that the username is available. • Make sure your comparison is case sensitive. If 
# 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.


# current_users = ["hasnain", "mughal", "hamza", "rohan", "nigga"]
# new_users = ["haSnain", "chnagezkhan", "rafay", "bhencho", "nigga"]
# current_users_copy = [user.lower() for user in current_users]

# for user in new_users:
#     if user.lower() in current_users_copy:
#         print("username already taken")
#     else:
#         print("username available")

# Qno: 02      
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a 
# dictionary of information about each city and include the country that the city is in, its approximate 
# population, and one fact about that city. The keys for each city’s dictionary should be something 
# like country, population, and fact. Print the name of each city and all of the information you have 
# stored about it. 


# cities = {
#     "Karachi": {
#         "population": "2.5million",
#         "fact": "biggest city",
#         "country": "Pakistan"
#     },
#     "Toronto": {
#         "population": "1.1million",
#         "fact": "favourite city",
#         "country": "Canada"
#     },
#     "Islamabad": {
#         "population": "0.85million",
#         "fact": "capital city",
#         "country": "Pakistan"
#     },
# }

# for city, info in cities.items():
#     print(f"City: {city}")
#     for key, value in info.items():
#         print(f"  {key.capitalize()}: {value}")


# Qno: 03 
# A college library maintains a record of book ID numbers using a tuple in Python to keep the data 
# secure and unchanged by default. First, the librarian enters the total number of books and inputs 
# each book ID, and the system stores these values in a tuple and displays the original list along with 
# their index positions. Since tuples are immutable, the program converts the tuple into a list to 
# perform modifications. When new books arrive, a new book ID is inserted at a specific index 
# position (for example, index 2), and the system displays the updated tuple along with the index 
# where the insertion occurred. If some books are removed due to damage or outdated editions, a 
# book ID is deleted from a given index position (such as index 4), and the system shows the 
# updated tuple and the index from which the value was removed. Additionally, if an incorrect book 
# ID is detected, the librarian updates the book ID at a particular index (for example, index 1), 
# and the program displays the modified tuple while clearly mentioning the index where the updation 
# took place. This approach helps the library manage book records efficiently while keeping track 
# of all changes using index values.

# total_books = int(input("Enter total number of books: "))
# book_ids = []

# for i in range(total_books):
#     book_id = input(f"Enter book ID {i + 1}: ")
#     book_ids.append(book_id)
# book_ids_tuple = tuple(book_ids)
# print("Original book IDs and their index positions:")
# for book_num, book_id in enumerate(book_ids_tuple):
#     print(f"{book_num + 1} : {book_id}")

# new_books = int(input("Enter total number of new books: "))
# for i in range(new_books):
#     book_index = int(input("Enter New Book Index: "))
#     book_id = input(f"Enter book ID {book_index}: ")
#     book_ids.insert(book_index, book_id)
# book_ids_tuple = tuple(book_ids)

# print("Original book IDs and their index positions:")
# for book_num, book_id in enumerate(book_ids):
#     print(f"{book_num + 1} : {book_id}")

# removed_books = int(input("Enter total number of removed books: "))
# for i in range(removed_books):
#     book_index = int(input("Enter Removed Book Index: "))
#     book_ids.pop(book_index)
# book_ids_tuple = tuple(book_ids)

# print("Original book IDs and their index positions:")
# for book_num, book_id in enumerate(book_ids):
#     print(f"{book_num + 1} : {book_id}")

# updated_books = int(input("Enter total number of updated books: "))
# for i in range(updated_books):
#     updated_book = int(input("Enter index of updated book: "))
#     book_ids[updated_book] = input(f"Enter updated book ID for index {updated_book}: ")
# book_ids = tuple(book_ids)

# print("Original book IDs and their index positions:")
# for book_num, book_id in enumerate(book_ids):
#     print(f"{book_num + 1}: {book_id}")


# Qno: 04 
# A school is organizing a fun quiz competition and wants to select students randomly for 
# different activities. The Python program uses the random module to make selections fair and 
# unpredictable. First, the teacher enters the names of all participating students. The system uses 
# random.choice() to select a single student randomly to answer a question. To randomize the order 
# of students for games or presentations, the program uses random.shuffle() on the list of student 
# names. For some mini-games, the system generates random numbers using random.randint() to 
# simulate dice rolls or points scoring. This ensures the quiz and games are exciting, fair, and 
# unpredictable, giving every student an equal chance to participate. 


# import random 
# students = []
# total_students = int(input("Enter total number of students: "))
# for std in range(total_students):
#     student_name = input("ENTER NAME OF THE STUDENT")
#     students.append(student_name)
# random.shuffle(students)
# selected_student = random.choice(students)
# print(students)
# print(selected_student)
# random_number = random.randint(1, 6)
# print(f"Random number generated: {random_number}")


# Qno: 05 
# A college wants to manage and format its course information using a Python program. The system 
# allows the user to enter the course name and department name and displays them in a readable 
# format. The program applies the title() function to the course name so that the first letter of each 
# word is capitalized, and the capitalize() function to the department name to ensure only the first 
# letter is uppercase. If the course name contains a mistake, the program allows the user to enter an 
# old name and a new name, and uses the replace() function to update the course name. 
# Additionally, the program extracts specific parts of the course name using string slicing with 
# index values: the first two characters (index 0 to 1) are extracted as the course code, characters 
# from index 1 to 4 are extracted as a verification part, and the last three characters (using negative 
# indexing, -3 to end) are extracted as the course ID. Finally, the program displays the updated 
# course name along with the course code, course ID, and verification part.

# totalnumofCourses = int(input('enter total number of courses'))
# courses = []
# for i in range(totalnumofCourses):    
#     course_name = input("Enter course name").title()
#     dep_name = input("Enter Department name").capitalize()
#     courses.append((course_name, dep_name))
#     print(courses)
#     print(f"Course Name: {course_name}")
#     print(f"Department Name: {dep_name}")
#     correction = input("Do you want to correct the course name? (yes/no)").lower()
#     if correction == 'yes':
#         old_name = input("Enter old course name: ").title()
#         new_name = input("Enter new course name: ").title()
#         course_name = course_name.replace(old_name, new_name)
#         print(f"Updated Course Name: {course_name}")
#     course_code = course_name[0:2]
#     verification_part = course_name[1:4]
#     course_id = course_name[-3:]  # Extract last three characters using negative indexing
#     print(f"Course Code: {course_code}")
#     print(f"Verification Part: {verification_part}")
#     print(f"Course ID: {course_id}")
#     print("-----------------------------")


# Qno: 06 
# A school administration system uses a Python program to manage student records using file 
# handling. When a new academic session starts, the system creates a text file named students.txt 
# to store student details such as roll number, name, and class. The administrator enters student 
# information, and the program opens the file in write mode to save these details permanently. 
# Whenever the administrator wants to view the stored records, the file is opened in read mode, and 
# all student data is displayed on the screen. If new students are admitted later, the program opens 
# the same file in append mode so that new records are added without deleting the existing data.


total_students = int(input("Enter Total Number of Students: "))
file = open("students.txt", "w")
std_info = []
for i in range(total_students):
    student_name = input("Enter Student Name: ")
    student_rollNo = input("Enter Student Roll No: ")
    std_info.append(student_name)
    std_info.append(student_rollNo)
    file.write(f"{std_info}\n")
print(std_info)
file.close()

