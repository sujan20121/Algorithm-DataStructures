"""
An O(n) time and space solution to find a list containing porducts
of all elements of a list except for the one at that index.
Eg: Given a list [1,2,3,4], output [24,12,8,6]
"""
def get_products_of_all_integers_except_at_index(input_list):
    if len(input_list) < 2:
        raise ValueError('List needs to have at least 2 integers')
    
    product_of_all_ints_before_index = [None]*len(input_list)
    product_so_far = 1
    
    for i in range(len(input_list)):
        product_of_all_ints_before_index[i] = product_so_far
        product_so_far *= input_list[i]
        
    product_so_far = 1
    for i in range(len(input_list)-1,-1,-1):
        product_of_all_ints_before_index[i] *= product_so_far #No need to create a new list containing
                                                             #product of elements after the index
        product_so_far *= input_list[i]
        
    return product_of_all_ints_before_index
