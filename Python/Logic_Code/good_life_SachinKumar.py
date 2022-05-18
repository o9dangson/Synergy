#Five dogs
#Saber, Ginger, Nutmeg, Pepper, and Bear\

#Five activities
#getting its ears scratched, playing catch, taking a nap, burying a chew toy, and going for a walk

# Pepper is either playing catch or burying a chew toy.
# Neither Ginger nor Saber nor Bear is on a walk.
# One of the dogs named after a spice is getting its ears scratched.
# A dog not named for a spice is playing catch.
# Bear is getting some exercise.

dog0 = 'Saber'
dog1 = 'Ginger'
dog2 = 'Nutmeg'
dog3 = 'Pepper'
dog4 = 'Bear'

dogs=[dog0,dog1,dog2,dog3,dog4]

activity0 = 'ear scratched'
activity1 = 'playing catch'
activity2 = 'taking a nap'
activity3 = 'burying a chew toy'
activity4 = 'going for a walk'

activities=[activity0,activity1,activity2,activity3,activity4]

#dogs=[True, True,True,True,True]
#dog    ear,catch,nap,chwew,walk
test0= [True,True,True,False,False]
test1= [True,False,False,False,False]#
test2= [True,False,True,False,True]
test3= [False,False,False,True,False]#
test4= [False,True,False,False,False]#

testcase= [test0,test1,test2,test3,test4]

counter = 0
location = 0
for i in range(5):
    for j in range(5):
        if(testcase[i][j]==True):
            counter+=1
            location=j
    if(counter == 1):
        for k in range(5):
            testcase[k][location]=False
        testcase[i][location] =True
    location=0
    counter=0


for i in range(5):
    for j in range(5):
        if(testcase[i][j]==True):
            counter+=1
            location=j
    if(counter == 1):
        for k in range(5):
            testcase[k][location]=False
        testcase[i][location] =True
    location=0
    counter=0


for i in range(5):
    for j in range(5):
        if(testcase[i][j]):
            print(dogs[i],activities[j]+" ")

print("end")





