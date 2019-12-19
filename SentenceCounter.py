#this function counts ". "s of the string
def dotSpaceCounter(str):
    n=str.count(". ")
    return (n)
#this function counts ". enter"s of the string
def dotEnterCounter(str):
    m=str.count(".\n")
    return (m)

# this is a function that counts the number of sentences
def sentenceCounter(s):
    # number of sentences
    number = dotSpaceCounter(s)
    number = number + dotEnterCounter(s)
    # checking whether the last sentence is counted
    if str.endswith('.'):
        return (number+1)
    else:
        return(number)

# This is a program, which counts the number of sentences in the story.txt file
# opening text file
f = open("story.txt", "r")
# reading text from the file
str = f.read()
# calling for the sentenceCounter method
num = sentenceCounter(str)
# printing counted sentence number
print(num)
f.close()







