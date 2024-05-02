
Names=[]
x= int(input("enter the number of Names : "))
for i in range(0, x):
    Names.append(input("enter the {}th Name : ".format(i+1)).strip())
Names= sorted(Names)





def Name_to_Name(lst):
    final_lst=[]
    new_lst=[]
    for i in lst:
        
        new_lst.append(i)
        y=i[-1]                        
        while should_restart:
            should_restart = False
            for z in lst:
             if y == z[0] and z not in new_lst:
                    new_lst.append(z)
                    y = z[-1]
                    should_restart = True
                    break
             

print(Name_to_Name(Names))               