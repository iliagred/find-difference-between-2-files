import os
#change directors where locate files
#os.chdir('D:/python')
os.chdir('D:/')
print(os.getcwd())
print('Please put location file1, Exemple:D:/python/file1 ')
file1 = input()
print('Please put location file2, Exemple:D:/python/file2 ')
file2 = input()
print('Please check if you file location corect '+file1)
print('Please check if you file location corect '+file2)

with open(file1,'r') as file1:
	with open(file2,'r') as file2:
		same=set(file1).intersection(file2)

same.discard('\n')
with open('output','w') as file_out:
	for line in same:
		file_out.write(line)
showmyresult = open('output', 'r')

print(showmyresult.read())		