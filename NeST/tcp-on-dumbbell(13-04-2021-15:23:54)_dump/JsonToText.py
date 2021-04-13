
'''

code to extract cwnd data and time in seconds

rohit kumar
'''

import json

file = open('ss.json', 'r')

data_orig  = json.loads(file.read())



def WriteToFile(data, file):
	
	line = ''
	time = float(data[1]['timestamp']);
	for i in range(1, len(data)):
		line = str(float(data[i]['timestamp'])-time) + '\t' + data[i]["cwnd"] + "\n"
		file.writelines(line)
	
	pass



file1 = open("cwnd_data_node_1.txt", "a")

data = data_orig["left-node-1"];
data = data[0]["10.0.1.3"]["35577"]

WriteToFile(data,  file1)



file2 = open("cwnd_data_node_0.txt", "a")

data = data_orig["left-node-0"];
data = data[0]["10.0.1.1"]["36447"]

WriteToFile(data, file2)


#"left-node-2"

file3 = open("cwnd_data_node_2.txt", "a")

data = data_orig["left-node-2"];
data = data[0]["10.0.1.5"]["35009"]

WriteToFile(data, file3)
