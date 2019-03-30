import random, string

def import_names(name_file):
    try:
        with open(name_file, 'r') as f_open:
            names = f_open.readlines()
            name_list = [x.strip() for x in names]
    except:
        print("name file not found\n")
    return  name_list

def namegetter(firstnames, lastnames, count):
        for i in range(0,count):
            first_name = random.choice(firstnames)
            last_name = random.choice(lastnames)
            rtn_name = first_name + ' ' + last_name
            print(rtn_name)

def main():
    input_m_first_name = 'maleNAMES.txt'
    input_f_first_name = 'femaleNAMES.txt'
    input_last_name = 'lastNAME.txt'

    while True:
        first_names = []
        last_names = []
        print("\n**********************************************\nLet's generate a random Male or Female name.")
        answer = input("Please answer 'M' or 'F' or Press 'Q' to quit.\n**********************************************\n")
        answer = answer.upper()
        if answer in ('M', 'F'):
            if answer == 'M':
                first_names = import_names(input_m_first_name)
                print("\n")
            elif answer == 'F':
                first_names = import_names(input_f_first_name)
                print("\n")
            last_names = import_names(input_last_name)
        elif answer == 'Q':
            print("\nGoodbye!")
            break
        else:
            print("Input must be 'M' or 'F' to select a Male or Female name or 'Q' to quit.\n")
            continue

        count = 0
        while True:
          try:
             count = int(input("How many names do you want? "))
             print("\n")
          except ValueError:
              print("Input must be an integer!\n")
              continue
          if count < 1:
              print("Input must be a positive number!\n")
          else:
              print("#########################")
              namegetter(first_names, last_names, count)
              print("#########################\n")
              break
main()
