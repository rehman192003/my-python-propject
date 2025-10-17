table_number=int(input("Enter Number of which table you want"))
end_number=int(input("Enter the number where you want to stop your table:"))
for i  in range(end_number):
    if(i+1>10):
        break
    print(table_number," x ",i+1,"=",table_number * (i+1))
print("Loop is break")