#!/usr/local/bin/python2.7.3
# -*- coding: utf-8 -*-
#given three files in english,swedish and greek
#the script will produce 3 cleaner versions of them
#3 tokenized versions of the cleaned versions
#and 3 files containing the lines erased
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import swadesh
english_stopwords = stopwords.words('english')
swedish_stopwords = stopwords.words('swedish')
#set(w.lower() for w in text)
#swadesh.fileids()
english_common_words = swadesh.words('en')

sv_eng_sim_in_sw_stopwords = ['i', 'till', 'dig', 'under']
for word in sv_eng_sim_in_sw_stopwords:
	if word in english_stopwords:
		english_stopwords.remove(word)

common_words_eng_swed = ['I', 'not', 'all', 'small', 'man', 'dog',\
 'bark', 'fat', 'hand', 'drink', 'live', 'hit', 'dig', 'lie', 'fall', \
 'river', 'lake', 'salt', 'sand', 'red', 'full', 'bad', 'far', 'in', 'and']

for word in common_words_eng_swed:
	if word in english_common_words:
		english_common_words.remove(word)


def read_files():
	path_el = 'corpus_el.txt'
	path_en = 'corpus_en.txt'
	path_sv= 'corpus_sv.txt'
	doc_=open(path_el,'r')
	el = doc_.read()
	doc_.close
	#doc_ = open(path_en,'r')
	#en = doc_.read()
	#doc_.close
	#remove_string(el, en)
	doc = open(path_sv, 'r')
	sv = doc.read()
	doc.close()
	#########################################
	#comment out what you don't want to call
	#clean_el(el)
	clean_sv(sv)
	#clean_en(en)
	########################################
def clean_sv(sv):
	out_file_sv = open('clean_sv', 'w')
	out_file_sv_dirty = open('dirty_sv', 'w')
	for line in sv.split('\n'):
		flag = 0
		if line == '':
			continue
		if line.isdigit():
			out_file_sv_dirty.write(line + "  ======digit")
			out_file_sv_dirty.write('\n')
			continue
		if len(line) < 3:
			out_file_sv_dirty.write(line+ "   ======small length")
			out_file_sv_dirty.write('\n')
			continue
		'''
		reg_char = 'the|I|[h|H]ave|[Y|y]ou|[H|h]e|[S|s]he|\
		[W|w]e|they| is| it|your| not|can|could|will| was| were| our| to | this| a | like| has'
		if bool(re.search(reg_char , line)):
			out_file_sv_dirty.write(line)
			out_file_sv_dirty.write('\n')
			continue
		'''
		merged = list(set(english_stopwords+english_common_words))
		for word in merged:
			#word_1 = ' ' + word +' '
			word_2 =' ' +word + ' '
			if (word_2 in line):# or (word_2 in line):
				out_file_sv_dirty.write(line + '===='+ word)
				out_file_sv_dirty.write('\n')
				flag = 1
				break
		if flag:
			continue
		line = line.replace('Å','å')
		line = line.replace('Ä','ä')
		line = line.replace('Ö','ö')
		out_file_sv.write(line.lower())
		out_file_sv.write('\n')
	out_file_sv_dirty.close()
	out_file_sv.close()
	tokenize('clean_sv')

def clean_el(el):
	out_file_el = open('clean_el', 'w')
	out_file_el_dirty = open('dirty_el', 'w')
	for line in el.split('\n'):
		if line == '':
			continue
		if line.isdigit():
			out_file_el_dirty.write(line)
			out_file_el_dirty.write('\n')
			continue
		if len(line) < 3:
			out_file_el_dirty.write(line)
			out_file_el_dirty.write('\n')
			continue
		'''
		if line.find('/') == -1 and line.find('[') == -1:
			pass
		'''
		reg_char = '[\[/\^_-\*<\=|a-z]'
		reg_char = '[#|a-z]'
		reg_char = '[\[/\^]'
		reg_char = '[#|a-z]'
		if bool(re.search(reg_char , line)):
			out_file_el_dirty.write(line)
			out_file_el_dirty.write('\n')
			continue
		out_file_el.write(line)
		out_file_el.write('\n')
	out_file_el_dirty.close()
	out_file_el.close()
	tokenize('clean_el')

def clean_en(en):
	out_file_en = open('clean_en', 'w')
	out_file_en_dirty = open('dirty_en', 'w')
	for line in en.split('\n'):
	    if line == '':
	    	continue
	    if line.isdigit():
	    	out_file_en_dirty.write(line)
	    	out_file_en_dirty.write('\n')
	    	continue
	    if len(line) < 3:
	    	out_file_en_dirty.write(line)
	    	out_file_en_dirty.write('\n')
	    	continue
	    out_file_en.write(line.lower())
	out_file_en_dirty.close()
	out_file_en.close()
	tokenize('clean_en')

def tokenize(text , lang = 'def'):
	doc=open(text,'r')
	clean_text = doc.read()
	doc.close()
	out_file = open(text+ "_tokenized", 'w')
	if lang == 'en':
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		out_file.write('\n'.join(tokenizer.tokenize(clean_text)))
	elif lang == 'sv':
		tokenizer = nltk.data.load('tokenizers/punkt/swedish.pickle')
		out_file.write('\n'.join(tokenizer.tokenize(clean_text)))
	elif lang == 'el':
		tokenizer = nltk.data.load('tokenizers/punkt/greek.pickle')
		out_file.write('\n'.join(tokenizer.tokenize(clean_text)))
	else:
		array = re.split(r"([.\s|,\s])",clean_text)
		clean_text = "".join(array)
		#clean_text = clean_text.replace('.',' . ')
		clean_text = clean_text.replace('!',' !')
		#clean_text = clean_text.replace(':',' :')
		clean_text = clean_text.replace('?',' ?')
		clean_text = clean_text.replace(';',' ;')
		clean_text = clean_text.replace(',',' , ')
		clean_text = clean_text.replace('[',' ')
		clean_text = clean_text.replace(']',' ')
		clean_text = clean_text.replace('(',' ')
		clean_text = clean_text.replace(')',' ')
		clean_text = clean_text.replace('»',' » ')
		clean_text = clean_text.replace('«',' « ')
		clean_text = clean_text.replace('·',' ·')
		clean_text = clean_text.replace('<',' < ')
		clean_text = clean_text.replace('>',' > ')
		out_file.write(clean_text)
	out_file.close()
#re.split('[]', file)
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#print nltk.data.path





read_files()
