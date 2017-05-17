# open the file - and read all of the lines.
changes_file = 'changes_python.log'


#my_file = open(changes_file, 'r')
#data = my_file.readlines()

# use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

class Commit(object):
	'class for commits'
	def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
		self.revision = revision
		self.author = author
		self.date = date
		self.comment_line_count = comment_line_count
		self.changes = changes
		self.comment = comment

	def get_commit_comment(self):
		return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
				+ self.author + ' with the comment ' + ','.join(self.comment) \
				+ ' and the changes ' + ','.join(self.changes)
				
	def get_commit_author(self):
		while index < len(data):
			try:
				author = data[index + 1].split('|').strip()
				if author in authors:
					authors[author] = authors[author] + 1
				else:
					authors[author] = 1
			except:
				break 

#a_commit = Commit('r1551925', 'Thomas', 
#		'2015-11-27 16:57:44 +0000 (Fri. 27 Nov 2015)',
#		1, None, 'Renamed folder to correct name')
		
#print a_commit.revision
#print a_commit.author

commits = []
current_commit = None
index = 0

#Search for seperator
#Read line for revision, author, date, comment line count
#Read file changes
#Read comment 
#Get next commit

author = {}

while True:
	# parse each of the commits and put them into a list of commits
	try:
		current_commit = Commit()
		details = data[index + 1].split('|')
		#print details
		current_commit.revision = int(details[0].strip().strip('r'))
		current_commit.author = details[1].strip()
		current_commit.date = details[2].strip()
		current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
		current_commit.changes = data[index + 2: data.index('', index + 1)]
		#print current_commit.comment_line_count
		current_commit.comment = data[index - current_commit.comment_line_count:index]
		index = data.index(sep, index + 1)
		
		commits.append(current_commit)
	except IndexError:
		break

print len(commits)
commits.reverse()

for index, commit in enumerate(commits):
	print commit.get_commit_author()
		
#print commits[2].author
#print commits[2].changes
#print commits[2].comment