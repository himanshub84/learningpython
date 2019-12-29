name=input('Enter your name')

if len(name) < 3:
    print('should be more then 3 char')
elif len(name) > 50:
    print('Name does not cointain more then 50 char')
else :
    print(name)
