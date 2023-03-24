# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:11:23 2023

@author: Kairu Cyrus
"""
#python matrix operarions using list
m1 = [[11,9,6],[15,7,13],[10,4,19]]
m2 = [[22,35,2],[7,14,18],[20,6,12]]
print(m1) #returns [[11,9,6],[15,7,13],[10,4,19]]
print(m2[-2]) #returns [7,14,18]
# matrix addition
m3 = [[0,0,0],[0,0,0],[0,0,0]]  #reason for introducing a third matric is because of the use of lists
matr_length = len(m1)
for j in range(len(m1)):
 for k in range(len(m2)):
   m3[j][k] = m1[j][k] + m2[j][k] 
   print(m3) #returns sum in every row and final answer [[33, 44, 8], [22, 21, 31], [30, 10, 31]] 

#for multiplication and subtraction, we involve a similar approach
for j in range(len(m1)):
 for k in range(len(m2)):
   m3[j][k] = m1[j][k] * m2[j][k] 
   print(m3)   # returns multiplication in every row starting with row[0]. Final answer: [[242, 315, 12], [105, 98, 234], [200, 24, 228]]

   


