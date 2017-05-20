#this file uses dictionaries as opposed to classes
changes_file = 'changes_python.log'

def read_file(changes_file):
	# strip us used to strip out spaces and trim the line.
	data = [line.strip() for line in open(changes_file, 'r')]
	return data

#get the number of commitments made over the whole dataset
def get_commits(data):
	#each commitment is separated by 72 hyphons
	sep = 72*'-'
	commits = []
	index = 0
	while index < len(data):
		try:
			details = data[index + 1].split('|')
			#parsing each of the commits and putting them into a dictionary with the associated keys and values
			commit = {'revision': details[0].strip(),
				'author': details[1].strip(),
				'date': details[2].strip(),
				'number_of_lines': details[3].strip().split(' ')[1]
			}
			#appending each commit to the list 'commits'
			commits.append(commit)
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return commits

#get a list of which authors made commits and how many each made
def get_authors(data):
	sep = 72*'-'
	authors = {}
	index = 0
	while index < len(data):
		try:
			#finding the authors within each commit
			author = data[index + 1].split('|')[1].strip()
			#adding new authors to the dictionary of authors, with an assignment of 1 commitment
			if author not in authors:
				authors[author] = 1
				index += 1
			#adding an additional value of 1 every time the author is found
			else:
				authors[author] += 1
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return authors

#similar to authors, finding which day produces the most commitments
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

#similar to 'get_busy_day' finding which month produces the most commitments
def get_busy_month(data):
	sep = 72*'-'
	months = {}
	index = 0
	while index < len(data):
		try:
			date = data[index + 1].split('|')[2].strip()
			month = date.split('(')[1].split(' ')[2]
			if month not in months:
				months[month] = 1
				index += 1
			else:
				months[month] += 1
			index = data.index(sep, index + 1)
		except IndexError:
			break
	return months	


#the following two functions were attempted but due to time constraints could be completed at a later date
	
#def get_quantity_files(data):
#	sep = 72*'-'
#	file_count = []
#	index = 0
#	while index < len(data):
#		try:
#			#details = data[index + 1].split('|')
#			# parse each of the commits and put them into a list of commits
#			# the author with spaces at end removed.
#			files = data[index+2:data.index('',index+1)]
#			for line in files.split('\n'):
#				file_count.append(files)
#			index = data.index(sep, index + 1)
#		except IndexError:	
#			break
#	return file_count


#def get_busy_timeofday(data):
#	sep = 72*'-'
#	morning = {}
#	afternoon = {}
#	unsociable = {}
#	index = 0
#	while index < len(data):
#		try:
#			date = data[index + 1].split('|')[2].strip()
#			time = date.split(' ')[1]
#			hour = time.split(':')[0]
#			if hour < 12 and hour >= 7:
#				morning[hour] = 1
#				index += 1
#			elif hour >= 12 and hour < 6:
#				afternoon[hour] = 1
#				index += 1
#			else:
#				unsociable[hour] = 1
#			index = data.index(sep, index + 1)
#		except IndexError:
#			break
#	return morning, 'xxxxx', afternoon, 'xxxxx', unsociable
	


		
if __name__ == '__main__':
	#testing the functions
	changes_file = 'changes_python.log'
	data = read_file(changes_file)
	commits = get_commits(data)
	authors = get_authors(data)
	days = get_busy_day(data)
	months = get_busy_month(data)

	print 'Number of lines of data: ', len(data)
	print 'Number of commitments: ', len(commits)
	print 'Authors and associated commits: ', authors
	print 'Days and associated commits: ', days
	print 'Months and associated commits: ', months