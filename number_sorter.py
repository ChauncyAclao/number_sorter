#inputs number
#loop input until invalid
#store in aaray
#sort numbers


#input and loop
while True:
    number = input("input number:")
    if not (number.isdigit() and int(number) <= 50 and int(number) >= 1) :
        print("end of input")    
        break
