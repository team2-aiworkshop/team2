from keywords import keyword_identifier
from lev_dist import levenshtein_model
from lda import lda_model
from app import application
import sys

app : application
lda_m : lda_model
levenshtein_m : levenshtein_model
kw_identifier : keyword_identifier

def load_file_callback():
    global lda_m
    global levenshtein_m

    # Create the new LDA model and Levenshtein model
    app.get_window().set_load_button_loading()

    lda_m = lda_model(language='english', stopwords_path='stopwords/stopwords_en.txt', text_path=app.get_window().get_file_path())
    levenshtein_m = levenshtein_model(topic_1_grams=lda_m.get_topic_1_grams(), transformed_paragraphs=lda_m.get_transformed_paragraphs())

    app.get_window().set_load_button_loaded()
def generate_answer_callback():
    global lda_m
    global levenshtein_m
    
    # Extract the keywords from the current question
    keywords = kw_identifier.get_keywords(app.get_window().get_question())

    # Get the best paragraphs
    best_paragraphs = levenshtein_m.get_best_paragraphs(keywords)

    # Save the best paragraphs to a string
    best_paragraphs_str = ''
    for (index, paragraph) in enumerate(best_paragraphs):
        best_paragraphs_str += lda_m.paragraphs[paragraph]
        if index != len(best_paragraphs) - 1:
            best_paragraphs_str += '\n\n'
    
    # Display the best paragraphs
    app.get_window().set_answer(best_paragraphs_str)

if __name__ == "__main__":
    # Create the keyword identifier
    kw_identifier = keyword_identifier(stopwords_path='stopwords/stopwords_en.txt')

    # Create and run the application
    app = application(sys.argv, load_file_callback=load_file_callback, generate_answer_callback=generate_answer_callback)
    sys.exit(app.run())