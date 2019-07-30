question_list=['q1','q2','q3','q4:','q5']
question_direct_yes=[2,4,4,5]
question_direct_no=[3,5,5,5]
final_question_anwser=["You are not lazy","You are lazy"]

def question(x):
    if x==len(question_list):
        final_question()
        
    else:
        print(question_list[x-1])
        anwser=input("What is your anwser?/n: ")

       
        if anwser=="yes":                          
            print("You have anwsered yes for the question "+str(x)+", please anwser the next question")
            question(question_direct_yes[x-1])
        elif anwser=="no":   
            print("You have anwsered no for the question "+str(x)+", please anwser the next question")
            question(question_direct_no[x-1])
        else:
            print("You have typed in the wrong anwser, please retry!")
            question(x)

def final_question():
    x=len(question_list)
    print(question_list[x-1])
    anwser=input("What is your anwser?/n: ")
    if anwser=="yes":                          
        print("You have anwsered yes for the last question, let's")
        print(final_question_anwser[0])
        exit()
    elif anwser=="no":   
        print("You have anwsered no for the question")
        print(final_question_anwser[1])
        exit()
    else:
        print("You have typed in the wrong anwser, please retry!")
        question(question_list[x])
        



def main():
    print("Hi, this is a quiz, please choose yes or no for the questions!")
    question(1)


main()
