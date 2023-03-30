name=input("What is your name? \n")
questions=[["Who is the father of muslim nation?","Mohammad (S.)","Adam(A.)","Musa(A.)","Ibrahim(A.)",4],
["Who is the Last Messenger  of ALLAH?","Prophet  Mohammad (S.)","Prophet Adam(A.)","Prophet Musa(A.)","Prophet Ibrahim(A.)",1],
["What is the capital city of Saudi Arabia?","Riyadh","Makka","Madina","UAE",1],
]

tk=[100,200,300,400,500,600,700,800,900,1000]
index=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
for i in range(0,len(questions)):
  question=questions[i]

  print(f"\n\nHere is your question for BDT.{tk[i]}\n")

  print(f"\n{index[i]}. {question[0]}")
  print(f"\na.{question[1]}  b. {question[2]}\n")
  print(f"c.{question[3]}  d. {question[4]}\n")

  reply=int(input("Enter your answer:(1-4): "))

  if reply==question[-1]:
   sum+=tk[i]
   print("\n Dear ",name ,f"your answer is correct,Congratulations, you've won Total BDT.{sum}")
  else: 
   print("Wrong answer! ")
   break
