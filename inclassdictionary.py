## My Dictionary
## This program lists potential apartments

#creating master dictionary
D = {'1531 Green St APT 3 Philadelphia PA 19130':
         {
        'Amenities':  {'Cooling': 'central', 'Heating':'forced', 'Parking':'unknown', 'wifi':'unknown'},
        'Distance:': {'Trader Joes': '1.3 miles', 'Broad Line':'0.3 miles', 'Park':'0.8 miles'},
        'Layout': {'Bedrooms': '2', 'Bathrooms':'1'},
        'Rent': 2000
        },

    '1836 Green St APT 4 Philadelphia PA': \
        {
        'Amenities': {'cooling': 'central', 'heating':'forced', 'parking':'unknown', 'wifi':'unknown'},
         'Distance':{'Trader Joes': '1.1 miles', 'Broad Line':'0.5 miles Broad line', 'Park':'0.6 miles'},
         'Layout': {'Bedrooms': '2', 'Bathrooms':'1'},
         'Rent': 1495
        },

    '1543 Spring Garden St Philadelphia PA':
             {
            'Amenities': {'cooling': 'central', 'heating':'forced', 'parking':'unknown', 'wifi':'unknown'},
            'Distance:': {'Trader Joes': '1.3 miles', 'Broad Line':'0.2 miles Broad line', 'Park':'0.8 miles'},
            'Layout': {'Bedrooms': '1', 'Bathrooms':'1'},
            'Rent': 1995
             }
    }


#Program

ui = input('Enter key ')
if ui in D:
    lookup = (D[ui])
    print(lookup.keys())
    ui2 = input('Which topic would you like to know about from the listed keys? ')
    if ui2 in lookup:
        lookup2 = lookup[ui2]
        print(lookup.keys())
        ui3 = input('Which topic would you like to know about from the listed keys? ')
        if ui3 in lookup2:
            print(lookup2.keys())

    else:
        print('Not a valid key')


else:
    print('Not a valid key')


