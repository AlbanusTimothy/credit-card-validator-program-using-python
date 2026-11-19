# python credit card validator program
# remove any '-' or ''
# add all the digits in the odd places from right to left
# double any second digit from right to left 
#       (if result is two digit number,
#        add the two digit number together to get a single digit)
# sum the totals of steps 2 and 3
# if the sum is divisible by 10,then the credit card # is valid


while True:
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    # step 1 
    card_number=input("enter a credit card number:  ")
    card_number=card_number.replace("-","")
    card_number=card_number.replace(" ","")

    # reverse the card number
    card_number=card_number[::-1] 

    # step 2
    for x in card_number[::2]:
        sum_odd_digits += int(x)


    #step 3
    for x in card_number[1::2]:
        x =int(x*2)
        if x >= 10:
            sum_even_digits += 1 + (x%10)
        else:
            sum_even_digits +=x


    # step 4
    total =sum_odd_digits + sum_even_digits

    # step 5
    if total % 10==0:
        print ("The card is valid")
        break
    else:
        print("The card is invalid!")   
        continue 

