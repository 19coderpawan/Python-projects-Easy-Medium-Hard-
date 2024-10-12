# This is a Simple quiz game in which the user need to answer few question and based on the response he will be
# graded.

print("Welcome to Quiz Game 2024")
consent=input("Would you like to play a game!")

if consent.lower()!="yes":
    quit()

score=0

print("Select the correct option-:")

q1=input('''Q1-:What does AI stand for?
A) Automated Intelligence
B) Artificial Intelligence
C) Advanced Integration
D) Algorithmic Intelligence
-:  ''')

q2=input('''Q2-:Which of the following is a subfield of AI?
A) Machine Learning
B) Data Mining
C) Cloud Computing
D) All of the above
-:  ''')

q3=input('''Q3-:What is the primary goal of machine learning?
A) To create robots
B) To enable computers to learn from data
C) To replace human jobs
D) To enhance computer graphics
-:  ''')

q4=input('''Q4-:Which algorithm is commonly used for classification tasks in machine learning?
A) Linear Regression
B) K-Nearest Neighbors (KNN)
C) Principal Component Analysis (PCA)
D) Gradient Descent
-:  ''')

q5=input('''Q5-:What is a neural network inspired by?
A) Human brain structure
B) Computer hardware
C) Mathematical equations
D) Biological ecosystems
-:  ''')

q6=input('''Q6-:Which of the following is NOT a type of machine learning?
A) Supervised Learning
B) Unsupervised Learning
C) Reinforcement Learning
D) Predictive Learning
-:  ''')

q7=input('''Q7-:What is Natural Language Processing (NLP)?
A) A method for optimizing algorithms
B) The ability of machines to understand and interpret human language
C) A way to enhance computer vision
D) A technique for data storage
-:  ''')

q8=input('''Q8-:Which company developed the AI program Watson that competed on Jeopardy!?
A) Google
B) Microsoft
C) IBM
D) Amazon
-:  ''')

q9=input('''Q9-:What is the Turing Test designed to evaluate?
A) The speed of a computer
B) The intelligence of a machine compared to a human
C) The efficiency of an algorithm
D) The accuracy of data processing
-:  ''')

q10=input('''Q10-:Which AI technique uses a reward system to encourage desired behavior?
A) Supervised Learning
B) Unsupervised Learning
C) Reinforcement Learning
D) Deep Learning
-:  ''')

if q1.lower()=="b":
    score+=1
if q2.lower()=="a":
    score+=1
if q3.lower()=="b":
    score+=1
if q4.lower()=="b":
    score+=1
if q5.lower()=="a":
    score+=1
if q6.lower()=="d":
    score+=1
if q7.lower()=="b":
    score+=1
if q8.lower()=="c":
    score+=1
if q9.lower()=="b":
    score+=1
if q10.lower()=="c":
    score+=1

print(f"You got {score} correct answers")
print(f"Out of 100 % you scored -: {(score/10)*100}%")