def inch_cm():
    try:
        user=input('Please enter the number: ')
        user=float(user)
        result = user*2.54
        return ('{} inches is {} cm'.format(user,result))
    except:
        return 'Sorry!!!, Please enter a number only'
inch_cm()
