#checks a block of text against a profanity list to determine whether or
# not those profanity words are in the block of text. By default, it will use a medium profanity filter,
#but can use optional level of filter.

import urllib2
import htmlParser

url = raw_input("Which page do you want to check to see if there is profanity?")

def get_page_text(url):
	website = urllib2.urlopen(url)
	website_html = website.read()
	return htmlParser.strip_tags(website_html)

def checkProf(text, filter="Med"):
	profanityLow = ['fuck', 'cunt']
	profanityMed = profanityLow + ['damn', 'shit', 'asshole']
	ProfanityHigh = profanityMed + ['jerk', 'dumbass']

	if filter == 'low' or filter == 'Low':
		profanity = profanityLow
	elif filter == 'high' or filter == 'High':
		profanity = ProfanityHigh
	else: 
		profanity = profanityMed

	profanity_instances = []

	words = text.split()
	for word in words:
		for curse in profanity:
			if word.startswith(curse):
				profanity_instances.append(word)

	if len(profanity_instances) == 0:
			return "Squeaky clean! There is no profanity here!"
	else:
		return "There are %s swear-words here! They are: %s." % (len(profanity_instances), profanity_instances)
	
	

print checkProf(get_page_text(url), raw_input("What level of profanity filter would you like to use? (low, med, high)"))