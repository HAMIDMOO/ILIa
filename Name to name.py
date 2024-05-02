

"""
in this script we get the names of the game from players and pour then in a list.

[13] Names= sorted(Names)
this code sort Names by alphabetical word.
"""
Names=[]
input_string = input()
Names = input_string.split(", ")
Names.sort()
"""
in this function first we create an empty list(final_lst) to acces to biggest sequence of Names.
then we loop over the Name list to select the first Name then add that to new_lst.
then we loop to elemets by while anf for loops to find the specifce Name that we need.
in end we test the new_lst if its element has mor than final_lst we pour element of new_lst to final_lst.
and return the final_lst  
"""
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
        
x=Name_to_Name(Names) 
print(', '.join(x[0:]))





