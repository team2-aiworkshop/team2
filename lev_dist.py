from levenshtein_distance import Levenshtein

class levenshtein_model:
    def __init__(self, topic_1_grams, transformed_paragraphs):
        self.topic_1_grams = topic_1_grams
        self.transformed_paragraphs = transformed_paragraphs

    def distance(self, word1:str, word2:str):
        lev = Levenshtein(word1, word2)
        return lev.distance()
    def inv_levenshtein_distance(self, word1:str, word2:str):
        return 1 / (self.distance(word1, word2) + 0.1)
        
    def get_best_paragraphs(self, keywords, val_count=3):
        # Calculate the weighted sum for every topic
        topic_weighted_sum = [0] * len(self.topic_1_grams)
        for (index, topic) in enumerate(self.topic_1_grams):
            max_product_sum = 0
            weight_sum = 0

            # Loop through the current topic's 1-grams
            for topic_element in topic:
                # Find the best matching keyword
                max_product = 0
                for keyword in keywords:
                    product = self.inv_levenshtein_distance(topic_element[0], keyword)
                    if product >= max_product:
                        max_product = product
                
                # Add the best product to the topic's sum
                max_product_sum += max_product
                weight_sum += topic_element[1]
            
            # Calculate the topic's weighted sum
            topic_weighted_sum[index] = max_product_sum / weight_sum
        
        # Calculate the weighted sum for every paragraph
        paragraph_weighted_sum = [(0, 0)] * len(self.transformed_paragraphs)
        for (index_paragraph, paragraph) in enumerate(self.transformed_paragraphs):
            # Add every topic to the sum based on its weight
            weighted_sum = 0
            for (index_topic, topic_weight) in enumerate(paragraph):
                weighted_sum += (topic_weighted_sum[index_topic] * topic_weight)
            
            paragraph_weighted_sum[index_paragraph] = (index_paragraph, weighted_sum)
        
        # Sort the sum array
        paragraph_weighted_sum.sort(key=lambda x: x[1])
        
        # Return the last values
        return [paragraph_weighted_sum[i][0] for i in range(len(paragraph_weighted_sum) - val_count, len(paragraph_weighted_sum))]