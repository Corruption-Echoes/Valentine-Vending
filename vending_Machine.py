from datetime import datetime, timedelta
import inquirer

def inputValidator(typeIn):
    intake=False
    while(intake==False):
        intake=input("")
        if(typeIn=='float'):
            try:
                intake=float(intake)    
            except:
                intake=False
                print('Please enter a float')
            if(type(intake)!=float):
                intake=False
            else:
                return intake
        elif(typeIn=='Bool'):
            if(intake=='Yes' or intake=='No'): 
                if(intake=='Yes'): 
                    return True
                else:
                    return False
            else:
                try:
                    intake=bool(intake)
                except:
                    print('Please enter Yes/No or True/False')
        else:
            return intake

def advertise():
    print("BUY A GIFT!")

def convertSelection(intake):
    for x in range(len(itemList)):
        if(intake==itemList[x]):
            return x
        
powerOn=True
currentBalance=0
currentCoinBuffer=0
currentState='advertising'
adDelay=1
selection=0
ctime=datetime.now()+timedelta(seconds=adDelay)
# implement an array of current items

itemList=['Cookies','Chocolates','Cinnamon Hearts','Breakfast in bed','Romantic Cards','Stuffed Animals','Love potions','Arrows']
#implement an array of current item prices
itemPrice=[3.25,5,7.8,4,4.25,11,2.5,11]
#implement an array of current stock
itemStock=[20,15,10,11,0,2,3,15]
while(powerOn):
    
    #print advertising messages
    if(currentState=='advertising'):
        if(datetime.now()>ctime):
            advertise()
            ctime=datetime.now()+timedelta(seconds=adDelay)
            currentState='CoinCollecting'
    #Wait for the user to insert coins
    if(currentState=='CoinCollecting'):
        print("Balance:$",currentCoinBuffer)
        print("Please add coins: Enter 0 to move to purchasing")
        inputI=inputValidator('float')#Validate the coins
        if(inputI!=0):
            currentCoinBuffer+=inputI
        else:
            currentState='Selection'
    #Ask for a selection
    if(currentState=='Selection'):
        questions = [
        inquirer.List('user_selection',
                            message="What are you interested in?",
                            choices=itemList,
                            ),
        ]
        answers = inquirer.prompt(questions)

        print('What would you like to purchase?(Type Menu for a list of options with prices)')
        inputI=answers['user_selection']
        if(inputI=='Menu' or inputI=='menu' or inputI=='MENU'):
            currentState='Menu'
        else:  
            selection=convertSelection(inputI)
            currentState='Paying'

    #Display a menu if the user requests it
    if(currentState=='Menu'):
        #Make a print for the menu with prices
        for x in range(len(itemList)):
            if(itemStock[x]>0):
                print(itemList[x],": $",itemPrice[x])
        currentState='Selection'
        
    #Check if the user has enough money inserted
    if(currentState=='Paying'):
        if(currentCoinBuffer >= itemPrice[selection]):
            currentCoinBuffer-=itemPrice[selection]
            currentBalance+=itemPrice[selection]
            currentState='Vending'
    #Vend items and update stock registry
    if(currentState=='Vending'):
        if(itemStock[selection]>0):
            itemStock[selection]-=1
            print('Here is your ',itemList[selection])
            print('Thank you for your purchase!')
            currentState='PostSale'            
    #inquire if user would like to purchase other items or return current coin buffer
    if(currentState=='PostSale'):
        print('Would you like to purchase anything else?')
        inputI=inputValidator('Bool')
        if(inputI):
            currentState='Selection'
        else:
            print('Have a wonderful day! Here is your change! You receive $',currentCoinBuffer)
            currentCoinBuffer=0
            currentState='advertising'