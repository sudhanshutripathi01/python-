#practicing nested lsits 
rows=int(input("Enter the number of rows:"))
cls=int(input("Enter the number of columns :"))
matrix=[]
for i in range(rows):
    list1=[]
    for k in range(cls):
        value=list(input(f"enter the value of ({i},{k})"))
        list1.append(value)
        
        
    matrix.append(list1)
    
print(matrix)
        