Passcode='Kiwi6541'
print('Hi, what is your name?')
print('Who planted zat stupid tree on siz sharp turn?')
print('It is much too dangerous')
print('I have a chainsaw')
name=input('My name is ')
Text=f'Hi {name}.'
print(Text)
print('What is the passcode for this computer?')
ans=0
Pass=input()
if(Pass!=Passcode):
    print('It is not working!!!')
    print('Since you gave me the wrong passcode, how did you log on to this computer!!!!!!?????')
    ans=input('1 = asking. 2 = tricking me. 3 = Someone did it for you. ')
    
    while(ans=='1'):
        if(ans=='1'):
            print('Try another passcode.')
            Pass=input()
        if(Pass==Passcode):
            Text=f'Thank you {name} for telling me.'
            print(Text)
            print('I am going to hack into this computer.')
            ans='0'
            print('What is your age?')
            Age=input('My age is: ')
            x=int(Age)
            if (x<20):
                print('You are very young. Go and do some sport.')
            if(19<x<51):
                print('You are quite old now. Go and have some sleep.')
            if(50<x):
                print('You are really old. Go and relax on a couch.')

            print('Your name going down will be: ')
            for word in name:
                for letter in word:
                    print(letter)
            print('Bye')
                
    if(ans=='2'):
        print('Why did you trick me? You are not allowed to enter this survey again if you do not tell me the password!')
        Pass=input()
        if(Pass==Passcode):
            Text=f'Thank you {name} for telling me.'
            print(Text)
            print('I am going to hack into this computer.')
            ans='0'
            print('What is your age?')
            Age=input('My age is: ')
            x=int(Age)
            if (x<20):
                print('You are very young. Go and do some sport.')
            if(19<x<51):
                print('You are quite old now. Go and have some sleep.')
            if(50<x):
                print('You are really old. Go and relax on a couch.')

            print('Your name going down will be: ')
            for word in name:
                for letter in word:
                    print(letter)
            print('Bye')
            
        else:
            print('Bye')

    if(ans=='3'):
        print('Ask that person to tell me the password to this computer. If he/she gets it wrong, you are not allowed to enter this survey again.')
        Pass=input()
        if(Pass==Passcode):
            Text=f'Thank you {name} for telling me.'
            print(Text)
            print('I am going to hack into this computer.')
            ans='0'
            print('What is your age?')
            Age=input('My age is: ')
            x=int(Age)
            if (x<20):
                print('You are very young. Go and do some sport.')
            if(19<x<51):
                print('You are quite old now. Go and have some sleep.')
            if(50<x):
                print('You are really old. Go and relax on a couch.')
            print('Your name going down will be: ')
            for word in name:
                for letter in word:
                    print(letter)
            print('Bye')

        else:
            print('Bye')


else:
     Text=f'Thank you {name} for telling me.'
     print(Text)
     print('I am going to hack into this computer.')
     print('What is your age?')
     Age=input('My age is: ')
     x=int(Age)
     if (x<20):
         print('You are very young. Go and do some sport.')
     if(19<x<51):
         print('You are quite old now. Go and have some sleep.')
     if(50<x):
        print('You are really old. Go and relax on a couch.')
    
     print('Your name going down will be: ')
     for word in name:
         for letter in word:
             print(letter)
     print('Bye')
          

