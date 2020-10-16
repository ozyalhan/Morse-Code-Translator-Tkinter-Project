import tkinter as tk
from tkinter import *

import translator as tsl

#Tkinter Development


class TextWithPlaceHolder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

if __name__ == "__main__":
    #Creates the window
    window = tk.Tk()

    #Window Title Sets
    window.title("Morse Code Translator 2020")

    #Screen Resolution Info and Application to Program
    pc_resol_width = window.winfo_screenwidth() 
    #print("pc screen resolution width: "+str(pc_resol_width)) #for debugging only
    pc_resol_height = window.winfo_screenheight()
    #print("pc screen resolution height: "+str(pc_resol_height)) #for debugging only

    #set the window geometry
    #window.geometry("1000x500+50+50") #1000px - 500px + 50 (margin to left) + 50 (margin from top)
    program_width=pc_resol_width//2 #set program width
    program_height=pc_resol_height//2 #set program height
    window.geometry("{}x{}+{}+{}".format(program_width,program_height,program_width//10,program_height//10)) #optimized with screen resolution

    #set the program as resizable
    #window.resizable(False,False) #width and height values are closed to resize


    label_input = tk.Label(
    window,
    text="Input",
    anchor="w",
    padx=5,
    pady=5,
    font=("Open Sans","12","bold")
    )
    #label_input.pack(anchor="ne",fill="x") # fill can be x y both
    #label_input.place(x=0.8,y=0.3)
    label_input.pack(anchor="ne",fill="x")

    placeholder_message = "Type your message here: normal text or Morse code using '.', '-' or '_', separating letters by spaces and words by '/' or '|'." 
    text1 = TextWithPlaceHolder(window, placeholder_message, color="grey") 
    #text1.place(width=program_width,height=program_height/3)
    #text1.pack(anchor="ne",fill="x",expand=1,padx=5,pady=5) #side="left"
    #text1.place(bordermode="outside",height=100,width=100) #side="left"
    text1.pack(anchor="ne",fill="x") #I have the height problem,

    label_output = tk.Label(
    window,
    text="Output",
    anchor="w",
    padx=5,
    pady=5,
    font=("Open Sans","12","bold")
    )
    #label_output.pack(anchor="ne",fill="x",expand=1) # fill can be x y both
    label_output.pack(anchor="ne",fill="x")



    text2 = tk.Text(
    window,
    height=5, 
    width=program_width,
    padx=5,
    pady=5,
    font=("Open Sans","12","normal"),
    )
    text2.configure(state="disabled") #it disable the text for input
    text2.pack()

    def get_data():
        expression = text1.get()
        converted_expression_object = tsl.MorseTranslator(expression)
        converted_expression = (converted_expression_object.morse_translation_func())
        text2.configure(state="normal") #it disable the text for input
        text2.insert(INSERT,converted_expression)
        text2.configure(state="disabled") #it disable the text for input

        #####hatalar hatalar, bekle

    #Convert button
    button_convert = Button( 
        text="Convert",
        command=get_data
    )
    button_convert.pack(anchor="ne",side="left",padx=5,pady=5)


    def exit_func():
        quit()

    #Exit button
    button_exit = Button( 
        text="Exit",
        command=exit_func
    )
    button_exit.pack(anchor="ne",side="left",padx=5,pady=5)


    def clear_text1():
        text1.delete(0,"end")
        TextWithPlaceHolder().put_placeholder() ###################

        text2.configure(state="normal") #it disable the text for input
        text2.delete("1.0","end")
        text2.configure(state="disabled") #it disable the text for input

    #Clear button
    button_exit = Button( 
        text="Clear",
        command=clear_text1
    )
    button_exit.pack(anchor="ne",side="left",padx=5,pady=5)



    window.mainloop()












# #Terminal Program is starting with text bellow, it is writing on the screen only one time
# #########################################################################################
# # print("""....................................................
# # - Morse Code Translation Application -     ozy_csfb
# # ....................................................\n
# # - Write your expression and press the enter!
# # ....................................................\n
# # - Only English letters and numbers can be converted.
# # ....................................................
# # Write you expression please.""")
# #########################################################################################

# #While loop is working for the program as infinite state
# # while True:
# #     expression = tsl.get_expression()

# #     result = tsl.MorseTranslator(expression)
    
# #     print(result.morse_translation_func())

# #     loop_status = tsl.exit_quest()
# #     #This statement check the answer from user. If loop_status is true, loop will break.
# #     if loop_status == True:
# #         break

# #This step for keep the terminal alive after end the while loop.  
# # print("........................")
# # input("For exit press the Enter.")
# #########################################################################################




# #for continuity of the window - it is also important to turn down the program
# mainloop()
