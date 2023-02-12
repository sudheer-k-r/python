csv_data_object = open("csv_file", "r")
csv_data = csv_data_object.readlines()
data = [i.rstrip('\n').split(',') for i in csv_data[1:]]
print(data)

result_object = open("result_csv","w")
for i in data:
    if "@gmail.com" in i[2]:
        result_object.write("$".join(i[::2]))

result_object.close()
csv_data_object.close()
3>4