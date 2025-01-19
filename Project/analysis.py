import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import io
import base64

# Load external data (words for locations, brands, negative, and positive)
with open('locationWords.txt', 'r') as file:
    extracLocation = [line.strip() for line in file.readlines()]

with open('brandWords.txt', 'r') as file:
    brand_words = [line.strip() for line in file.readlines()]

with open('negativeWords.txt', 'r') as file:
    negative_words = [line.strip() for line in file.readlines()]

with open('positiveWords.txt', 'r') as file:
    positive_words = [line.strip() for line in file.readlines()]


# Individual feature extraction functions

def showgenerate_word_cloud(text: str):
    """Generates and displays a word cloud from the given text."""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
def generate_word_cloud(text: str):
    """Generates a word cloud from the given text and returns the image as a base64 string."""
    
    # Generate the word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Save the word cloud image to a BytesIO object (in memory)
    img = io.BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img.seek(0)  # Rewind the BytesIO object to the start
    
    # Encode the image to base64
    img_base64 = base64.b64encode(img.read()).decode('utf-8')
    
    return img_base64


def top_10_frequent_words(text: str):
    """Returns the top 10 most frequent words and their word counts."""
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(10)


def top_10_topics(texts: list, n_topics: int = 10):
    """Perform topic modeling using LDA and return the top 10 topics with their words."""
    if isinstance(texts, str):
        texts = [texts]
        
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    
    lda = LatentDirichletAllocation(n_components=n_topics)
    lda.fit(X)
    
    words = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda.components_):
        topic_words = [words[i] for i in topic.argsort()[:-11:-1]]
        topics.append(f"Topic {topic_idx + 1}: " + ", ".join(topic_words))
    
    return topics


def word_frequency(text: str):
    """Returns a dictionary of all words and their frequency, sorted by frequency (high to low)."""
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return dict(word_counts.most_common())


def extract_brands(text: str):
    """Extracts a list of brand names (organizations) from the text using NER."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    brands = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    return list(set(brands))  # Remove duplicates


def find_brand_words_in_text(text, brand_words):
    """Find brand words that are present in the text."""
    words_in_text = [word.lower() for word in text.split()]
    found_brand_words = [word for word in brand_words if word.lower() in words_in_text]
    return found_brand_words


def extract_locations(text: str, extra_locations=None):
    """Extracts a list of location names from the text using NER and adds extra locations."""
    if extra_locations is None:
        extra_locations = []
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    
    for loc in extra_locations:
        if any(loc.lower() in word.lower() for word in text.split()):
            locations.append(loc)
    
    return list(set(locations))


def extract_persons(text: str):
    """Extracts a list of well-known persons' names from the text using NER."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    persons = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    return list(set(persons))


def analyze_sentiment(text: str):
    """Analyzes the sentiment of the text and returns positive, negative, or neutral sentiment."""
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'


def extract_actions(text: str):
    """Extracts a list of verbs (actions) from the text using NER and POS tagging."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    actions = [token.text for token in doc if token.pos_ == 'VERB']
    return list(set(actions))  # Remove duplicates


def matching_keywords(text: str, keywords: list):
    """Returns a list of keywords from the given list that are found in the text."""
    words = re.findall(r'\w+', text.lower())
    matching = [keyword for keyword in keywords if keyword.lower() in words]
    return matching


# Main feature extraction function

def feature_extractor(text: str, keywords: list = None):
    """Extracts various features from the input text and returns a structured dictionary."""
    if keywords is None:
        keywords = ["stress", "alone", "etc"]  # Default keyword list
    
    # Call the individual feature extraction functions
    word_cloud = generate_word_cloud(text)  # Displays the word cloud
    top_words = top_10_frequent_words(text)
    topics = top_10_topics([text])
    all_word_frequency = word_frequency(text)
    brands = find_brand_words_in_text(text, brand_words) + extract_brands(text)
    locations = extract_locations(text, extracLocation)
    persons = extract_persons(text)
    sentiment = analyze_sentiment(text)
    actions = extract_actions(text)
    matched_keywords = matching_keywords(text, keywords)
    
    # Compile everything into a dictionary
    features = {
        "top_10_frequent_words": top_words,
        "top_10_topics": topics,
        "all_word_frequency": all_word_frequency,
        "brands": brands,
        "locations": locations,
        "persons": persons,
        "sentiment": sentiment,
        "actions": actions,
        "matched_keywords": matched_keywords,
        "word_cloud": word_cloud
    }
    
    return features


# Example usage
rawText = """
Stress is a natural response of the body to external pressures, challenges, or threats, which can trigger a variety of physical, mental, and emotional reactions. In small doses, stress can be beneficial, helping individuals stay alert, focused, and motivated to overcome challenges. This type of stress is often referred to as "eustress" and can enhance performance, increase productivity, and help individuals meet deadlines or achieve goals. However, when stress becomes chronic or excessive, it can have negative effects on both physical and mental health. Chronic stress is often called "distress" and can lead to a range of serious health issues, including heart disease, high blood pressure, diabetes, anxiety, depression, and a weakened immune system.

