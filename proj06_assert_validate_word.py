from proj06 import validate_word

stopwords = {'same', 'anything', "isn't", 'have', "what's", 'few', "there's", 'aint', 'this', "won't", 'ought', "he's", 'myself', 'nothing', 'with', 'while', 'on', 'are', "mustn't", 'more', 'our', 'their', "wasn't", "i'll", 'what', 'yourselves', 'again', 'ever', 'it', 'whom', 'other', 'am', 'into', "she's", 'ourselves', 'so', 'any', 'the', 'in', 'you', 'everyone', 'against', 'here', "we'll", "we're", 'should', "i've", 'some', 'cannot', 'off', 'above', 'yourself', "let's", 'because', 'by', 'can', 'him', "that's", 'all', "weren't", 'just', 'my', "you'll", 'be', "it's", 'themselves', 'would', 'than', 'below', "i'd", 'they', 'always', 'having', 'nor', 'hers', 'up', 'were', "doesn't", 'these', "you're", 'ours', 'further', 'us', "why's", 'which', 'through', "didn't", "wouldn't", 'as', 'of', 'too', 'both', 'still', 'every', 'she', "aren't", 'under', 'how', "when's", 'his', 'to', "don't", "we'd", 'from', "he'll", "can't", "here's", "they've", 'who', 'yours', 'himself', 'never', "how's", 'them', 'do', "they'd", 'its', 'before', 'there', 'we', 'me', 'for', 'been', 'very', 'when', "she'd", "couldn't", 'each', "we've", 'her', "haven't", 'i', 'until', 'at', 'good', "shouldn't", "ain't", 'no', 'such', 'those', 'but', 'your', 'will', 'where', 'between', 'if', 'only', 'about', "you've", "shan't", 'out', 'around', "she'll", 'hey', 'and', 'did', "hasn't", 'now', 'that', "he'd", 'why', 'herself', 'theirs', 'being', "who's", 'once', "they're", 'own', "hadn't", 'already', 'an', "i'm", 'down', 'has', "you'd", 'he', 'not', 'a', 'was', "where's", 'had', "they'll", 'does', 'or', 'well', 'could', 'oh', 'doing', 'over', 'during', 'most', 'itself', 'after', 'then', 'is'}

#["you", "love", "all!", "2"]:
print("you", ":" , validate_word("you", stopwords))
assert validate_word("you", stopwords) == False
print("love", ":" , validate_word("love", stopwords))
assert validate_word("love", stopwords) == True
print("all!", ":" , validate_word("all!", stopwords))
assert validate_word("all!", stopwords) == False
print("2", ":" , validate_word("2", stopwords))
assert validate_word("2", stopwords) == False
