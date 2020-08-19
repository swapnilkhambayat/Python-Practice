def process_numbers(my_list):
    #return_list = []
    number_list = []
    #string_list = []

    if isinstance(my_list,list):
        for i in my_list:
            if isinstance(i,int):
                number_list.append(i) 
            elif isinstance(i, str):
                if i.isnumeric():
                    converted_item = int(i)
                    number_list.append(converted_item)
    else:
        return number_list
    
    number_list.sort()
    return number_list


def process_names(my_list):
    #return_list = []
    string_list = []

    if isinstance(my_list,list):
        for i in my_list:
            if isinstance(i,str):
                if i.isnumeric() == False:
                    string_list.append(i)       
    else:
        return string_list

    string_list.sort()
    return string_list

