


Names=[]
x= int(input("enter the number of Names : "))
for i in range(0, x):
    Names.append(input("enter the {}th Name : ".format(i+1)).strip())
Names= sorted(Names)




def Name_to_Name(lst):
    final_lst=[]
    for i in lst:
        new_lst=[]
        new_lst.append(i)
        y=i[-1]                        
        should_restart = True
        while should_restart:
            should_restart = False
            for z in lst:
             if y == z[0] and z not in new_lst:
                    new_lst.append(z)
                    y = z[-1]
                    should_restart = True
                    break       
        if len(new_lst) > len(final_lst):
            final_lst= new_lst            
    return final_lst
        
print(Name_to_Name(Names)  )     









    # should_restart = True  
    # while should_restart == False:    
    #     for z in lst and i in range(0, len(lst)-1):
    #         if i==(len(lst)-1) and p == p:
    #              if y == z[0] and z not in new_lst :
    #                 new_lst.append(z)
    #                 y=z[-1]
    #                 lst=lst.remove(z)
    #                 p+=1
    #              should_restart = True
    #              break
            
    #         elif y == z[0] and z not in new_lst : 
    #                 new_lst.append(z)
    #                 y=z[-1]
    #                 lst=lst.remove(z)
    #                 p+=1
    #         else: break