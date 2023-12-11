def user_selection() :
     ans = input ("Enter selection:")
     if ans == "q" :
          return False
     return True

def main() :
     run_me = True
     while run_me:
          run_me = user_selection()
          
if __name__ ==  "__main__":
        main()
