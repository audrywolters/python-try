
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
