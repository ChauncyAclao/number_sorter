#inputs number
#loop input until invalid
#store in aaray
#sort numbers

numbers = []

#input and loop
while True:
    number = input("input number:")
    if not (number.isdigit() and int(number) <= 50 and int(number) >= 1) :
        print("INVALID: end of inputs")    
        break

#array
    numbers.append({
        "num" : int(number)
    })

#sort numbers
num_1to10 = [nums["num"] for nums in numbers if (nums["num"] >= 1 and nums["num"] <= 10)]
print("1-10:",num_1to10)
num_11to20 = [nums["num"] for nums in numbers if (nums["num"] >= 11 and nums["num"] <= 20)]
print("11-20:",num_11to20)
num_21to30 = [nums["num"] for nums in numbers if (nums["num"] >= 21 and nums["num"] <= 30)]
print("21-30:",num_21to30)
num_31to40 = [nums["num"] for nums in numbers if (nums["num"] >= 31 and nums["num"] <= 40)]
print("31-40:",num_31to40)
num_41to50 = [nums["num"] for nums in numbers if (nums["num"] >= 41 and nums["num"] <= 50)]
print("41-50:",num_41to50)
