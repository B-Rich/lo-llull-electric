import os



out_path = './dylan_complete.txt'
songs_path = './bobDylan_lyricsFreak'



def clean_text(text):
	index1 = text.find("<!-- song lyrics -->")
	index2 = text.find("<!-- /song lyrics -->")
	clean = ''
	if index1 > -1 and index2 > -1:
		clean = text[index1+52:index2-7]
		clean = clean.replace('<br>', ' ')
	return clean



complete_text = ''

for f in os.listdir(songs_path):
	text = open(songs_path+'/'+f).read().lower()	
	complete_text += clean_text(text)

print(complete_text)
