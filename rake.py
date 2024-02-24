from multi_rake import Rake
from pprint import pprint
global TESTING
TESTING = False

def test_input(nr):
        file = open('input_tests/test_input' + str(nr) + '.txt', 'r', encoding= 'utf-8')
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

class rake_model:

    def __init__(self, stop_words_file, min_chars= 2, max_words= 1, min_freq= 1, language_code= 'en', lang_detect_threshold= 100,
                 max_words_unknown_lang= 1, generated_stopwords_percentile= 90, generated_stopwords_max_len= 3, 
                 generated_stopwords_min_freq= 4):
        self.min_chars = min_chars
        self.max_words = max_words
        self.min_freq = min_freq
        self.language_code = language_code
        self.lang_detect_threshold = lang_detect_threshold
        self.max_words_unknown_lang = max_words_unknown_lang
        self.generated_stopwords_percentile = generated_stopwords_percentile
        self.generated_stopwords_max_len = generated_stopwords_max_len
        self.generated_stopwords_min_freq = generated_stopwords_min_freq
        self.stop_words_file = stop_words_file
        self.stop_words = self.stop_words_make_list(self.stop_words_file)
        self.model = self.create_model()
        

    def stop_words_make_list(self, stop_words_file):
        file = open(stop_words_file, 'r', encoding= 'utf-8')
        stop_words = file.readlines()
        stop_words = [word.replace("\n", "") for word in stop_words]
        file.close()
        return stop_words
           

    def create_model(self):
        rake = Rake(
            min_chars= self.min_chars,
            max_words= self.max_words,
            min_freq= self.min_freq,
            language_code= self.language_code, 
            stopwords= self.stop_words,  
            lang_detect_threshold= self.lang_detect_threshold,
            max_words_unknown_lang= self.max_words_unknown_lang,
            generated_stopwords_percentile= self.generated_stopwords_percentile,
            generated_stopwords_max_len= self.generated_stopwords_max_len,
            generated_stopwords_min_freq= self.generated_stopwords_min_freq
        )
        return rake
    
    def update_parameters(self):
        return self.create_model() 

if __name__ == "__main__":
    rake = rake_model(stop_words_file= 'stopwords/stopwords_en.txt')

    text = 'What is the organelle that produces proteins?'

    keywords = rake.model.apply(text)
    #keywords = [(word , score/2) if word.find(' ') != -1 else (word, score) for word,score in keywords]
    for word in keywords:
        pprint(word)
