import sys
table = sys.stdin

cond = sys.argv[1]


'''
cond is a list of comma seperated conditions eg: col_name=val

To run this code use:

python3 select_mapper.py < Employee_data.csv educ=15,gender=m

'''

fp = open("schema.txt","r")
schema = fp.read().strip("()")
fp.close()
schema = schema.split(",")
schema = [x.split(':')[0] for x in schema]

try:
	cond = cond.split(',')
except:
	pass

column_index = []

columns = [x.split("=")[0].strip() for x in cond]
values = [x.split("=")[1].strip() for x in cond]

flag= True
for x in columns:
	if x not in schema:
		print("Select: Given column doesnot exist")
		flag = False

for i in range(len(columns)):
	for j in range(len(schema)):
		if columns[i] == schema[j]:
			column_index.append(j)
# print(columns)
# print(column_index)
# print(values)

for line in table:
	if flag:
		count = len(values)
		line = line.strip()
		line_list = line.split(',')
		for i in range(len(values)):
			if line_list[column_index[i]] == values[i]:
				count-=1
		if count == 0:
			print(line)
