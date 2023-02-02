import math
import random
import text_encryption_function


def copy_text_file(in_file,out_file):
    out_file = open(out_file,"x")
    in_file = open(in_file)
    out_file.write(in_file.read())

#copy_text_file("namn.csv","my_copy.csv")

def encrypt_file(in_file, out_file):
    out_file = open(out_file,"x")
    in_file = open(in_file)
    in_file_e = text_encryption_function.encrypt(in_file.read())
    out_file.write(in_file_e)

#encrypt_file("namn.csv", "secret_names.csv")

def user_dialogue():
    out_file = input("Name of new encrypted file:")
    while(True):
        try:
            in_file = input("Name of file to be encrypted:")
            file = open(in_file)
            break
        except:
            print("That resulted in an input/output error, please try again! Details:FileNotFoundError(2, 'No such file or directory')")
        
    encrypt_file(in_file, out_file)
    print("Encryption complete!")  

def get_int_input(prompt_string):
    while(True):
        try:
            i = int(input(prompt_string))
            break
        except:
            print("ange ett heltal")
    return i
short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']]

def run_quiz(quiz_list_of_lists):
    print("----------------------------------------")
    print("Hello and welcome to the quiz!")
    print("----------------------------------------")
    for q in quiz_list_of_lists:
        c_answer = q[1]
        print(q[0])
        q.pop(0)
        random.shuffle(q)
        for i in range(0,len(q)):
            print("Alternativ:",(i+1),end=" ")
            print(q[i], end=" ")
        print()
        prompt_string = "Vilket är ditt svar? "
        prompt_string += "( "
        for i in range(0,len(q)):
            prompt_string += str(i+1)+ " "
        prompt_string += ")"
        answer = get_int_input(prompt_string)
        if(q[answer-1] == c_answer):
            print("Rätt, det är: "+c_answer)
        else:
            print("Fel,Rätt svar är "+c_answer)

#run_quiz(short_quiz_list_of_lists)

def get_quiz_list_handle_exceptions():
    in_file = input("Name of quiz file:")
    in_file = open(in_file)
    file_list = in_file.read()
    quiz_list = []
    for i in range(0,len(file_list)-1):
        quiz_list.append(file_list[i].split(";"))
    print(file_list)
            
        
            
            
get_quiz_list_handle_exceptions()
#WTF CRINGe
a = [1,2,3]
b  = a
b[2] = 1
print(a)