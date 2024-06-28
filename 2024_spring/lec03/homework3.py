def cancellation(input_list, stop_word):
    output_list = [] 
    for element in input_list:
        if element == stop_word:
            break 
        output_list.append(element)
    return output_list

def copy_all_but_skip_word(input_list, skip_word):
    output_list = [] 
    for element in input_list:
        if element != skip_word:
            output_list.append(element) 
    return output_list

def my_average(input_list):
    total = 0
    for element in input_list: 
        total += element 
    return total / len(input_list)