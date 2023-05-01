# Range Function


# for i in range(11): # range is not inclusive, counts TO that value.
#     print(i)

# for i in range(1,11): # 1 is the start, 11 is the stop
#     print(i)

# for i in range(11, 0, -1):
#     print(i)


food_list = ['Udon Noodles', 'Tacos', 'Pizza', 'Hummus', 'fried rice']

for i in range( len(food_list) ):
    print( food_list[i] )

for food in food_list:
    print(food)