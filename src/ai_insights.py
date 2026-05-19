import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_ai_insights(df):

    # Clean + sort data for better AI input
    df = df.dropna(subset=["language"])
    df = df.sort_values(by="stars", ascending=False)

    repo_text = df.to_string(index=False)

    prompt = f"""
You are a senior tech analyst.

Analyze this GitHub repository dataset:

{repo_text}

Return ONLY valid JSON in this format:

{{
  "trends": [
    "trend 1",
    "trend 2",
    "trend 3"
  ],
  "languages": {{
    "Python": 0,
    "JavaScript": 0,
    "Go": 0
  }},
  "insights": [
    "insight 1",
    "insight 2"
  ],
  "summary": "short overall summary"
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
