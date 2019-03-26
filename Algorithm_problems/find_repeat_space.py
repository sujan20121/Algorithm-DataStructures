#interviewcake-find repeat space edition

def search_repeated(arr):
    l = len(arr)
    possible_elem_range = list(range(1,l))
    
    while len(possible_elem_range)>1:
        mid = len(possible_elem_range) // 2
        
        check_list_1 = possible_elem_range[:mid]#the first half of the possible integer values
        print('check_list_1:',check_list_1)
        
        check_list_2 = possible_elem_range[mid:]#the other half of the possible integer values
        print('check_list_2:',check_list_2)
        
        arr1 = [e for e in arr if e in check_list_1]#the elements in the array which belong to the FIRST half of the possible element values
        print('arr1:',arr1)
        
        arr2 = [e for e in arr if e in check_list_2]#the elements in the array which belong to the SECOND half of the possible element values
        print('arr2:',arr2)
        
        if len(arr1)>len(check_list_1):
            """
            making the use of Pigeon hole theory, such that if arr1 has more elements than the numbers of distinct elements
            possible, then arr1 has at least one duplicate element
            """
            possible_elem_range = check_list_1#if that's the case, this should be the new range for possible distinct elements
            print('p_e_r:',possible_elem_range)
        else:
            possible_elem_range = check_list_2
            print('p_e_r:',possible_elem_range)
    
    print('element is:',possible_elem_range[0])
