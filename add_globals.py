Var = 42

def ask_me() :
      num = int(input("Enter number:"))
      return(num)

def  add(num) :
       return (num  + Var)

def main () :
      number1 = ask_me()
      number2 = ask_me()

      sum = add(number1)
      sum = add(number2)

      print("Sum:," sum)
      print("Global:",  Var) 
