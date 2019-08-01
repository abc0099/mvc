question_list=['四隻雞與三隻兔子關在同一籠子中，請問籠中共有幾隻腳？','雞兔28隻，102隻腳，則兔有幾隻？','大月有31日，小月有30日，那麼一年中幾個月有28日？','醫生給你3個藥丸，要你每30分鐘吃1個，這些藥丸多久後會被吃完？']#questions are stored in here

question_direct_correct=[3,3,4]#If you are correct with q1, you will jump onto q3
question_direct_incorrect=[2,3,4]#If you are not correct with q1, you need to do q2 too
final_question_anwser=["You are great","Please work hard"]
final_question_number=[4]#adding the number of final question here
question_anwser_select=[[14,16,18,20],[25,24,23,26],[2,1,9,12],[20,40,60,90]]
question_correct_anwser=[4,3,4,3]


def question(x, score):
    for y in final_question_number:
        if x==y:
            final_question(y, score)
            break;#after final_question the quiz is finished
        
        else:
            print(question_list[x-1])
            print("Choice:")
            y=1
            for z in question_anwser_select[x-1]:
                print(str(y)+". "+str(z))
                y+=1

            anwser=int(input("What is your anwser?(please type the int for the choice): "))
            
            
            if isinstance(anwser, int)and 0<anwser<5:    
                if anwser==question_correct_anwser[x-1]:                          
                    print("Your anwser is correct, please anwser the next question")   
                    score=score+1                     
                    print("Your score now is "+str(score))                 
                    question(question_direct_correct[x-1], score)
                
                    
                else:   
                    print("Your anwser is wrong, please anwser the next question")
                    print("Your score now is "+str(score))
                    question(question_direct_incorrect[x-1], score)
                
                    
            
            else:
                print("You have typed in the wrong anwser, please retry!")
                question(x, score)

def final_question(x, score):
    print(question_list[x-1])
    print("Choice:")
    y=1
    for z in question_anwser_select[x-1]:
        print(str(y)+". "+str(z))
        y+=1

    anwser=int(input("What is your anwser?(please type the int for the choice): "))
            
    
    if isinstance(anwser, int) and 0<anwser<5:    
        if anwser==question_correct_anwser[x-1]:                          
            print("Your anwser is correct, this is the last question")
            score=score+1
            print("Your score is "+str(score))
        else:   
            print("Your anwser is wrong, this is the last question")
            print("Your score is "+str(score))
    else:
        print("You have typed in the wrong anwser, please retry!")
        question(x, score)
       


        



def main():
    print("Hi, this is a quiz, please choose the number of the choice for the questions!")
    question(1, 0)


main()
