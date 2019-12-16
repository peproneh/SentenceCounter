# This is a program, which counts the number of sentences in the story.txt file
#opening text file
f=open("story.txt", "r")
#reading text from the file
str=f.read()
#counting sentences of the string
num=str.count(". ")
#checking whether the last sentence is counted
if str.endswith('. ') : num
else: num=num+1
#printing counted sentence number
print(num)


