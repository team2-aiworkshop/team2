from multi_rake import Rake
global TESTING
TESTING = True

def test_input(nr):
         file = open('input_tests/test' + str(nr) + '.txt', 'r', encoding= 'utf-8')
         list = file.readlines()
         text = ''
         for word in list:
              text = (text + word )
         file.close()
         return text

class rake_model:

    def __init__(self, stop_words_file = None, min_chars= 3, max_words= 2, min_freq= 2, language_code= 'en', lang_detect_threshold= 50,
                 max_words_unknown_lang= 2, generated_stopwords_percentile= 50, generated_stopwords_max_len= 3, 
                 generated_stopwords_min_freq= 4, stop_words_list = None):
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
        self.stop_words = self.stop_words_make_list(stop_words_file, stop_words_list)
        self.model = self.create_model()
        

    def stop_words_make_list(self, stop_words_file, stop_words_list):
         if self.stop_words_file != None:
            file = open(stop_words_file, 'r', encoding= 'utf-8')
            stop_words = file.readlines()
            file.close()
            return stop_words
         else:
              return stop_words_list
            
    
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


rake = rake_model(stop_words_file= "stopwords/stopwords_en.txt")
text = test_input(6)

keywords = rake.model.apply(text)

for word in keywords:
    print(word)