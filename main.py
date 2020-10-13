#This dictionary contains equivalent letters to the morse code. White space " " defined as "/" as equivalent of breaks for between the words.
morse_dict={
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    " ":"/",
}

#This fuction get input from the user.
def get_expression():
    # expression is getting from user with lower characters and rstrip removes white spaces in the end if its necessary.
    get_expression_str = input("").lower().rstrip()   
    return get_expression_str

#This function check user that wants to work with program or not, It is not connected with the class MorseTranslator
def exit_quest():
    exit_status = False # if it is True, program will end
    check_exit = input("Do you want to translate morse again?(y/n) ").lower()
    if(check_exit == "y" or check_exit == "yes" ):
        print("Write you expression please.")
        pass 
    elif(check_exit == "n" or check_exit == "no"):
        print("Thank you and goodbye.")
        exit_status = True    
    else:
        print("Your answer is not valid.")
        exit_quest() #with wrong answer exit_quest() function will work again
    return exit_status

#Changing code for OOP, we get the results from class methods
class MorseTranslator:
    def __init__(self,user_expression):
        self.user_expression = user_expression
    
    #Main translation function
    def morse_translation_func(self):
        morse_expression =  ''  # morse_expression is final expression (morse)

        #In this loop we get every character from expression string and convert them to morse value which is matched on morse_dict dictionary.
        for i in self.user_expression:
            if i in morse_dict:
                morse_expression = morse_expression + morse_dict[i] + " " #string concatenation
                #print(morse_dict[i]) #for debugging only

        # morse_expression[:-1] it saves us from whitespace in end.
        morse_expression = morse_expression[:-1]    #morse_expression.rstrip(" ") #it doesnt work here, new solution is done

        #print(morse_expression) #for debugging only
        return morse_expression 


#Terminal Program is starting with text bellow, it is writing on the screen only one time
#########################################################################################
print("""....................................................
- Morse Code Translation Application -     ozy_csfb
....................................................\n
- Write your expression and press the enter!
....................................................\n
- Only English letters and numbers can be converted.
....................................................
Write you expression please.""")
#########################################################################################

#While loop is working for the program as infinite state
while True:
    expression = get_expression()

    result = MorseTranslator(expression)
    
    print(result.morse_translation_func())

    loop_status = exit_quest()
    #This statement check the answer from user. If loop_status is true, loop will break.
    if loop_status == True:
        break

#This step for keep the terminal alive after end the while loop.  
print("........................")
input("For exit press the Enter.")
#########################################################################################        

    



