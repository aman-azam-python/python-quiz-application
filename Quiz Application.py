score=0
name=input("enter your name = ")
print("--------------")
print("welcome!",name)
print("lets start python quiz!")
questions=[
     { 
        "question":"1. what is the correct extension of a python file ?",
        "options":["a. .cpp","b. .html","c. .py","d. .java"],
        "answer":"c"
    },
    {
        "question":"2. which keyword is used to define a function in python ?",
        "options":["a. function","b. def","c. func","d. define"],
        "answer":"b"
        },
    {   
        "question":"3. which symbol is used for a comment in python ?",
        "options":["a. //","b. /**/","c. #","d. <!---->"],
        "answer":"c"
        },
    {   
        "question":"4. which of the following is a python list ?",
        "options":["a. {1,2,3}","b. (1,2,3)","c. [1,2,3]","d. <1,2,3>"],
        "answer":"c"
        },  
    {   
        "question":"5. which keyword is used to stop a loop ?",
        "options":["a. stop","b. exit","c. break","d. end"],
        "answer":"c"
        }
]
for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer=input("enter your answer = ")
    if answer.lower()==question["answer"]:
        print("correct answer")
        score=score+1
    else:
        print("wrong answer!")
print("-----------------------")
print("Quiz Completed")
print("name = ",name)
print("Your Score = ",score)
print("Total Questions = ",len(questions))
percentage=(score/len(questions))*100
print("Your Percentage = ",round(percentage,2),"%")
if percentage>=80:
    print("Result = Excellent")
elif percentage>=60:
    print("Result = Good")
elif percentage>=40:
    print("Result = Pass")
else:
    print("Result  = Fail!")