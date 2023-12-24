# used mainly for randomizing the questions
import random

def compare_coeff1(user_coeff):
  #correct coefficients for problem 1
  c_problem1 = [4, 1, 2]
  #interating through each one of the three element in the c_problem1 list
  for i in range(len(c_problem1)):
    #compares to each element in the user_coeff list to see whether it's a match
    if c_problem1[i] != user_coeff[i]:
      return False
  return True

#following functions carry out the same procedure as the compare_coeff1 function but for the other equations/problems 
def compare_coeff2(user_coeff):
  c_problem2 = [1,5,1]
  for i in range(len(c_problem2)):
    if c_problem2[i] != user_coeff[i]:
      return False
  return True

def compare_coeff3(user_coeff):
  c_problem3 = [2,1,1]
  for i in range(len(c_problem3)):
    if c_problem3[i] != user_coeff[i]:
      return False
  return True 

# a function that allows the scientific equations to have subscripts; code obtained from GeeksforGeeks
def get_sub(x):
  normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
  sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
  res = x.maketrans(''.join(normal), ''.join(sub_s))
  return x.translate(res)

# setting subscripts for each equation 
problem_1 = "Na" + " +" + " O{}".format(get_sub('2')) + "→" + " Na{}O{}".format(get_sub('2') ,get_sub(''))
#problem 1: Na + O2 → Na2O

problem_2 = "P{}".format(get_sub('4')) + " +" " O{} ".format(get_sub('2')) + "→" + " P{}O{}".format(get_sub('4') ,get_sub('10'))                                                
#problem 2: P4 + O2 → P4O10

problem_3 = "Li" + " +" + " S" + " →" + " Li{}" .format(get_sub('2') + "S")
#problem 3: Li + S → Li2S

# using increment system to determine when the program stops, increases by 1 each time "Yes" is entered by user 
user_continue = 0
#list that carries the problems that will be generated
problems = [problem_1, problem_2, problem_3]

while user_continue <= 2 and user_continue >= 0:
  #used to randomize the questions 
  random_problems = random.choice(problems)

  # user enters their answers and answers are appended in user_coeff list
  print("Your equation is: " + str(random_problems))
  print()
  #empty list that would store the user coefficients 
  user_coeff=[]
  u_coeff1 = int(input("What is the coefficient for 1st element? "))
  user_coeff.append(u_coeff1)
  print()
  u_coeff2 = int(input("What is the coefficient for 2nd element? "))
  user_coeff.append(u_coeff2)
  print()
  u_coeff3 = int(input("What is the coefficient for the solution? "))
  user_coeff.append(u_coeff3)
  print("Your answer:" + str(user_coeff))
  print()

  #calling the functions 3 separate times for each question that compare the user coefficients and correct coefficients and allowing user to try again if function returns false

  #once the user enters correct answers, the problem generated is removed from the problems list
  if random_problems == problem_1:
    result1 = compare_coeff1(user_coeff)
    while result1 == False:
      print("Your answer is " + str((result1)) + "." + " Please try again!\n")
      user_coeff.clear()
      u_coeff1 = int(input("What is the coefficient for 1st element? "))
      user_coeff.append(u_coeff1)
      print()
      u_coeff2 = int(input("What is the coefficient for 2nd element? "))
      user_coeff.append(u_coeff2)
      print()
      u_coeff3= int(input("What is the coefficient for the solution? "))
      user_coeff.append(u_coeff3)
      print()
      result1 = compare_coeff1(user_coeff)
    print("Your answer is " + str((result1)))
    if result1 == True:
      problems.remove(problem_1)


  if random_problems == problem_2:
    result2 = compare_coeff2(user_coeff)
    while result2 == False:
      print("Your answer is " + str((result2)) + "." + " Please try again!\n")
      user_coeff.clear()
      u_coeff1 = int(input("What is the coefficient for 1st element? "))
      user_coeff.append(u_coeff1)
      print()
      u_coeff2 = int(input("What is the coefficient for 2nd element? "))
      user_coeff.append(u_coeff2)
      print()
      u_coeff3= int(input("What is the coefficient for the solution? "))
      user_coeff.append(u_coeff3)
      print()
      result2 = compare_coeff2(user_coeff)
    print("Your answer is " + str((result2)))
    if result2 == True:
      problems.remove(problem_2)


  if random_problems == problem_3:
    result3 = compare_coeff3(user_coeff)
    while result3 == False:   
      print("Your answer is " + str((result3)) + "." + " Please try again!\n")
      user_coeff.clear()
      u_coeff1 = int(input("What is the coefficient for 1st element? "))
      user_coeff.append(u_coeff1)
      print()
      u_coeff2 = int(input("What is the coefficient for 2nd element? "))
      user_coeff.append(u_coeff2)
      print()
      u_coeff3= int(input("What is the coefficient for the solution? "))
      user_coeff.append(u_coeff3)
      print()
      result3 = compare_coeff3(user_coeff)
    print("Your answer is " + str((result3)))
    if result3 == True:
      problems.remove(problem_3)

  print()
  #allows user to try different problems
  user_opinion = str(input("Would you like a different equation? Yes or No?: "))
  print()
  if user_opinion == "Yes" or user_opinion == "yes":
      user_continue += 1
  elif user_opinion == "No" or user_opinion == "no":
      user_continue += 3
      print("Thank you for playing! ")
  #allows the user to reenter a valid input, if they make a mistake the first time
  while user_opinion != "Yes" and user_opinion != "yes" and user_opinion != "no" and user_opinion != "No": 
    user_opinion = input("Please enter a valid response. Would you like a different equation? Yes or No?: ")
    user_continue += 0
    if user_opinion == "Yes" or user_opinion == "yes":
      user_continue += 1
    elif user_opinion == "No" or user_opinion == "no":
      user_continue += 3
      print("Thank you for playing! ")

  #once the problems list is empty, program ends 
  if problems == []:
    print("No more practice needed! Good luck! ")





'''
# here are the correct answers:
Na + O2 → Na2O = [4,1,2] 
P4 + O2 → P4O10 = [1,5,1] 
Li + S → Li2S = [2,1,1]
'''