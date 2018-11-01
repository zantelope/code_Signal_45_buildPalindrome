def buildPalindrome(st):

    ###s acts as a temporary string to test for palindromes
    s = st
    ### counter for while loop
    t = 0
    
    ###checks if a palindrom has been achieved, if not continue loop
    while s[::-1] != s:
        
        ### sets s equal to the original string, plus a reversed slice of the string that starts from one more space 
        ### to the right each iteration(t defines starting point), and goes to the beginning
        s = st + st[t::-1]
        
        ### increase counter by 1
        t += 1


    return s
