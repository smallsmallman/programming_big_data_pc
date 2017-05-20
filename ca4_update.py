#this file uses dictionary as opposed to classes
#this file doesn't bother getting the changes or comments, do this ourselves
changes_file = 'changes_python.log'

def read_file(changes_file):
	# use strip to strip out spaces and trim the line.
	data = [line.strip() for line in open(changes_file, 'r')]
	return data

def get_commits(data):
	sep = 72*'-'
	commits = []
	index = 0
	while index < len(data):
		try:
			# parse each of the commits and put them into a list of commits
			details = data[index + 1].split('|')
			# the author with spaces at end removed.
			commit = {'revision': details[0].strip(),
				'author': details[1].strip(),
				'date': details[2].strip(),
				'number_of_lines': details[3].strip().split(' ')[1]
			}
			# add details to the list of commits.
			commits.append(commit)
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return commits


def get_authors(data):
	sep = 72*'-'
	authors = {}
	index = 0
	while index < len(data):
		try:
			# parse each of the authors and put them into a list of authors
			author = data[index + 1].split('|')[1].strip()
			if author not in authors:
				authors[author] = 1
				index += 1
			else:
				authors[author] += 1
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return authors

def get_busy_day(data):
	sep = 72*'-'
	days = {}
	index = 0
	while index < len(data):
		try:
			date = data[index + 1].split('|')[2].strip()
			day = date.split(' ')[3].strip('(').strip(',')
			if day not in days:
				days[day] = 1
				index += 1
			else:
				days[day] += 1
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return days
		
	
if __name__ == '__main__':
	# open the file - and read all of the lines.
	changes_file = 'changes_python.log'
	data = read_file(changes_file)
	commits = get_commits(data)
	authors = get_authors(data)
	day = get_busy_day(data)

# print the number of lines read
	print(len(data))

	print authors

	print day
	
#print(commits)
#print commits

#print(commits[1]['author'])
#print(len(commits))