# Enter rowss

rows = int(input("Enter The Number Of rowss = ")) #enter rowss

for i in range(0, rows): #loop goes from 0 to entered ( rows ) input

    for j in range(0, rows-i-1): #need 1 less than the rows (rows-1) for adding space

        print(" ", end = "") #space character enterd & end = is used to get all in one line

    for j in range(0, i + 1): #starting of the loop

        print("* ", end= "") #star needed to be print

    print() #print used for pyramid shape

