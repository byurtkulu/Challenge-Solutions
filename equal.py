# Equal:
# Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. 
# She is biased towards her friends and may have distributed the chocolates unequally. 
# One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.
# But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,

# For every operation, she can choose one of her colleagues and can do one of the three things.
# 1. She can give one chocolate to every colleague other than chosen one.
# 2. She can give two chocolates to every colleague other than chosen one.
# 3. She can give five chocolates to every colleague other than chosen one.
# Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates.


# Greedy Algorithm:
# (a + 2b + 5c) = n  -->  min value of (a+b+c)??
def getminSum(n):
    return n/5 + (n%5)/2 + (n%5)%2

# Adding 1,2 or 5 to all element except one of them is as same as
# substracting 1,2 or 5 to that one element.
# Hold on to this idea!
def equal(arr):
    # if arr has 0 or 1 element no change is necessary.
    if len(arr) < 2:
        return 0
    # We meet at most with the minimum by substracting 1,2,5
    # Ex1:  [2,2,3,7] :  2, 2, 3(-1), 7(-5) --> 2, 2, 2, 2
    # Ex2:   [1,5,5]  :  1(-1), 5(-5), 5(-5) --> 0, 0, 0
    m = min(arr)
    m_i = arr.index(m)
    
    # These are for finding and keeping track of the minimum number of operation 
    result = 0
    c_min = sys.maxint
    
    
    
    
    for k in xrange(3):
        result = 0 # it is zero at the beginning of each turn
        # Check the difference between the min value(m) and the other array elements.
        # The difference tells us how many decrementing operation we need.
        # getminSum(n) is used to calculate it.
        for i in xrange(len(arr)):
            if i != m_i:
                d = arr[i] - m
                result += getminSum(d)
        
        # if the turn is 0 this means that we did not decremented the min value yet.
        # for each decrementing we apply extra one operation. 
        # So add it to result.
        if k != 0:
            result += 1
        # Keep track of the min value.
        if result < c_min:
            c_min = result
        
        # Run the for loop by decrementing min value by one at each turn
        # It is necessary to do to find the min.
        m -= 1
        arr[m_i] -= 1
    
    return c_min