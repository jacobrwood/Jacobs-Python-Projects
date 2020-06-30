#---------------------------------------!!!THIS PROGRAM'S ALGORITHM WAS COLLECTED FROM https://taxfoundation.org/2020-sales-taxes -------------#
#---------------------------------------!!!THIS PROGRAM USES THE COLUMN LABELED "COMBINED RATE!!!----------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#
while True:
    State = str(input('Please provide the state you are purchasing an item in: '))
    priceOfProduct = float((input('What is the price of the product you are purchasing: ')))
    if State == 'Delaware' or State=='Montana' or State=='New Hamphire' or State=='Oregon':
        tax = float(0.00)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Alaska':
        tax = float(1.76)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Hawaii':
        tax = float(4.44)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Wyoming':
        tax = float(5.34)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Wisconsin':
        tax = float(5.46)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Maine':
        tax = float(5.50)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Virginia':
        tax = float(5.65)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='D.C.' or State=='Kentucky' or State=='Maryland' or State=='Michigan':
        tax = float(6.00)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Idaho':
        tax = float(6.03)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Vermont':
        tax = float(6.22)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Massachusetts':
        tax = float(6.25)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Pennsylvania':
        tax = float(6.34)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Connecticut':
        tax = float(6.35)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='South Dakota':
        tax = float(6.40)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='West Virginia':
        tax = float(6.41)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='New Jersey':
        tax = float(6.60)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='North Dakota':
        tax = float(6.86)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Nebraska':
        tax = float(6.93)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Iowa':
        tax = float(6.94)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='North Carolina':
        tax = float(6.97)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Indiana' or State=='Rhode Island':
        tax = float(7.00)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Florida':
        tax = float(7.05)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Mississippi':
        tax = float(7.07)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Ohio':
        tax = float(7.17)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Utah':
        tax = float(7.18)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Georgia':
        tax = float(7.31)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Minnesota' or State=='South Carolina':
        tax = float(7.46)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Colorado':
        tax = float(7.65)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='New Mexico':
        tax = float(7.82)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Arizona':
        tax = float(8.40)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='California':
        tax = float(8.66)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Kansas':
        tax = float(8.68)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Missouri':
        tax = float(8.18)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='New York':
        tax = float(8.52)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Nevada':
        tax = float(8.32)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Oklahoma':
        tax = float(8.94)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Texas':
        tax = float(8.19)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Alabama':
        tax = float(9.22)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Arakansas':
        tax = float(9.47)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Illinois':
        tax = float(9.08)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Louisiana':
        tax = float(9.52)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Tennessee':
        tax = float(9.53)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))
    elif State=='Washington':
        tax = float(9.21)
        finalPrice= float((priceOfProduct*(tax/100))+priceOfProduct)
        print('Your final cost is $'+str(float(round(finalPrice,2))))

    
    #the loop below comes from https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input    
    
    while True:
        runProgramAgain = input('Would you like to run the program again? Type "Y" for yes, and "N" for no): ')
        if runProgramAgain in ('Y', 'N'):
            break
        print ('Invalid input.  Please type "Y" for yes, and "N" for no.   Please.')
    if runProgramAgain == 'Y':
        continue
    else:
        print ('Program is finished.  Goodbye')
        break
input('Press ENTER to close this program.')
