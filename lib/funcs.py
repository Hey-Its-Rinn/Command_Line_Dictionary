import json
import difflib
from difflib import SequenceMatcher


data = json.load(open('data.json'))


def lookup(word):
	if word in data:
		return data[word]
	elif word.capitalize() in data:
		return data[word.capitalize()]
	elif word.upper() in data:
		return data[word.upper()]
	else:
		suggestion = ''
		suggestion_score = 0
		for key in data:
			candidate = key			
			candidate_score = SequenceMatcher(None, word, key).ratio()
			if candidate_score > suggestion_score:
				suggestion = candidate
				suggestion_score = candidate_score
		
		user_input = input('Did not find ' + word + '. Did you mean: ' + suggestion + '?(Y/N): ')
		if user_input.lower() in ['yes', 'y', 'yeah', 'hell yes']:
		#	import pdb; pdb.set_trace()
			return data[suggestion]
		else:
			return ['No word found.']