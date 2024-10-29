#inputs number
#loop input until invalid
#store in aaray
#sort numbers

numbers = []

#input and loop
while True:
    number = input("input number:")
    if not (number.isdigit() and int(number) <= 50 and int(number) >= 1) :
        print("INVALID: end of inputS")    
        break
#array
    numbers.append({
        "num" : number
    })

print(numbers)

