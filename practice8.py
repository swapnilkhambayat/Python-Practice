first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = (first_value.title().strip(' '))
second_value = (second_value.strip('-')).strip(' ').capitalize()
third_value = (third_value.lower()).replace(' ','').replace('-',' ').capitalize()

print(f'{first_value:^30}')
print(second_value)
print(f'{third_value:>30}')

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value +'#'+fifth_value+'#'+sixth_value+'!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'{fourth_value:>13} \n {fifth_value:>11} \n {sixth_value:>11}')
#       First Challenge        
#Second challenge
#               Third challenge
#fourth#fifth#sixth!
#        fourth
#        fifth
#        sixth