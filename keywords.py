from artifici_lda.logic.stop_words_remover import *
from nltk.stem import WordNetLemmatizer
from pprint import pprint

class keyword_identifier:
    def __init__(self, stopwords_path):
        # Read every stopword
        stopwords_file = open(stopwords_path, mode='r', encoding='utf-8')

        self.stopwords = stopwords_file.readlines()

        stopwords_file.close()

        # Remove all linebreaks from stopwords
        self.stopwords = [i.replace('\n', '') for i in self.stopwords]

        # Create the stop words remover
        stopwords_remover_params =  {
            'stopwords': self.stopwords
        }
        self.stopwords_remover = StopWordsRemover(**stopwords_remover_params)

        # Create the lemmatizer
        self.lemmatizer = WordNetLemmatizer()

    def get_keywords(self, question):
        # Remove all stopwords from the question
        question_no_stopwords = self.stopwords_remover.fit_transform([question])[0]

        # Split the question into keywords
        question_no_stopwords = question_no_stopwords.replace('.', ' ')
        question_no_stopwords = question_no_stopwords.replace('?', ' ')
        question_no_stopwords = question_no_stopwords.replace('!', ' ')

        keywords = question_no_stopwords.split(' ')

        # Lemmatize every keyword and remove empty ones
        keywords = [self.lemmatizer.lemmatize(i) for i in keywords if i != '']

        return keywords

if __name__ == "__main__":
    # Use the keyword identifier on a sample question and print every keyword
    kw_identifier = keyword_identifier(stopwords_path='stopwords/stopwords_en.txt')

    question = 'What is the organelle that produces proteins?'
    keywords = kw_identifier.get_keywords(question)
    pprint(keywords)
