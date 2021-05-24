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
def _cont_exp(x):
	return utils._cont_exp(x)

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
	return utils._remove_accentedchars(x)

# Remove stopwords
def remove_stopwords(x):
	return utils._remove_stopwords(x)

# Make to base form
def make_base(x):
	return utils._make_base(x)

# Value counts
def get_value_counts(df, col):
	return utils._get_value_counts(df, col)

# Remove frequent/common words
def remove_commonwords(x, freq, n=20):
	return utils._remove_commonwords(x, freq, n)

# Remove rare words
def remove_rarewords(x, freq, n=20):
	return utils._remove_rarewords(x, freq, n)

# Spell correction
def spelling_correction(x):
	return utils._spelling_correction(x)