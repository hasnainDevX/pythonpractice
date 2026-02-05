# file = open('data.txt', 'r')
# s1 = file.read()
# print(s1)

# file.close()

# f = open('jj.txt', 'w')
# f.write('hello world')

# # Function to read and write files
# def readWriteFile():
#     with open("data.txt", "r") as f:
#         content =f.read()
#         print(content)
#     with open("newfile.text", "w") as nf:
#         nf.write(content)
#         nf.write("\nFile copied successfully!")
#     print("File operations completed.")
# readWriteFile()

# # Function to append data to a file
# def appendData(): 
#     with open("data.txt", "a") as f:
#         content = "NEW APPENDED CONTENT"
#         f.write("\n", content)

# appendData()

# def appendData2():
#     f = open("data.txt", "a")
#     f.write("\nNEW APPENDED CONTENT")
#     f.close()


# # 3. Write a program that prompts the user for their name. When they respond, write their 
# # name to a file called guest.txt. 
# def writeName():
#     name = input("Enter your name")
#     f = open("guest.txt", "w")
#     f.write(name)
#     f.close()
#     print("Your name has been written")
# writeName()

