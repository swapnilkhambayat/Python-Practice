colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']
#Slicing in List
print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')

print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[:3])

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end up until the last item:')
print(colors[-4:-1])
#reverse helper function 
colors.reverse()
print('Reversed List:',colors)
#sort helper function
colors.sort()
print('Sorted List:',colors)
#pop helper function 
color = colors.pop(0)
print('popped', color)

print(colors)
#append new data at the end of list
colors.append('black')
colors.append('white')
#remove data from the list
colors.remove('yellow')
colors.remove('orange')

print('Appended and Removed data from List:',colors)
#extend the new list to existing list
new_colors = ['lime', 'gray']
colors.extend(new_colors)
print('Extended List:',colors)
# clear the list data
colors.clear()
print(colors)