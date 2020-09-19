def hamming(n):
    """Returns the nth hamming number"""
    
    seq = [1]*n # First term is 1
    m2 = 2 # Next potential hamming numbers
    m3 = 3 # They are obtained by multiplying themselves by 2,3 or 5 each time they are the right hamming numbers
    m5 = 5
    
    l2 = 0 # Last index m2 was multiplied with
    l3 = 0 # m3 by 3
    l5 = 0 # m5 by 5
    
    for i in range(1,n):
        m = min(m2,m3,m5)
        seq[i] = m
        
        if m == m2:
            l2+=1
            m2 = 2 * seq[l2]
        
        if m == m3:
            l3+=1
            m3 = 3 * seq[l3]
        
        if m == m5:
            l5+=1
            m5 = 5 * seq[l5]
    
    return seq[n-1]    
