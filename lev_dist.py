from levenshtein_distance import Levenshtein
from lda import lda_model
from pprint import pprint

class levenshtein_model:
    def __init__(self, input_keywords, topic_1_grams, transformed_paragraphs):
        self.keywords = input_keywords
        self.topic_1_grams = topic_1_grams
        self.transformed_paragraphs = transformed_paragraphs

    def distance(self, word1:str, word2:str):
        lev = Levenshtein(word1, word2)
        return lev.distance()
        
    def paragraph_identifier(self):
        topic_weighted_sum = [0] * len(self.topic_1_grams)
        paragraph_weighted_sum = [0] * len(self.transformed_paragraphs)
        for (index, topic) in enumerate(self.topic_1_grams):
            max_product_sum = 0
            weight_sum = 0
            for topic_element in topic:
                max_product = 0
                for keyword in self.keywords:
                    product = (1 / (self.distance(topic_element[0], keyword) + 1)) * topic_element[1]
                    if( product >= max_product):
                        max_product = product
                max_product_sum += max_product
                weight_sum += topic_element[1]
            topic_weighted_sum[index] = max_product_sum / weight_sum
        
        for (index_paragraph, paragraph) in enumerate(self.transformed_paragraphs):
            for (index_topic, topic_weight) in enumerate(paragraph):
                paragraph_weighted_sum[index_paragraph] += (topic_weighted_sum[index_topic] * topic_weight)
        
        max_sum_paragraph_index = 0
        max_sum_paragraph_val = 0

        for (index, paragraph_sum) in enumerate(paragraph_weighted_sum):
            if paragraph_sum >= max_sum_paragraph_val:
                max_sum_paragraph_val = paragraph_sum
                max_sum_paragraph_index = index
        
        return max_sum_paragraph_index


        

