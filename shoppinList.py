#!/usr/bin/env python3

shopList = ['banana', 'apple', 'orange', 'mango']

print('I have', len(shopList), 'items to purchase')

print('These items are:',end=' ')

for item in shopList:
  print(item, end=' ')


print('I will append another item to my list')
shopList.append('grapes')
print('Show my list', shopList)
