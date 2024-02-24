from rake import rake_model
from lev_dist import levenshtein_model
from lda import lda_model
from pprint import pprint

def test_input(nr):
        file = open('input_tests/test' + str(nr) + '.txt', 'r', encoding= 'utf-8')
        list = file.readlines()
        aux_text = ''
        for word in list:
            aux_text += word
        aux_text = [word.replace("\n", " ") for word in aux_text]
        text = ''
        for i in aux_text:
             text += i 
        file.close()
        return text

rake = rake_model('stopwords/stopwords_en.txt', max_words= 1, min_freq= 1)

lda = lda_model('english', 'stopwords/stopwords_en.txt', 'input_tests/test6.txt', n_topics_per_paragraph= 3)

question = 'protein proteins protein protein organelle organelle organelle protein'

keywords = question.split(' ')

pprint(keywords)
print()

topic_1_gram = lda.get_topic_1_grams()
transformed_paragraphs = lda.get_transformed_paragraphs()
paragraphs = lda.get_paragraphs()

lev = levenshtein_model(keywords, topic_1_grams= topic_1_gram, transformed_paragraphs= transformed_paragraphs)

final_paragraph = lev.paragraph_identifier()

print(final_paragraph)
print()
pprint(paragraphs[final_paragraph])

