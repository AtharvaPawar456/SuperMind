from fpdf import FPDF
from collections import Counter
import re

# Function to extract 20 user insights from raw text
def generateInsights(rawText):
    """
    Extracts and summarizes insights from raw text.
    Input:
        rawText (str): The input raw text.
    Output:
        insights (list): List of key insights.
    """
    # Clean the text by removing non-alphanumeric characters and converting to lowercase
    cleanText = re.sub(r'\W+', ' ', rawText.lower())
    words = cleanText.split()

    # Use Counter to get the most common words as insights
    wordCounts = Counter(words)

    # Extract the 20 most common words or phrases as insights
    insights = [item[0] for item in wordCounts.most_common(20)]

    return insights

# Function to generate a PDF report
def generateReport(insights, outputPath="insights_report.pdf"):
    """
    Generates a PDF report of the insights.
    Input:
        insights (list): List of insights to include in the report.
        outputPath (str): File path to save the PDF report.
    Output:
        None
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Insights Report", ln=True, align='C')
    pdf.ln(10)

    for i, insight in enumerate(insights, start=1):
        pdf.multi_cell(0, 10, txt=f"{i}. {insight}")
        pdf.ln(5)

    pdf.output(outputPath)
    print(f"Report generated: {outputPath}")

# Main function to run the program
def main():
    # Sample raw text
    rawText = """
    
    Stress is a natural response of the body to external pressures, challenges, or threats, which can trigger a variety of physical, mental, and emotional reactions. In small doses, stress can be beneficial, helping individuals stay alert, focused, and motivated to overcome challenges. This type of stress is often referred to as "eustress" and can enhance performance, increase productivity, and help individuals meet deadlines or achieve goals. However, when stress becomes chronic or excessive, it can have negative effects on both physical and mental health. Chronic stress is often called "distress" and can lead to a range of serious health issues, including heart disease, high blood pressure, diabetes, anxiety, depression, and a weakened immune system.

    The body’s stress response is governed by the autonomic nervous system and the release of stress hormones such as adrenaline and cortisol. When a person perceives a threat, the body enters a “fight-or-flight” mode, preparing the body to either confront or flee from the danger. This results in increased heart rate, rapid breathing, muscle tension, and heightened awareness. These physical changes are adaptive in situations where immediate action is required, such as when faced with a dangerous predator or during a stressful work deadline. However, when stress is prolonged and the body is continuously exposed to these physiological changes, it can have detrimental effects on health.

    One of the most noticeable effects of stress is its impact on mental health. Chronic stress can lead to feelings of anxiety, irritability, and emotional exhaustion. It may also contribute to mood disorders such as depression and post-traumatic stress disorder (PTSD). When stress levels are high, individuals may have difficulty concentrating, making decisions, or remembering important tasks. The constant state of alertness can impair cognitive function, making it harder to think clearly and logically. Over time, this can reduce productivity and negatively affect personal relationships, as individuals may become withdrawn or more prone to conflict.

    Physically, stress can cause a variety of symptoms. Common physical manifestations of stress include headaches, digestive issues, muscle tension, and sleep disturbances. People under chronic stress are more likely to experience problems with their cardiovascular system, such as high blood pressure or heart disease. Stress has also been linked to digestive problems like irritable bowel syndrome (IBS) or acid reflux, as the digestive system becomes disrupted during periods of high stress. Moreover, individuals may resort to unhealthy coping mechanisms, such as overeating, smoking, or excessive alcohol consumption, which can further exacerbate the negative effects of stress.

    In addition to its physical and mental toll, stress can have an impact on a person’s social life. Chronic stress may lead to withdrawal from social interactions, as individuals may feel overwhelmed or unable to engage in conversations or activities. Over time, this isolation can deepen feelings of loneliness and contribute to the worsening of mental health issues. Relationships with friends, family, and colleagues may suffer as stress affects a person’s ability to communicate and empathize effectively.

    Managing stress is crucial for maintaining both physical and mental well-being. Various techniques and strategies can help alleviate stress and prevent its negative consequences. Regular physical activity, such as walking, yoga, or swimming, is one of the most effective ways to reduce stress. Exercise promotes the release of endorphins, which are natural mood boosters that help counteract the effects of stress. Practicing mindfulness and meditation can also be beneficial in managing stress. These practices help individuals stay present in the moment, calm their minds, and regulate their emotional responses. Additionally, maintaining a healthy lifestyle, which includes getting adequate sleep, eating a balanced diet, and staying hydrated, is essential for managing stress effectively.

    In conclusion, stress is a complex and multifaceted experience that affects individuals in different ways. While short-term stress can be motivating and energizing, chronic stress can have serious consequences for both physical and mental health. Recognizing the signs of stress and adopting healthy coping mechanisms are essential for managing stress and reducing its impact. By engaging in physical activity, practicing relaxation techniques, and maintaining a balanced lifestyle, individuals can mitigate the harmful effects of stress and improve their overall well-being. Ultimately, stress management is about finding a balance that allows individuals to cope with life’s challenges without compromising their health or happiness.
    """
        
    
    print("Extracting insights...")
    insights = generateInsights(rawText)

    print("\nGenerated Insights:")
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")

    print("\nGenerating PDF report...")
    generateReport(insights)

if __name__ == "__main__":
    main()
