#getting the user's input and cleaning it up
inp = input("Input: ")
inp = inp.replace(" ", "")
inp = inp.lower()

#some variables to do the actual searching
letterList = {}
big = 0
tie = False

#looping through all the letters in the input
for i in inp:
    #if it's in the letter list already, add 1 to it
    if(i in letterList):
        letterList[i] += 1
    #if it's not in the letter list, just make it 1
    else:
        letterList[i] = 1
    
    #if the letter has occored the most, save the value for later and set the tie variable to false
    if(letterList.get(i) > big):
        big = letterList.get(i)
        tie = False
    #if it's tied for the most frequent letter, then just set tie to true
    elif(letterList.get(i) == big):
        tie = True

#settingup the output to be output to te user's screen
text = "Output: "
char = ""

#if there's no tie, find the most frequent letter in the string
if(tie == False):
    for letter, freq in letterList.items():
        if(freq == big):
            char = letter
    print(text, char)
#if there is a tie, just get the first letter of the string
elif(tie == True):
    char = inp[:1]
    print(text, char)


