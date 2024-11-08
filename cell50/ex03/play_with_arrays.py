#!/usr/bin/env python3

arrNum=[2,8,9,48,8,22,-12,2]
arrNew=set([x+2 for x in arrNum if x>5])

print('Original array;',arrNum)
print('New array:',arrNew)
