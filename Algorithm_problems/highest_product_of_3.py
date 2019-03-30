"""
This is a O(n) solution to finding the largest product of any 
3 numbers in a given array/list. This uses greedy approach. A brute force
would require O(n^3) time complexity. 

The main idea with the approach is that, the highest product of 3 numbers at
a given number is the maximum of (current_number*highest_product_of_2,current_number*lowest_product_of_2))

"""

def func_highest_product_of_3(integer_list):
    highest_number = max(integer_list[0],integer_list[1],integer_list[2])
    lowest_number = min(integer_list[0],integer_list[1],integer_list[2])
    
    highest_product_of_2 = max(integer_list[0]*integer_list[1],integer_list[0]*integer_list[2],integer_list[1]*integer_list[2])
    lowest_product_of_2 = min(integer_list[0]*integer_list[1],integer_list[0]*integer_list[2],integer_list[1]*integer_list[2])
    
    highest_product_of_3 = integer_list[0]*integer_list[1]*integer_list[2]
    
    for i in range(3,len(integer_list)):
        current_number = integer_list[i]
        current_product_of_3 = max(current_number*highest_product_of_2,current_number*lowest_product_of_2)
        
        if current_product_of_3 > highest_product_of_3:
            highest_product_of_3 = current_product_of_3
        
        current_product_of_2 = max(current_number*highest_number,current_number*lowest_number)
        if current_product_of_2 > highest_product_of_2:
            highest_product_of_2 = current_product_of_2
            
        if current_product_of_2 < lowest_product_of_2:
            lowest_product_of_2 = current_product_of_2
        
        if current_number > highest_number:
            highest_number = current_number
            
        if current_number < lowest_number:
            lowest_number = current_number
        
    
    return highest_product_of_3
            
        
        
    
    
