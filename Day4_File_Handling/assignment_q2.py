data = input().split(",")
data_obj1 = open("datafile3","r")
test_data = [line.rstrip('\n') for line in data_obj1.readlines()]
data_obj1.close()
write_obj1 = open("result_file1","a")
for i in data:
    if i in test_data:
        print(i)
        write_obj1.write(i)
    else:
        continue
write_obj1.close()