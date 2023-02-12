fileobject = open("data2.txt", "a+")

fileobject.seek(0)

print(fileobject.read(3))


fileobject.seek(5)
fileobject.write("$$")

fileobject.close()