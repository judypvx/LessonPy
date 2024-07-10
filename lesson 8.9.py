while True:
    for attempt in range(1,4):
        pincode = int(input('Enter your pincode: '))
        if pincode == 1234:
            print('You entered the correct pincode')
            break
        print('Try again left chances: ', 3 - attempt)
    else:
        print('Your card is blocked')
    print('Welcome new visitor')
