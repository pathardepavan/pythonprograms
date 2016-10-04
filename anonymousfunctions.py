#A Lambda function to return the sum of 2 numbers
sum=lambda x,y:x+y

#A Reduce function to get the sum of all the numbers between
#1 to 11
total=reduce(sum,range(1,11))
print(total)	
