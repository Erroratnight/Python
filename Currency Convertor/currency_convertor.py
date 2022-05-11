data_dict={}

with open("currency_data.txt") as data:
    lines=data.readlines()

    for line in lines:
        splited_line=line.split("\t")

        data_dict[splited_line[0]]=splited_line[1]

Choice=int(input("Enter Choice 1- Convert in Rupess 2-Convert From Rupess: "))
print("Available Option are:")

[print(item) for item in data_dict.keys()]
Currency=input("\nEnter Foregin Currency Name:")
Value=float(input(("\nEnter Value: ")))


if Choice==1:
    print(f"Your Converted Amount is {float(Value)/float(data_dict[Currency])} Rupess\n")

else:
    print(f"Your Converted Amount is {float(Value)*float(data_dict[Currency])} {Currency}\n")



