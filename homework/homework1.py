odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

for a in zip (odd,even):
    print(list(a))
    list2=a*2
    print(list2)
    #print(f'Even: {even[a]*2}')
    #print(f'Odd: {odd[a]*2}')
    

