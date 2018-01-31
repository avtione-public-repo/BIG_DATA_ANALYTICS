import re
import csv
from HTMLParser import HTMLParser


path = "/home/bigdata/enwiki-all-special_newlines.csv"

# Match on [[ :? Category: .*? ]] ... a non-greedy matcher is used to avoid nested brackets
category_filter_re = re.compile(r"\[\[:?Category\:.*?\]\]")

# remove '[[Category', anything beyond the guard, and the last ']]'
def extract_category(text):
        text = re.sub(r'\[\[:?Category\:', "", text)
        text = re.sub(r'\|.*\]\]', "", text)
        text = re.sub(r'\]\]', "", text)
        return text

def clean_extract_categories(text):
        # Assumption: user wants meaningful categories without duplicates, a Set is used
        # trade-off speed vs usefulness
        categories_list = []
        for occ in re.findall(category_filter_re,text):
                #clean the text from the entire [[category]]
                text = re.sub(category_filter_re,"", text)
                #get the category name
                if occ:
                        categories_list.append(extract_category(occ))
        return (text, list(set(categories_list)))

def get_article_name(text):
    #since it's csv, split the text on commas and take the second item, strip it off quotes
    text = text.split(',')[1]
    return re.sub(r'\"',"", text)

# open csv file categories, read line by line
# get article name, cleaned text and categories list
# write them down in the csv file
with open('categories.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        with open(path) as fileobject:
                for line in fileobject:
                        text,categories = clean_extract_categories(line)
                        name = get_article_name(line)
                        csvwriter.writerow([name, text,categories])

# By having a look at the Special Characters section in https://en.wikipedia.org/wiki/Help:Wiki_markup#Limiting_formatting_.2F_escaping_wiki_markup
# I assumed all special characters are HTML entites (http://www.fileformat.info/format/w3c/htmlentity.htm)
# which HTMLparser can be helpful
def clean_extract_symbols_lib(text):
    h = HTMLParser()
    return h.unescape(text)

# The other way is to make a dictionary and run through a dict ... However I couldn't find a website/source to get all the mapping/conversions
# So I added a sample library and the necessery steps following the fact that a reliable map/dict/library exists.
def clean_extract_symbols(text):
    # example dict
    d = {"&Acirc;":'a', "&Agrave;":'b'}
    for occ in re.findall(r'\&.*?\;',text):
                v = d.get(occ)
                #replace if value found in dict
                if v:
                        text = re.sub(occ,v, text)
    return text;

# open csv file categories, read line by line
# get article name, cleaned text and categories list
# write them down in the csv file
with open('symbols.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        with open(path) as fileobject:
                for line in fileobject:
                        text = clean_extract_symbols(line)
                        name = get_article_name(line)
                        csvwriter.writerow([name, text])