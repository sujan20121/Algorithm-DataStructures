def mD(stocks,stocks_len):#function to calculate the maximum difference
    m_D = stocks[1] - stocks[0]#variable for storing latest Max Difference
    min_stock = stocks[0]#variable for the latest minimum stock value
    for i in range(1,stocks_len):
        if(stocks[i] - min_stock > m_D):
            m_D = stocks[i] - min_stock
       
        if(stocks[i] < min_stock):#if this stock is smaller than the current minimum stock value
            min_stock = stocks[i]
    return m_D

closing = [7,6,4,3,1,2,5]
size = len(closing)
print(mD(closing,size))#prints the max profit value
