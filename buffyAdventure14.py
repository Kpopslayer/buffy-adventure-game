# Choose you own adventure Buffy Style

import sys  # have to import this to use sys.exit in order to stop code execution

print('You are Buffy Summers, the vampire slayer')
print('...')
input()

print('Even though you take your destiny seriously, '
      'sometimes you just want to hang out with your friends and be a regular teenage girl.')
print('...')
input()

print('\nAre you going to patrol at the cemetery (A) like you watcher asked you too or chill (B) at the Bronze?')

choice = 1
while choice != 'A' or 'B':
    choice = input('A or B? ')

    if choice == 'A':
        print('\nAt the cemetery you are bored out of your mind.')
        print('...')
        input()
        print('At least you feel like you are doing something useful, instead of just partying.')
        print('...')
        input()
        print('Your slayer instinct kicks in, and you feel like you should check out the Mausoleum.')
        print('...')
        input()
        print('\nAre you staying where you are right now (A) like you promised your watcher, or are you going to '
              'investigate (B)?')
        choice = 1
        while choice != 'A' or 'B': 
            choice = input('A or B? ')

            if choice == 'A':
                print('\nYou decide to stay and walk around, kinda hoping that a vampire will show up')
                print('...')
                input()
                print('Suddenly you feel the flesh on your back melting...')
                print('...')
                input()
                print('Before you can scream, everything turns black...')
                print('...')
                input()
                print('\nTHE END.')
                input()
                sys.exit()  # This stops code execution in Python
                
            if choice == 'B':
                print('\nYou trust Giles, but you trust yourself more.')
                print('...')
                input()
                print('You are almost at the entrance of the Mausoleum.')
                print('...')
                input()
                print('Something is not right...')
                print('...')
                input()
                print('\nAre you going to sneak in (A) or wait outside in the bushes (B)?')
                choice = 1
                while choice != 'A' or 'B': 
                    choice = input('A or B? ')

                    if choice == 'A':
                        print('\nYou do not want to take any risks and decide to find a silent way in.')
                        print('...')
                        input()
                        print('At the right of the mausoleum you spot a small hole.')
                        print('...')
                        input()
                        print('\nAre you going to climb through the hole (A) or try to look through it(B)?')
                        choice = 1
                        while choice != 'A' or 'B': 
                            choice = input('A or B? ')

                            if choice == 'A':
                                print('\nYou cannot help but smile at the though of surprising who ever is inside')
                                print('...')
                                input()
                                print('Very...slowly... you try to squeeze yourself through the hole.')
                                print('...')
                                input()
                                print('Emphasis on TRYING. You forgot that most woman have curves'
                                      ' and are not stick figures.')
                                print('...')
                                input()
                                print('you keep pulling and pulling and eventually you fall into the mausoleum.')
                                print('...')
                                input()
                                print('Unfortunately, your fall made a lot of noise and your instincts go haywire.')
                                print('...')
                                input()      
                                print('Before you are able to prepare yourself, you feel an intense heat.')
                                print('...')
                                input() 
                                print('And then NOTHING.')
                                print('\nTHE END.')
                                input()
                                sys.exit()  # This stops code execution in Python
        
                            if choice == 'B':
                                print('\nYou slowly get closer to the hole.')
                                print('...')
                                input()
                                print('You look through the hole, but it its quite dark.')
                                print('...')
                                input()
                                print('But then you notice a figure who is crouching over some books.')
                                print('...')
                                input()
                                print('A faint red light makes the outlines of his figure visible.')
                                print('...')
                                input()
                                print('Suddenly the mysterious guy stands up.')
                                print('...')
                                input()
                                print('Your heart jumps, but you are pretty sure he has not spotted you (yet).')
                                print('...')
                                input()
                                print('\nAre you going to continue to look (A)'
                                      ' through the hole or try to find a way (B) inside?')
                                choice = 1
                                while choice != 'A' or 'B': 
                                    choice = input('A or B? ')

                                    if choice == 'A':
                                        print('\nBefore you can blink, the mysterious figure looks straight at you.')
                                        print('...')
                                        input()
                                        print('You feel an enormous heat, and then... you vanish')
                                        print('...')
                                        input()
                                        print('Like they say...')
                                        print('...')
                                        input()
                                        print('Curiosity killed the cat...')
                                        print('...')
                                        input()
                                        print('THE END.')
                                        input()
                                        sys.exit()  # This stops code execution in Python

                                    if choice == 'B':
                                        print('\nYou slowly back away, and try to find an alternative way in.')
                                        print('...')
                                        input()
                                        print('You climb on top of the Mausoleum, trying to be as silent as you can.')
                                        print('...')
                                        input()
                                        print('what a coincidence, another hole, but this time it is a lot bigger.')
                                        print('...')
                                        input()
                                        print('You make your way inside. it is time to come up with a plan.')
                                        print('...')
                                        input()
                                        print('\nAre you going for a sudden and vicious attack (A)'
                                              ' or a silent kill (B)?')
                                        choice = 1
                                        while choice != 'A' or 'B':
                                            choice = input('A or B? ')

                                            if choice == 'A':
                                                print('You already wasted enough time, and decide to make it quick.')
                                                print('...')
                                                input()
                                                print('You try to orientate yourself and '
                                                      'realize the figure is around the corner.')
                                                print('...')
                                                input()
                                                print('you reach for your stake and focus all of your energy.')
                                                print('...')
                                                input()
                                                print('It is showtime!')
                                                print('...')
                                                input()
                                                print('You run towards the corner and make a sharp turn to the right.')
                                                print('...')
                                                input()
                                                print('The figure turns out to be nerdy vampire, with glasses and'
                                                      ' X-men shirt.')
                                                print('...')
                                                input()
                                                print('\nAre you going to kick him in the face (A)'
                                                      ' or right in the nuts (B)?')
                                                choice = 1
                                                while choice != 'A' or 'B':
                                                    choice = input('A or B? ')

                                                    if choice == 'A':
                                                        print('\nWithout thinking twice, you kick him right in his face'
                                                              '')
                                                        print('...')
                                                        input()
                                                        print('His glasses fall broken on the floor and the vampire '
                                                              'squeezes his eyes out of agony')
                                                        print('...')
                                                        input()
                                                        print('Are you going to stake him (A)'
                                                              ' or torture (B)  him for information first?')
                                                        choice = 1
                                                        while choice != 'A' or 'B':
                                                            choice = input('A or B? ')

                                                            if choice == 'A':
                                                                print('You immediately stake him right in the heart')
                                                                print('...')
                                                                input()
                                                                print('After a second only red ashes are left')
                                                                print('...')
                                                                input()
                                                                print('Weird, but you guess you will never find out the'
                                                                      ' reason for this odd color.')
                                                                print('...')
                                                                input()
                                                                print('Guess it is time to hit the Bronze after all.')
                                                                print('...')
                                                                input()
                                                                print('THE END.')
                                                                input()
                                                                sys.exit()  # This stops code execution in Python

                                                            if choice == 'B':
                                                                print('You grab him by his shirt and toss him on the'
                                                                      ' ground')
                                                                print('...')
                                                                input()
                                                                print('You ask: What are you doing here here mister?')
                                                                print('...')
                                                                input()
                                                                print('He gives you a sinister smile.')
                                                                print('...')
                                                                input()
                                                                print('He says: My destiny...')
                                                                print('...')
                                                                input()
                                                                print('Before you can reply with a catchphrase, '
                                                                      'everything turns bright red.')
                                                                print('...')
                                                                input()
                                                                print('You scream for mere seconds, but it feels like '
                                                                      'minutes while your flesh burns...')
                                                                print('THE END.')
                                                                input()
                                                                sys.exit()  # This stops code execution in Python

                                                    if choice == 'B':
                                                        print('This will teach it.')
                                                        print('...')
                                                        input()
                                                        print('Unfortunately for you, it looks like he is prepared.')
                                                        print('...')
                                                        input()
                                                        print('Even vampires protect their jewels at all costs.')
                                                        print('...')
                                                        input()
                                                        print('He grabs your leg and throws you on your back.')
                                                        print('...')
                                                        input()
                                                        print('You try to get back up, but he kicks you in the face.')
                                                        print('...')
                                                        input()
                                                        print('He slowly removes his glasses and stares right at you.')
                                                        print('...')
                                                        input()
                                                        print('Calmly he says: No one can stop my destiny.')
                                                        print('...')
                                                        input()
                                                        print('laser beams from his eyes start to burn in your '
                                                              'stomach.')
                                                        print('...')
                                                        input()
                                                        print('Your eyes roll back and in seconds your short life'
                                                              ' flashes before your eyes.')
                                                        print('...')
                                                        input()
                                                        print('You are just a 16 year old girl.')
                                                        print('...')
                                                        input()
                                                        print('You WERE just a 16 year old girl.')
                                                        print('...')
                                                        input()
                                                        print('THE END.')
                                                        input()
                                                        sys.exit()  # This stops code execution in Python
                                                        
                    if choice == 'B':
                        print('Whatever of whoever is inside should eventually come out....Right?')
                        print('...')
                        input()
                        print('You sit in the center of the biggest bush you could find and try to make yourself '
                              'somewhat comfortable.')
                        print('...')
                        input()
                        print('A few minutes pass...')
                        print('...')
                        input()
                        print('You suddenly feel something crawling at the back of you neck.')
                        print('...')
                        input()
                        print('It cannot be...')
                        print('...')
                        input()
                        print('A freaking spider!!!')
                        print('...')
                        input()
                        print('You jump up and down while screaming hysterically.')
                        print('...')
                        input()
                        print('Suddenly a faint red light catches your eyes.')
                        print('...')
                        input()
                        print('In front of the mausoleum a figure with bright red eyes stares right at you.')
                        print('...')
                        input()
                        print('Before you can get into cover, you feel an intense heat.')
                        print('...')
                        input()
                        print('You want to cry, but it is already to late.')
                        print('THE END.')
                        input()
                        sys.exit()  # This stops code execution in Python

    if choice == 'B':
        print('\n\'The Devil you Know (God is a Man\') by Face to Face is playing while you enter the Bronze.')
        print('...')
        input()
        print('You are wondering whether your \'sorta\' boyfriend Angel is going to show up.')
        print('...')
        input()
        print('Before you can over think your last conversation with him Xander, one of your best friends,'
              ' drags you to the dance floor.')
        print('...')
        input()
        print('While you are are being dragged away, a red headed Giles at the balcony above you, '
              'is trying to get your attention by waving his arms frantically.')
        print('...')
        input()
        print('\nAre you joining Xander on the dance floor (A) or will you go to Giles, your watcher?')
        choice = 1
        while choice != 'A' or 'B': 
            choice = input('A or B? ')

            if choice == 'A':
                print('You sign to Giles that you are going to catch up with him later and turn around before '
                      'you can see his disappointment, or well, anger.')
                print('...')
                input()