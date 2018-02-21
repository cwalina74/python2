#Author: Caroline Cwalina
#Class: CCAC Python 2
#Teacher: Eric Darsow
# Goal: This program will have user rank things and sort accordingly



#Get the user input
print('Hello! Welcome to rate my ice cream app! ')
us1= input('Would you like to proceed? (Y/N) ')


#Program if they want to use the app
if us1 == 'Y':
    #Setup the dictionary
    ice_dict = []

    #Get the user input
    print('Okay! Let me ask you a few questions. please answer with a number 1-3 ')
    dict1rate = int(input(" 1-3 what do you rank mint chip? "))
    dict2rate = int(input("1-3 what do you rank grahm central station? "))
    dict3rate = int(input("'1-3 what do you rank vanilla? "))

    #Append the list
    ice_dict.append({
         "mint chip": dict1rate,
         "grahm central": dict2rate,
         "vanilla": dict3rate
    })


    #Sort the list
    items = [(v, k) for k, v in ice_dict.items()]
    items.sort()
    items = [(k, v) for v, k in items]

   #return the list
    print('Here are your rankings: ')
    print(items)



#What to exicute if app not wanted
elif us1 =='N':
    print('Okay! Have a good day!')

#What to exicute if no valid response
elif us1 != 'Y' and us1 != 'N':
    print('Invalid Response. Please start over ')

