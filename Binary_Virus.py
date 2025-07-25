def Virus_eat(array,no_spikes):
    final_list = []
    # for i in array:
    #     binary_num = format(i,'b')
    #     removed_spikes  = binary_num[:-no_spikes]
    #     if removed_spikes:
    #         converted_decimal = int(removed_spikes,2)
    #     else:
    #         converted_decimal = 0
    #     final_list.append(converted_decimal)
    # return final_list
    for i in array:
        converted_decimal = i >> no_spikes  # Bitwise right shift
        final_list.append(converted_decimal)
    return final_list

array = [1,2,3,4,5]
array1 = [45,57]
no_spikes = 2
print(Virus_eat(array,no_spikes))
print(Virus_eat(array1,no_spikes))
