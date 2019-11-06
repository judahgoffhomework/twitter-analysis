from sys import argv
def parse_arguments():
	if len(argv) > 1:
		# Remove the file name
		del argv[0]
		return argv[0]
	print("Error: Supply a twitter ID to read")
	return None

def read_file(file_name):
	featnames = []
	users_to_tweets = {}
	with open(f'{file_name}.featnames', 'r', encoding='utf-8') as file_reader:
		line = file_reader.readline()
		while line:
			line_list = line.strip().split(' ')
			featnames.append(line_list[1])
			line = file_reader.readline()
	with open(f'{file_name}.feat', 'r', encoding='utf-8') as file_reader:
		line = file_reader.readline()
		while line:
			line_list = line.strip().split(' ')
			user_id = line_list[0]
			rest = line_list[1:]
			user_tweets = []
			for item in rest:
				index = int(item)
				if index != 0:
					print(user_id, user_tweets)
					user_tweets.append(featnames[index])
			users_to_tweets[user_id] = user_tweets
			line = file_reader.readline()
	print(users_to_tweets)


file_name = parse_arguments()
if file_name is not None:
	read_file(file_name)