
spring_break = { 'monday': 'work at kellys', 'tuesday': 'work with norkus', 'wednesday':'ran',
               'thursday': 'strip_district', 'friday': 'mall', 'saturday':'pajama icecream', 'sunday': 'drive to cleveland' }



def search_activity(day):
    ''' Retrun the activity of the day by inputting day of the week '''
    try:
        activity = spring_break[day.lower()]
    except:
        return 'day not found'
    return activity

