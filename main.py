import translator as tsl

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
    expression = tsl.get_expression()

    result = tsl.MorseTranslator(expression)
    
    print(result.morse_translation_func())

    loop_status = tsl.exit_quest()
    #This statement check the answer from user. If loop_status is true, loop will break.
    if loop_status == True:
        break

#This step for keep the terminal alive after end the while loop.  
print("........................")
input("For exit press the Enter.")
#########################################################################################