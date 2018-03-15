

def csv_searcher (search_word): #input is the word that you are searching for
    file_to_search = open('fruit.csv') #open csv
    list_to_test = list(file_to_search) #turn to list
    times_in_list = list_to_test.count(search_word)  #seaqrch for it
    return int(times_in_list) #outpt is number in times in the list



print((csv_searcher('apple')))
