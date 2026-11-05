import sys
import cviceni6.py function 

def convert_ammount(ammount,currency):
   
    

    pass

if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit()

    ammount = int(sys.argv[1])
    currency = sys.argv[2]

    print(convert_ammount(ammount,currency))