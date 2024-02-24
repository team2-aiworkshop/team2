from artifici_lda.lda_service import train_lda_pipeline_default
from pprint import pprint

class lda_model:
    def __init__(self, language, stopwords_path, text_path, n_topics=10):
        # Save the model's language and number of topics
        self.language = language
        self.n_topics = n_topics

        # Read every stopword
        stopwords_file = open(stopwords_path, mode='r', encoding='utf-8')

        self.stopwords = stopwords_file.readlines()

        stopwords_file.close()

        # Read every paragraph
        text_file = open(text_path, mode='r', encoding='utf-8')

        self.paragraphs = text_file.read().split('\t')

        text_file.close()

        # Remove all linebreaks from stopwords
        self.stopwords = [i.replace("\n", "") for i in self.stopwords]

        # Remove every empty paragraph and replace every linebreak with a space
        self.paragraphs = [i.replace("\n", " ") for i in self.paragraphs if i != '']

        # Train the pipeline on the given paragraphs
        self.transformed_paragraphs, self.top_paragraphs, self.topic_1_grams, self.topic_2_grams = train_lda_pipeline_default(self.paragraphs, n_topics=self.n_topics, stopwords=self.stopwords, language=self.language)

    def print_info(self, out_path):
        # Open the output file
        out_file = open(out_path, mode='w', encoding='utf-8')

        # Log all relevant info
        pprint(self.transformed_paragraphs, out_file)
        pprint(self.top_paragraphs, out_file)
        pprint(self.topic_1_grams, out_file)
        pprint(self.topic_2_grams, out_file)

        # Close the output file
        out_file.close()
    def print_top_paragraphs(self, out_path):
        # Open the output file
        out_file = open(out_path, mode='w', encoding='utf-8')

        # Log every topic word and its corresponding paragraph
        for i in range(0, self.n_topics):
            out_file.write('############################################\n')
            pprint(self.topic_1_grams[i], out_file)
            pprint(self.topic_2_grams[i], out_file)
            out_file.write(self.top_paragraphs[i])
            out_file.write('\n\n')
        
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
                pprint(self.topic_1_grams[j], out_file)
                pprint(self.topic_2_grams[j], out_file)
                out_file.write(str(self.transformed_paragraphs[i][j]))
                out_file.write('\n')
            
            # Write the full paragraph
            out_file.write(self.paragraphs[i])
            out_file.write('\n\n')
        
        # Close the output file
        out_file.close()

model = lda_model(language='english', stopwords_path='stopwords/stopwords_en.txt', text_path='input_tests/test3.txt', n_topics=10)
model.print_info("info.txt")
model.print_top_paragraphs("top_paragraphs.txt")
model.print_weighted_paragraphs('paragraphs.txt')

