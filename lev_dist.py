from levenshtein_distance import Levenshtein
from pprint import pprint

class levenshtein_model:
    def __init__(self, input_keywords, topic_list):
        self.input_keywords = input_keywords
        self.topic_list = topic_list

    def word_to_word_distance(self, word1:str, word2:str):
        lev = Levenshtein(word1, word2)
        return lev.distance()
        
    def keywords_to_topic(self):
        topic_match = {}

        for keyword in self.input_keywords:
            min_dist = 9999999999999999999999999999999999
            min_dist_topics = []
            for topic in self.topic_list:
                dist = self.word_to_word_distance(keyword, topic)
                if dist < min_dist:
                    min_dist_topics = [topic]
                    min_dist = dist
                elif dist == min_dist:
                    min_dist_topics.append(topic)
            
            for topic in min_dist_topics:
                if topic_match.get(topic, None) == None:
                    topic_match[topic] = [keyword]
                else:
                    topic_match[topic].append(keyword)
        
        max_keyword_count = 0
        best_topic = ''

        for topic in topic_match:
            if(len(topic_match[topic]) > max_keyword_count):
                max_keyword_count = len(topic_match[topic])
                best_topic = topic

        return best_topic


lev = levenshtein_model(['nucleus', 'membrane', 'type', 'ribosomes', 'proteins', 'golgi apparatus', 'vacuoles', 'lysosomes'], ['cellular', 'cartasdasda'])

topic = lev.keywords_to_topic()
pprint(topic)

        

