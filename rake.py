from multi_rake import Rake

stop_words_file = open('stopwords/stopwords_en.txt', mode = 'r', encoding= 'utf-8')
stop_words = stop_words_file.readlines()
stop_words_file.close()


rake = Rake(
    min_chars=3,
    max_words=3,
    min_freq=1,
    language_code=None,  # 'en'
    stopwords=stop_words,  # {'and', 'of'}
    lang_detect_threshold=50,
    max_words_unknown_lang=2,
    generated_stopwords_percentile=80,
    generated_stopwords_max_len=3,
    generated_stopwords_min_freq=2,
)





keywords = rake.apply(text)

for i in keywords:
    print(i)