The body’s stress response is governed by the autonomic nervous system and the release of stress hormones such as adrenaline and cortisol. When a person perceives a threat, the body enters a “fight-or-flight” mode, preparing the body to either confront or flee from the danger. This results in increased heart rate, rapid breathing, muscle tension, and heightened awareness. These physical changes are adaptive in situations where immediate action is required, such as when faced with a dangerous predator or during a stressful work deadline. However, when stress is prolonged and the body is continuously exposed to these physiological changes, it can have detrimental effects on health.

One of the most noticeable effects of stress is its impact on mental health. Chronic stress can lead to feelings of anxiety, irritability, and emotional exhaustion. It may also contribute to mood disorders such as depression and post-traumatic stress disorder (PTSD). When stress levels are high, individuals may have difficulty concentrating, making decisions, or remembering important tasks. The constant state of alertness can impair cognitive function, making it harder to think clearly and logically. Over time, this can reduce productivity and negatively affect personal relationships, as individuals may become withdrawn or more prone to conflict.

Physically, stress can cause a variety of symptoms. Common physical manifestations of stress include headaches, digestive issues, muscle tension, and sleep disturbances. People under chronic stress are more likely to experience problems with their cardiovascular system, such as high blood pressure or heart disease. Stress has also been linked to digestive problems like irritable bowel syndrome (IBS) or acid reflux, as the digestive system becomes disrupted during periods of high stress. Moreover, individuals may resort to unhealthy coping mechanisms, such as overeating, smoking, or excessive alcohol consumption, which can further exacerbate the negative effects of stress.

In addition to its physical and mental toll, stress can have an impact on a person’s social life. Chronic stress may lead to withdrawal from social interactions, as individuals may feel overwhelmed or unable to engage in conversations or activities. Over time, this isolation can deepen feelings of loneliness and contribute to the worsening of mental health issues. Relationships with friends, family, and colleagues may suffer as stress affects a person’s ability to communicate and empathize effectively.

Managing stress is crucial for maintaining both physical and mental well-being. Various techniques and strategies can help alleviate stress and prevent its negative consequences. Regular physical activity, such as walking, yoga, or swimming, is one of the most effective ways to reduce stress. Exercise promotes the release of endorphins, which are natural mood boosters that help counteract the effects of stress. Practicing mindfulness and meditation can also be beneficial in managing stress. These practices help individuals stay present in the moment, calm their minds, and regulate their emotional responses. Additionally, maintaining a healthy lifestyle, which includes getting adequate sleep, eating a balanced diet, and staying hydrated, is essential for managing stress effectively.

In conclusion, stress is a complex and multifaceted experience that affects individuals in different ways. While short-term stress can be motivating and energizing, chronic stress can have serious consequences for both physical and mental health. Recognizing the signs of stress and adopting healthy coping mechanisms are essential for managing stress and reducing its impact. By engaging in physical activity, practicing relaxation techniques, and maintaining a balanced lifestyle, individuals can mitigate the harmful effects of stress and improve their overall well-being. Ultimately, stress management is about finding a balance that allows individuals to cope with life’s challenges without compromising their health or happiness.

Mumbai, dadar, virar, pune

ambani, elon musk, tesla , shaun, atharva, Ahmedabad

"""
features = feature_extractor(rawText)

# Convert to JSON-like structure
import json
features_json = json.dumps(features, indent=4)

# print(features_json)

# Save the JSON string to a file
with open('analysis.json', 'w') as file:
    file.write(features_json)

print("JSON data has been written to analysis.json.")