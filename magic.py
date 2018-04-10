#CLI program to find the animal in user's mind using algorithm.
def getUserInput(group):
    print '**********';
    for animal in group:
        print animal
    print '**********';
    userInput = raw_input("In the above list, do you see the animal that you have in your mind? y/n:")
    if userInput == 'y':
        return group[0]
    elif userInput == 'n':
        return 0
    else:
        print 'Your input is not recognised'
        return getUserInput(group)


#Program starts here
    
animals = ['cat', 'dog', 'tiger', 'lion', 'dear', 'bear', 'elephant', 'monkey', 'donkey', 'pig'] #defining a list know as animals to hold all the animals listed as option to user
group1 = [1, 'tiger', 'lion', 'cat', 'pig', 'dear'] #group 1 of animals for user to chose
group2 = [2, 'cat', 'lion', 'dear', 'dog', 'donkey', 'bear']#group 2 of animals for user to chose
group3 = [3, 'cat', 'dog', 'tiger', 'monkey', 'bear', 'dear']#group 3 of animals for user to chose
group4= [4, 'tiger', 'dog', 'cat', 'elephant', 'lion']#group 4 of animals for user to chose
print '**********';
#for loop to display all the options to ask the user to think of an animal from the list
for animal in animals:
    print animal
print '**********';
print "Think of an animal from the above list, keep it in your mind!"
raw_input("press any key once you are done thinking of an animal")
#total holds the index of the list animals
total = getUserInput(group1) + getUserInput(group2) + getUserInput(group3) + getUserInput(group4)
#subracted with 10 as per the algorithm
total = 10 - total
print 'The animal in your mind is "'+animals[total]+'"'

