from multi_rake import Rake
import json
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_json_text():
    with open('articles.json', 'r') as f:
        data = json.load(f)
    for k, v in data.items():
        if 'text' in v:
            # convert text to lowercase
            v['text'] = v['text'].lower()
            # remove punctuations
            v['text'] = v['text'].translate(str.maketrans('', '', string.punctuation))
            # remove numbers
            v['text'] = re.sub(r'\d+', '', v['text'])
            # remove extra whitespaces
            v['text'] = ' '.join(v['text'].split())
    with open('articles_processed.json', 'w') as f:
        json.dump(data, f)

def articles_keywords_to_string(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    rake = Rake()
    articles_keywords = {}
    for id in data:
        keywords = rake.apply(data[id]['text'])
        keywords_string = ", ".join([kw[0] for kw in keywords])
        articles_keywords[id] = keywords_string
    for id, keywords_string in articles_keywords.items():
        print(f"Keywords for article {id}: {keywords_string}")
    return articles_keywords

def vectorize_text(text):
    tfidf_vectorizer = TfidfVectorizer(max_features = 10)
    doc_vec = tfidf_vectorizer.fit_transform([text])
    df = pd.DataFrame(doc_vec.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    print(df)

preprocess_json_text()        
articles_keywords = articles_keywords_to_string('articles_processed.json')
for article_id, keywords_string in articles_keywords.items():
    print(f"\nKeywords for article {article_id}:")
    vectorize_text(keywords_string)


