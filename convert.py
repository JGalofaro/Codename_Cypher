import base64

def printThis(x):
	str(x)
	print(x)

def encodeString(x):
	str(x)
	a = base64.b64encode(x)
	print(a)

def decodeString(x):
	str(x)
	a = base64.b64decode(x)
	print(a)


def encodeFile(read, write):
	str(read)
	str(write)
	rf = open(read, 'r')
	wf = open(write, 'w')
	a = rf.read().encode("base64")
	wf.write(a)
	rf.close()
	wf.close()

