from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from .models import AdProjects

from django.urls import reverse


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

import os
from django.conf import settings



# Use os.path to construct the absolute file path
file_path = os.path.join(settings.BASE_DIR, 'mainApp', 'dbwords', 'brandWords.txt')
extracLocation_path = os.path.join(settings.BASE_DIR, 'mainApp', 'dbwords', 'locationWords.txt')
negativeWords_path = os.path.join(settings.BASE_DIR, 'mainApp', 'dbwords', 'negativeWords.txt')
positiveWords_path = os.path.join(settings.BASE_DIR, 'mainApp', 'dbwords', 'positiveWords.txt')








# Open and read the file
with open(file_path, 'r') as file:
    brand_words = [line.strip() for line in file.readlines()]
    
# Open and read the file
with open(extracLocation_path, 'r') as file:
    extracLocation = [line.strip() for line in file.readlines()]
    
# Open and read the file
with open(negativeWords_path, 'r') as file:
    negative_words = [line.strip() for line in file.readlines()]
    
# Open and read the file
with open(positiveWords_path, 'r') as file:
    positive_words = [line.strip() for line in file.readlines()]
    
    
    
    
    
    

# Create your views here.

def index(request):
    return render(request,"dashboards/analytics.html")


def profile(request):
    return render(request,"profile.html")

def analytics(request):
    return render(request,"dashboards/analytics.html")

def calendar(request):
    return render(request,"calendar/calendar.html")


from django.shortcuts import render
import json
import google.generativeai as genai

# Configure Generative AI
genai.configure(api_key="AIzaSyBxrak2bJZpmiBk2Dd7ZG_BeSUx-ErfdDI")

# Fallback JSON
fallbackjson = {
    "domains": {
        "work_stress": {
            "pain_point": "High-stress jobs leading to burnout, anxiety, and decreased well-being.",
            "hooks": [
                "Reclaim your evenings. SuperMind helps you unwind after a long workday.",
                "Find your focus. SuperMind helps you manage stress and improve concentration.",
                "Unplug and recharge. SuperMind provides tools for stress reduction and better sleep."
            ],
            "ctas": [
                "Start your free 7-day trial of SuperMind today!",
                "Download our free guide: \"5 Simple Stress-Reduction Techniques.\"",
                "Join our supportive community of young professionals."
            ]
        },
        "college_stress": {
            "pain_point": "Academic pressure, social anxieties, and feelings of isolation common among college students.",
            "hooks": [
                "Ace your exams, conquer your anxiety. SuperMind supports your academic journey.",
                "Find your calm amidst the chaos. SuperMind helps you manage college stress.",
                "Connect and thrive. SuperMind fosters a supportive community for students."
            ],
            "ctas": [
                "Get started with SuperMind's free student trial!",
                "Download our free study break meditation.",
                "Join our student community forum."
            ]
        },
        "loneliness_trauma": {
            "pain_point": "Loneliness, social isolation, and the lasting effects of trauma.",
            "hooks": [
                "Reconnect with yourself. SuperMind empowers you to heal and thrive.",
                "Find your support system. SuperMind helps you build community and connection.",
                "Break free from the past. SuperMind offers personalized tools for trauma recovery."
            ],
            "ctas": [
                "Begin your journey to healing with SuperMind's free trial.",
                "Access our free journaling prompts for self-discovery.",
                "Join our compassionate community forum for support and connection."
            ]
        }
    },
    "creative_strategies": [
        "Partner with mental health influencers and organizations to promote SuperMind authentically and reach a wider audience. Run joint giveaways and webinars.",
        "Organize in-person and virtual wellness events featuring SuperMind resources. These could include guided meditation sessions, mindfulness workshops, and community building activities."
    ],
    "visual_mockup_concept": "A social media graphic featuring a serene image (e.g., sunrise, nature scene) overlaid with the strongest hook (\"Reconnect with yourself. SuperMind empowers you to heal and thrive.\") and CTA (\"Begin your journey to healing with SuperMind's free trial.\"). The SuperMind logo and website URL would be subtly incorporated."
}

# Function to fetch and process data
def geminiModelBot(myprompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(myprompt)
        geminiresponse = response.text
        return geminiresponse
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def get_data():
    myprompt = """
    Your marketing campaign prompt here... (Shortened for readability in Django)
    """

    response_text = geminiModelBot(myprompt)
    if response_text:
        try:
            response_text = response_text.replace("```", "")
            response_json = json.loads(response_text.replace("json", ""))
            return response_json
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            return fallbackjson
    else:
        print("No response received from the model.")
        return fallbackjson

# Django view to render the data
def datasources(request):
    data = fallbackjson  # Replace with get_data() if calling the model
    return render(request, 'data-source-list.html', {'data': data})






def usercentric(request):
    """
    Handles the listing of AdProjects and processes form submission if a POST request is made.
    """
    # Fetch all AdProjects records sorted by the latest timestamp (descending)
    ad_projects = AdProjects.objects.all().order_by('-timestamp')
    
    if request.method == "POST":
        # Handle form submission (assuming `campaignTitle` is submitted in POST data)
        campaign_title = request.POST.get('campaignTitle', '').strip()
        keywords = request.POST.get('keywords', '').strip()
        
        features = feature_extractor(str(keywords))
        
        
        myprompt = f"""
        Campaign Title: {campaign_title}
        Keywords: {keywords}
        Features: {features}
        Status: New Project Created

        My Insights:
        This project represents a fresh and innovative approach to addressing the challenges related to {keywords}. By focusing on {features}, it has the potential to engage and resonate with a broad audience, offering tangible solutions to real-world problems. The new project status signals the beginning of an exciting journey, one that can set new trends in the industry. As it moves forward, I believe this initiative will attract attention from key stakeholders and drive significant interest due to its relevance and value in today’s market.
        """
        
        botResponse = geminiModelBot(myprompt)
        
        
        # Create a new AdProjects record
        new_ad_project = AdProjects(
            campaignTitle=campaign_title,
            status="In Progress",
            gptinsights=botResponse,
            metadata=str(features),  # Replace as necessary
            rawTest=str(keywords)  # Replace as necessary
        )
        new_ad_project.save()
        
        # Redirect to the same page after saving the record
        return HttpResponseRedirect(reverse('usercentric'))
    
    # Render the page with the AdProjects data
    return render(request, "usercentric.html", {'ad_projects': ad_projects})


def usercentric_detail(request: HttpRequest, adprojid: int):
    """
    Handles the detailed view of a specific AdProject based on the provided `adprojid`.
    Processes JSON metadata and passes it to the template for rendering.
    """
    # Fetch the specific AdProjects record
    ad_project = get_object_or_404(AdProjects, adprojid=adprojid)
    
    # Convert the rawTest string to JSON
    try:
        metadata = json.loads(ad_project.rawTest)
    except json.JSONDecodeError as e:
        metadata = {}  # Handle JSON errors gracefully

    # Add metadata to the ad_project object for easy access
    ad_project.metadata = metadata

    # Render the page with the specific AdProjects record and metadata
    return render(request, "usercentric_detail.html", {'ad_project': ad_project})







# Supporting Function:


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
