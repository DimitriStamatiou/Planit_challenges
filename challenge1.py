#declaring program wide variables
a, b, i, n = 0, 1, 0, 0

# this is so I can insert this question into multiple sercumstances
text = "Which number of the fibinacci sequence would you like to choose? "
# first input request for the user
n = int(input(text))

#checking if n is below 0
if(n <= 0):
    #prints out an error message and tells the user to try again
    print("Invalid Number, Please Provide a positive number")
    n = int(input(text))
#if the number is above 0 it will go through the fibinacci sequence until it hits the number
elif(n > 0):
    #loop until you get the right number
    #I'm doing n-2 here because there was a logical error where it got the next number in the sequence
    while(i <= (n-2)):
        #walking through the entire fibinacci sequence from 0 to infinity
        j = a + b
        a = b
        b = j
        i += 1
    #this is just to make the code more legable and maluable
    text = [str(a), " is the ", str(n)]
    text = ','.join(text)
    text = text.replace(',' ,"")
    #print and exit the program
    if(n == 1):
        print(text, "st number in the fibinacci sequence!")
    elif(n == 2):
        print(text, "nd number in the fibinacci sequence!")
    elif(n == 3):
        print(text, "rd number in the fibinacci sequence!")
    else:
        print(text, "nd number in the fibinacci sequence!")
    exit()
