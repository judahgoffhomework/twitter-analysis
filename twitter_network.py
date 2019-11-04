def parse_arguments():
	if len(argv) > 0:
		# Remove the file name
		del argv[0]
		return argv[0]
	if len(argv) == 0:
		print("Error: Supply a twitter ID to read")
		return None

file_name = parse_arguments()
if file_name is None:
	return
