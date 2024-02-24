from rake import rake_model
from lev_dist import levenshtein_model
#from lda import lda_model
from lda import *
from pprint import pprint

def test_input(nr):
        file = open('input_tests/test' + str(nr) + '.txt', 'r', encoding= 'utf-8')
        list = file.readlines()
        aux_text = ''
        for word in list:
            aux_text += word
        aux_text = [word.replace('\n', ' ') for word in aux_text]
        text = ''
        for i in aux_text:
             text += i 
        file.close()
        return text

rake = rake_model('stopwords/stopwords_en.txt', max_words= 1, min_freq= 1)

lda = lda_model('english', 'stopwords/stopwords_en.txt', 'input_tests/test8.txt', n_topics_per_paragraph= 3)

question = 'How long will it be before Agroprom emerges in the role of financial provider'

# Read every stopword
stopwords_file = open('stopwords/stopwords_en.txt', mode='r', encoding='utf-8')

stopwords = stopwords_file.readlines()

stopwords_file.close()

# Remove all linebreaks from stopwords
stopwords = [i.replace('\n', '') for i in stopwords]

question = str(StopWordsRemover(**{ 'stopwords': stopwords }).fit_transform([question])[0])

question = question.replace('.', ' ')
question = question.replace('?', ' ')
question = question.replace('!', ' ')

lemmatizer = WordNetLemmatizer()
keywords = question.split(' ')
keywords = [lemmatizer.lemmatize(i) for i in keywords if i != '']

topic_1_gram = lda.get_topic_1_grams()
transformed_paragraphs = lda.get_transformed_paragraphs()
paragraphs = lda.get_paragraphs()

lev = levenshtein_model(keywords, topic_1_grams= topic_1_gram, transformed_paragraphs= transformed_paragraphs)

final_paragraph = lev.paragraph_identifier()

pprint(paragraphs[final_paragraph])

