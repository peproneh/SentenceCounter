# This is a program, which counts the number of sentences in the story.txt file
#opening text file
f=open("story.txt", "r")
#reading text from the file
str=f.read()
#counting sentences of the string
num=str.count(". ")
num=num+str.count(".\n")
#checking whether the last sentence is counted
if str.endswith('.') : num=num+1
else: num=num
#printing counted sentence number
print(num)


