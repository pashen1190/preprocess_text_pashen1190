from preprocess_text_pashen1190 import utils

__version__ = '0.0.1'

# Word count
def get_wordcount(x):
	return utils._get_wordcount(x)

# Character count
def get_charcount(x):
	return utils._get_charcount(x)

# Average word length
def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

# Stopwords count
def get_stopwordscount(x):
	return utils._get_stopwordscount(x)

# Hashtag count
def get_hashtagcount(x):
	return utils._get_hashtagcount(x)
	
# @mentions count
def get_mentionscount(x):
	return utils._get_mentionscount(x)

# numeric digit count
def get_digitcount(x):
	return utils._get_digitcount(x)

# uppercase count
def get_uppercasecount(x):
	return utils._get_uppercasecount(x)

# Contraction Expansion 
def get_cont_exp(x):
	return utils._get_cont_exp(x)

# Emails and its count

def get_emails(x):
	return utils._get_emails(x)

# Remove email
def remove_emails(x):
	return utils._remove_emails(x)

# URL and count
def get_urls(x):
	return utils._get_urls(x)

# Remove Urls
def remove_urls(x):
	return utils._remove_urls(x)

# Retweets and count
def get_retweets(x):
	return utils._get_retweets(x)
# Remove retweets
def remove_rt(x):
	return utils._remove_rt(x)

# Remove special characters
def remove_specialchars(x):
	return utils._remove_specialchars(x)

# Remove HTML Tags
def remove_HTMLtags(x):
	return utils._remove_HTMLtags(x)

# Remove Accented Characters
def remove_accentedchars(x):
	return utils._remove_accentedchars

# Remove stopwords
def remove_stopwords(x):
	return utils._remove_stopwords(x)

# Make to base form
def make_base(x):
	return utils._make_base(x)

# Find most frequent/common words
def get_commonwords(x, n=20):
	return utils._get_commonwords(x, n)

# Find least freqent/rare words
def get_rarewords(x, n=20):
	utils._get_rarewords(x, n)

# Remove common/rare words
def remove_common_rare_words(x, fn):
	return utils._remove_common_rare_words(x, fn)

# Spell correction
def spelling_correction(x):
	return utils._spelling_correction(x)