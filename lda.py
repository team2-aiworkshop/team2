from artifici_lda.lda_service import *
from artifici_lda.data_utils import *
from artifici_lda.logic.stop_words_remover import *
from artifici_lda.logic.stemmer import *
from artifici_lda.logic.count_vectorizer import *
from artifici_lda.logic.lda import*
from sklearn.pipeline import Pipeline

from pprint import pprint

class lda_model:
    def __init__(self, language, stopwords_path, text_path, n_topics_per_paragraph=3):
        # Save the model's language and number of topics
        self.language = language

        # Read every stopword
        stopwords_file = open(stopwords_path, mode='r', encoding='utf-8')

        self.stopwords = stopwords_file.readlines()

        stopwords_file.close()

        # Read every paragraph
        text_file = open(text_path, mode='r', encoding='utf-8')

        self.paragraphs = text_file.read().split('\t')

        text_file.close()

        # Remove all linebreaks from stopwords
        self.stopwords = [i.replace('\n', '') for i in self.stopwords]

        # Remove every empty paragraph and replace every linebreak with a space
        self.paragraphs = [i.replace('\n', ' ') for i in self.paragraphs if i != '']

        # Set the number of topics
        self.n_topics = n_topics_per_paragraph * len(self.paragraphs)

        # Set the LDA pipeline's params
        lda_pipeline_params = {
            'stopwords__stopwords': self.stopwords,
            'stemmer__language': self.language,
            'count_vect__max_df': 1.0,
            'count_vect__min_df': 1,
            'count_vect__ngram_range': (1, 2),
            'count_vect__strip_accents': None,
            'lda__n_components': self.n_topics,
            'lda__max_iter': 750,
            'lda__learning_decay': 0.5,
            'lda__learning_method': 'online',
            'lda__learning_offset': 10,
            'lda__batch_size': 25,
            'lda__n_jobs': -1,
        }

        # Create and fit the LDA pipeline
        self.lda_pipeline = Pipeline([
            ('stopwords', StopWordsRemover()),
            ('stemmer', Stemmer()),
            ('count_vect', CountVectorizer()),
            ('lda', LDA())
        ]).set_params(**lda_pipeline_params)

        # Get the pipeline's transformed and top paragraphs
        self.transformed_paragraphs = self.lda_pipeline.fit_transform(self.paragraphs)
        self.top_paragraphs = get_top_comments(self.paragraphs, self.transformed_paragraphs)

        # Get the topic words and their weightings
        topic_words = self.lda_pipeline.inverse_transform(Xt=None)
        topic_weighting = get_word_weightings(self.lda_pipeline)
        topic_words_weighting = link_topics_and_weightings(topic_words, topic_weighting)

        # Split the topic words into 1-grams
        self.topic_1_grams, self.topic_2_grams = split_1_grams_from_n_grams(topic_words_weighting)

    def get_lda_pipeline(self):
        return self.lda_pipeline
    def get_topic_1_grams(self):
        return self.topic_1_grams
    def get_topic_2_grams(self):
        return self.topic_2_grams
    def get_paragraphs(self):
        return self.paragraphs
    def get_transformed_paragraphs(self):
        return self.transformed_paragraphs

    def print_topics(self, out_path):
        # Open the output file
        out_file = open(out_path, mode='w', encoding='utf-8')

        # Log each topic's 1-grams and 2-grams
        for i in range(0, self.n_topics):
            out_file.write('############################################ Topic ')
            out_file.write(str(i + 1))
            out_file.write('\n')
            pprint(self.topic_1_grams[i], out_file)
            pprint(self.topic_2_grams[i], out_file)
            out_file.write('\n')

        # Close the output file
        out_file.close()
    def print_weighted_paragraphs(self, out_path):
        # Open the output file
        out_file = open(out_path, mode='w', encoding='utf-8')

        # Log every paragraph with each topic's weight
        for i in range(0, len(self.paragraphs)):
            # Write the file's topic weights
            out_file.write('############################################\n')
            for j in range(0, self.n_topics):
                out_file.write('Topic ')
                out_file.write(str(j + 1))
                out_file.write(': ')
                out_file.write(str(self.transformed_paragraphs[i][j]))
                out_file.write('\n')
            
            # Write the full paragraph
            out_file.write(self.paragraphs[i])
            out_file.write('\n\n')
        
        # Close the output file
        out_file.close()

if __name__ == "__main__":
    # Create a test model and get its info
    model = lda_model(language='english', stopwords_path='stopwords/stopwords_en.txt', text_path='input_tests/test2.txt')

    model.print_topics('topics.txt')
    model.print_weighted_paragraphs('paragraphs.txt')

