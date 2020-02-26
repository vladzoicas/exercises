hosts = open('C:\Windows\System32\drivers\etc\hosts')
hosts_file_contents = hosts.read()
#print(hosts_file_contents)

#print(hosts.tell())

#hosts.seek(1000)

#print(hosts.read())

#hosts.close()

#print('###############################################################')

#with open('C:\Windows\System32\drivers\etc\hosts') as the_file:
	#for line in the_file:
	#	print(line)
	
#open('C:\D\python stuff\exercises\file.txt', 'w+') as new_file:
#	print(new_file)
#new_file = open('file.txt','w+')

with open('file.txt', 'w') as new_file_2:
	new_file_2.write(hosts_file_contents)
	
with open('file.txt') as new_file_2:	
	print(new_file_2.read())