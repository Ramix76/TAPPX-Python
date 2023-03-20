from multi_rake import Rake
import json

def articles_keywords():

    articles_text = open('articles.json')
    data = json.load(articles_text)
    rake = Rake()
    articles_keywords = [rake.apply(data[id]['text']) for id in data]
    print(f"\n{articles_keywords[0]}\n")
    
def videos_keywords():
    videos_text = open('videos.json')
    data = json.load(videos_text)
    rake = Rake()
    video_keywords = [rake.apply(data[id]['text']) for id in data]
    print(f"\n{video_keywords[0]}\n")

__name__ == '__main__'
articles_keywords()
videos_keywords()
