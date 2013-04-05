import sys
import screed

filename = sys.argv[1]
print filename
count=0
for record in screed.open(filename):
	if count > 9:
		break
	print record
	count +=1
