oldList = [4,5,3,45,7,89,2,0,34,344]
newList = []

def function():
	for number in oldList:
		if(number > 5):
			newList.append(number)
function()
print(newList)