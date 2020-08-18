
# fizz buzz!
def fizzBuzz():
    for number in range( 25 ):
        if ( number % 3 == 0 ):
            print( 'fizz' )
        elif ( number % 5 == 0 ):
            print( 'buzz' )
        else:
            print( 'fizz buzz' )
        
fizzBuzz()


# function and variable
def helloFriend( friendName ):
    print ( 'hello ' + friendName )

friends = 'Jill and Megan'
helloFriend( friends )


# array and loop
coolArray = [ 'thing', 2, True ]

for item in coolArray:
    print( item )


# object
class Cat:
    def __init__( self, name, color ):
        self.name = name
        self.color = color

kitty1 = Cat( 'Mina', 'brown spotted tabby' )
kitty2 = Cat( 'Mervyn', 'black' )

print( 'Names: ' + kitty1.name, kitty2.name )
print( 'Colors: ' + kitty1.color, kitty2.color )


# return value function
def sumNumbers( num1, num2 ):
    return num1 + num2

print( '1 + 2 =', sumNumbers( 1, 2 ) )


# conditionals
def equalOperator(): 
    if ( 1 == 2 ):
        print ( 'equal: True' )
    else:
        print ( 'equal: False' )

equalOperator()


one = 1
two = 2
def andOperator():
    if ( one == 1 and two == 2 ):
        print( 'and: True' )
    else:
        print( 'and: False' )

andOperator()

def orOperator():
    if ( one == 2 or two == 2 ):
        print( 'or: True' )

orOperator()