# Set operations on data ( shopping basket )

basket_1 = {'apple', 'mango', 'salt', 'shampoo', 'rice', 'milk'}
basket_2 = {'tissues', 'soup', 'gum', 'mango', 'pepper', 'rice', 'apple'}

union = basket_1 & basket_2
differance = basket_1 - basket_2
intersection = basket_1 | basket_2
symmetric_difference = basket_1 ^ basket_2

print(union)
print(differance)
print(intersection)
print(symmetric_difference)
