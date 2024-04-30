data={"book":10,"pen":20}
x = 0
while x<5:
    print("\n\n**********  stock list    ***********")
    for i in data.keys():
        print(i,"   :   ",data[i])
    print("\n\nEnter 1 to add new item \n 2 to delete item \n 3 to search stock \n other to exit")
    x=int(input("\nEnter the value:"))
    if x==1:
        new_value=input("Enter the item name:")
        data[new_value]=input("Enter number of items:")
    elif x==2:
        value_name=input("Enter the item name")
        data.__delitem__(value_name)
    elif x==3:
        value_name=input("Enter the item name")
        print("no of item = ",data[value_name]) 


