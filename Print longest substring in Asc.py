# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:52:27 2017

@author: ramals2
"""

# get the string
# check if ascii value of first char say n char <= n+1 char
# if yes check next and contcatenate to a string variable and repeat till n > n+1
# get length of string and put it in a variable once n > n+1
# Now for  n > n+1, check next if ascii of n <=n+1 if yes repeat above step and put this set in a
# new string variable and get the length
# repeat this step till all the set are found and then compare the lenght of each string set and print the string of max len


#s = 'azabcdefghijcbobobegghikl'

s = 'azcbobobegghaklmnilopqm'


i = 0
str1=''
print(s,len(s))
for l in s:    #b
    
    
    if i < len(s)-1 and l <=s[i+1]:# len 14  i 7 b
            str1 = str1 + l #b
            #print("First ",i, str1)
            i +=1 # i = 8
            
            if i+1 < len(s) and s[i] > s[i+1]: #len 15 i 8 e
                str2 = str1 + s[i] #be
                #print("Second ",i, str2)
                str1=''
            elif i+1 < len(s) and s[i] <= s[i+1]:
                str2 = str1 + s[i]
                
            
            print("final ",i, str2)
            
    else:
            i += 1 # 7
            

   
    
    #str3 = str2
    #print("test",str3)       
    #print(len(s))
i -= 1
if i == len(s)-1 and ord(s[i])>ord(s[i-i]):
                str2 = str2 + s[i]
                print(str2, "'",s[i],s[i-1], s[len(s)-1],i, len(s)-1, ord(s[i]), ord(s[i-1]))
print (i)
        

            
  

        
        
        