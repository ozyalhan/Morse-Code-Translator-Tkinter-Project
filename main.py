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

print("""....................................................
- Morse Code Translation Application -     ozy_csfb
....................................................\n
- Write your expression and press the enter!
....................................................\n
- Only English letters and numbers can be converted.
....................................................""")

# expression is getting from user with lower characters.
expression = input("").lower()   

# morse_expression is final expression (morse)
morse_expression =  '' 

#print("first expression: " + expression) #for debugging only

#In this loop we get every character from expression string and convert them to morse value which is matched on morse_dict list.
for i in expression:
    if i in morse_dict:
        morse_expression = morse_expression + morse_dict[i] + " " #string concatenation
        #print(morse_dict[i]) #for debugging only

# morse_expression[:-1] it saves us from whitespace in end.
morse_expression = morse_expression[:-1]    #morse_expression.rstrip(" ") #it doesnt work here, new solution is done

print(morse_expression) #for debugging only
input("Press Enter for Exit.")


