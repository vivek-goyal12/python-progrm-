#program to get number of notes from atm 
num = int(input("enter requirement amount"))
t = num//2000   #number of 2000 notes
num = num%2000
f = num//500    #number of 500 notes
num = num%500
h = num//100    #number of 100 notes
print("number of 2000,500,100 = ",t,f,h)
