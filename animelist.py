class Anime:
	# constructor: takes name of anime (string) and number of episodes (int)
	# and optionally length if episodes are not standard length
	
	def __init__(self, name, episodes, length=22):
		self.name = name
		self.episodes = int(episodes)
		self.length = int(length)
		

	def to_string(self):
		string = self.name + ', ' + str(self.episodes)
		return string


def main():
	anime_list = read_from_file("animelist.txt")
	run_program = True
	while(run_program):
		print('''1. View list
2. Total time spent
3. Append to list
4. Save Session
5. Quit''')

		choice = input('>')

		if choice == '1':
			view_list(anime_list)
		elif choice == '2':
			total_time(anime_list)
		elif choice == '3':
			add_anime(anime_list)
		elif choice == '4':
			write_to_file(anime_list, "animelist.txt")
		elif choice == '5':
			print("Goodbye!")
			run_program = False
		else:
			print("Invalid input. Try again.")


	
# read saved data from text file and convert to Anime objects
# takes name of file 
# returns list of Anime objects 
def read_from_file(fname):
	filename = fname
	file = open(fname, 'r')

	line_list = file.read().splitlines()

	

	anime_list = []

	for line in line_list:
		split_index = 0
		for i, c in enumerate(line):
			if c == ',':
				split_index = i

		anime_name = line[0:split_index]
		anime_episodes = line[split_index+2:]

		anime = Anime(anime_name, anime_episodes)
		anime_list.append(anime)

	return anime_list


# prints contents of anime list to console
# takes anime_list as argument
def view_list(anime_list):
	print("view list")
	for anime in anime_list:
		print(anime.to_string())


# prints total time of life spent watching anime to console
# takes anime_list as argument
def total_time(anime_list):
	time = 0
	for anime in anime_list:
		t = anime.episodes * anime.length
		time = time + t
	print("You have spent " + str(time) + " minutes watching anime.")

	# minutes to hours
	hours = time / 60
	hours = round(hours, 1)

	# minutes to days
	days = hours / 24
	days = round(days, 1)

	print("This is equivalent to " + str(hours) + " hours, or " + str(days) + " days.")

# allows user to input another entry to add to list
# takes anime_list
def add_anime(anime_list):
	name = input("Enter title for new entry. >")
	eps = input("Enter number of episodes for new entry. >")

	new_anime = Anime(name, eps)

	anime_list.append(new_anime)

# writes current list contents to file to save
# takes anime_list, filename
def write_to_file(anime_list, fname):
	# truncate file
	file = open(fname, 'w')
	file.close()

	file = open(fname, 'a')
	for anime in anime_list:
		line_to_write = anime.to_string()
		line_to_write = line_to_write + '\n'
		file.write(line_to_write)

	file.close()

	print("File saved.")


main()