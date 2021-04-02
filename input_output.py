def loadUsers(filename):
	try:
		f = open(filename, 'r')
		lines = f.readlines()
		out =[]
		for line in lines:
			t = line.replace('<', '')
			t = t.replace('>', '')
			out.append(t)
		users = []
		for line in out:
			u = line.replace('\n', '')
			users.append(u + 'Inbox.txt')
		f.close()
		return users
	except:
		print("file not found")
		return []