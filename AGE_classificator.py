def classify_age()
    while True:
        Age = int(input("How old are you now?"))
        
        if Age < 0:
            print ("Invalid input, please try again.")
        elif Age < 13:
            print ("You are a Child.")
        elif Age < 20:
            print ("You are a Teenager.")
        elif Age < 65:
            print ("You are an Adult.")
        else:
            print("You are a Senior.")

classify_age()