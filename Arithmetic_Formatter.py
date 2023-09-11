def arithmetic (problems,yesorno):
    topline=""
    bottomline=""
    dashline=""
    result=""
    firstnum=""
    secondnum=""
    operator=""
    sum=""
    
    if len(problems)>5:
        print ("Error: Too Many Problems.")
    
    else:
        for equation in problems:
            
            try:
                eqvar = equation.split()
                firstnum=int(eqvar[0])
                secondnum=int(eqvar[2])
                operator=eqvar[1]
                
            except:
                return "Error: Numbers must only contain digits"
    
            length=max(len(str(firstnum)),len(str(secondnum)))

            if operator!="+" and operator!="-":
                return "Error: Operator must be \"+\" or \"-\""
                
            elif len(str(firstnum))>4 or len(str(secondnum))>4:
                return "Numbers cannot be more than 4 digits"
                
            else:
                if operator=="+":
                    sum=firstnum + secondnum
                elif operator=="-":
                    sum=firstnum-secondnum

                topline=topline + str(firstnum).rjust(length+2)
                bottomline=bottomline + operator + str(secondnum).rjust(length+1)
                result= result + str(sum).rjust(length+2)
                for index in range(length+2):
                    dashline+="-"
                
                if equation!=problems[-1]:
                    topline+="    "
                    bottomline+="    "
                    dashline+="    "
                    result+="    "
        
        if yesorno.lower()=="y":
            return topline+"\n"+bottomline+"\n"+dashline+"\n"+result
        else:
            return topline+"\n"+bottomline+"\n"+dashline
resume = True
equations = list()

while resume == True:
    statement = input("Enter numbers: \n")
    equations.append(statement)
    cont = input ("Continue? y/n: ")
    if cont.lower() == "y":
        continue
    elif cont.lower() == "n":
        resume=False
    else:
        print ("Invalid Input. Defaulting to n")
        resume=False
statementanswer = input ("Show answer? Y/N? \n")

print(arithmetic(equations,statementanswer))