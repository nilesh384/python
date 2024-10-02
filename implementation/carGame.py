
type = ''
while type.lower()!='quit':
    type = str(input('type anything: '))
    type = type.lower()


    if(type == 'help'):
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')

    elif(type == 'start'):
        print('car started...Ready to go')
    
    elif(type == 'stop'):
        print('car stopped')
    
    elif(type == 'quit'):
        print('bye')
    else:
        print('i dont understand')