import re
import os
import sys

import pandas as pd
import numpy as np

import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

# Word count
def _get_wordcount(x):
	length = len(str(x).split())
	return length

# Character count
def _get_charcount(x):
	s = x.split()
	x = ''.join(s)
	return len(x)

# Average word length
def _get_avg_wordlength(x):
	count = _get_charcounts(x)/_get_wordcounts(x)
	return count

# Stopwords count
def _get_stopwordscount(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

# Hashtag count
def _get_hashtagcount(x):
	l = len([t for t in x.split() if t.startswith('#')])
	return l

# @mentions count
def _get_mentionscount(x):
	l = len([t for t in x.split() if t.startswith('@')])
	return l

# numeric digit count
def _get_digitcount(x):
	l = len([t for t in x.split() if t.isdigit()])
	return l

# uppercase count
def _get_uppercasecount(x):
	return len([t for t in x.split() if t.isupper()])

# contraction expansion
def _get_cont_exp(x):

	contractions = { 
		"ain't": "am not",
		"aren't": "are not",
		"can't": "cannot",
		"can't've": "cannot have",
		"'cause": "because",
		"could've": "could have",
		"couldn't": "could not",
		"couldn't've": "could not have",
		"didn't": "did not",
		"doesn't": "does not",
		"don't": "do not",
		"hadn't": "had not",
		"hadn't've": "had not have",
		"hasn't": "has not",
		"haven't": "have not",
		"he'd": "he would",
		"he'd've": "he would have",
		"he'll": "he will",
		"he'll've": "he will have",
		"he's": "he is",
		"how'd": "how did",
		"how'd'y": "how do you",
		"how'll": "how will",
		"how's": "how does",
		"i'd": "i would",
		"i'd've": "i would have",
		"i'll": "i will",
		"i'll've": "i will have",
		"i'm": "i am",
		"i've": "i have",
		"isn't": "is not",
		"it'd": "it would",
		"it'd've": "it would have",
		"it'll": "it will",
		"it'll've": "it will have",
		"it's": "it is",
		"let's": "let us",
		"ma'am": "madam",
		"mayn't": "may not",
		"might've": "might have",
		"mightn't": "might not",
		"mightn't've": "might not have",
		"must've": "must have",
		"mustn't": "must not",
		"mustn't've": "must not have",
		"needn't": "need not",
		"needn't've": "need not have",
		"o'clock": "of the clock",
		"oughtn't": "ought not",
		"oughtn't've": "ought not have",
		"shan't": "shall not",
		"sha'n't": "shall not",
		"shan't've": "shall not have",
		"she'd": "she would",
		"she'd've": "she would have",
		"she'll": "she will",
		"she'll've": "she will have",
		"she's": "she is",
		"should've": "should have",
		"shouldn't": "should not",
		"shouldn't've": "should not have",
		"so've": "so have",
		"so's": "so is",
		"that'd": "that would",
		"that'd've": "that would have",
		"that's": "that is",
		"there'd": "there would",
		"there'd've": "there would have",
		"there's": "there is",
		"they'd": "they would",
		"they'd've": "they would have",
		"they'll": "they will",
		"they'll've": "they will have",
		"they're": "they are",
		"they've": "they have",
		"to've": "to have",
		"wasn't": "was not",
		" u ": " you ",
		" ur ": " your ",
		" n ": " and ",
		"won't": "would not",
		'dis': 'this',
		'bak': 'back',
		'brng': 'bring'
	}

	x = x.lower()
	if type(x) is str:
		for key in contractions:
			value = contractions[key]
			x = x.replace(key, value)
		return x
	else:
		return x

# Emails and its count

def _get_emails(x):
	emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)', x)
	count = len(emails)

	return counts, emails

# Remove email
def _remove_emails(x):
	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

# URL and count
def _get_urls(x):
	urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
	count = len(urls)

	return count, urls

# Remove Urls
def _remove_urls(x):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

# Retweets and count
def _get_retweets(x):
	rts = re.findall(r'\brt\b\s', x)
	counts = len(rts)

	return counts, rts

# Remove retweets
def _remove_rt(x):
	return re.sub(r'\brt\b\s', '', x)

# Remove special characters
def _remove_specialchars(x):
	x = re.sub(r'[^\w]+', '', x)
	x = ' '.join(x.split())
	return x

# Remove HTML Tags
def _remove_HTMLtags(x):
	return BeautifulSoup(x, 'html.parser').get_text().strip()

# Remove Accented Characters
def _remove_accentedchars(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x

# Remove stopwords
def _remove_stopwords(x):
	return ' '.join([t for t in x.split if t not in stopwords])

# Make to base form
def _make_base(x):
	nlp = spacy.load('en_core_web_sm')
	x = str(x)
	x_list = []
	doc = nlp(x)
	
	for token in doc:
		lemma = token.lemma_
		if lemma == '-PRON-' or lemma == 'be':
			lemma = token.text

		x_list.append(lemma)
	return ' '.join(x_list)

# Find most frequent/common words
def _get_commonwords(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm[n]
	return fn

# Find least freqent/rare words
def _get_rarewords(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm.tail(n)
	return fn

# Remove common/rare words
def _remove_common_rare_words(x, fn):
	x = ' '.join([t for t in x.split() if t not in fn])
	return x

# Spell correction
def _spelling_correction(x):
	 x = TextBlob(x).correct()
	 return x
