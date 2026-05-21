import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_insights(df):

    repo_text = df.to_string(index=False)

    prompt = f"""
You are a senior tech analyst.

Analyze this GitHub repository dataset:

{repo_text}

Return:
- key technology trends
- dominant languages
- ecosystem insights
- short summary
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        top_language = (
            df["language"]
            .mode()[0]
        )

        top_repo = (
            df.sort_values(
                by="stars",
                ascending=False
            )
            .iloc[0]["name"]
        )

        average_stars = int(
            df["stars"].mean()
        )

        return f"""
AI service is currently unavailable.

Local  Analysis:

• Most dominant language: {top_language}

• Most popular repository: {top_repo}

• Average repository stars: {average_stars}

• The ecosystem shows strong interest in scalable web technologies and open-source frameworks.

• Python and JavaScript ecosystems remain highly dominant in modern development.
"""
