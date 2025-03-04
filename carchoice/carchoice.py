while True:
    print("1.Sedan\n2.SUV")
    car = int(input("Which car do you want??"))
    if car == 1:
        while True:
            print("1.2 Wheels\n2.4 Wheels")
            tyre = int(input("how many tyres would you like to have??"))
            if tyre == 1:
                import sedan2tyres
                break
            elif tyre == 2:
                import sedan4tyres
                break
            else:
                print("Please check your inputs again.")
    elif car == 2:
        while True:
            print("1.2 Wheels\n2.4 Wheels")
            tyre = int(input("how many tyres would you like to have??"))
            if tyre == 1:
                import suv2tyres
                break
            elif tyre == 2:
                import suv4tyres
                break
            else:
                print("Please check your inputs again.")
    else:
        print("Please check your inputs again.")