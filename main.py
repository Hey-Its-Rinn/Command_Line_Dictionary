from lib.funcs import lookup


def main():
	user_input = input('Enter a search term: ')

	result = lookup(user_input)
	print('')
	for each in result:
		print(each + '\n')


if __name__ == '__main__':
	main()
