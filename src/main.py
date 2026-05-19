import pandas as pd

from github_api import fetch_repos
from ai_insights import generate_ai_insights

print("🚀 GitHub AI Analyzer Starting...\n")

# 1. Fetch GitHub data
repos = fetch_repos()

# 2. Convert to DataFrame
df = pd.DataFrame(repos)

# 3. Show basic data
print(df[["name", "stars", "language"]])

print("\n==============================")
print("🤖 AI INSIGHTS")
print("==============================\n")

# 4. Get AI insights safely
insights = generate_ai_insights(df)

# 5. Fallback if AI fails
if isinstance(insights, str) and "Error" in insights:
    print("⚠️ AI unavailable — using fallback insights\n")

    insights = [
        "Python is the most common language in top GitHub repositories.",
        "Web frameworks dominate the open-source ecosystem.",
        "FastAPI, Django, and Flask are leading Python frameworks.",
        "High-star projects indicate strong community adoption trends."
    ]

# 6. Print results
if isinstance(insights, list):
    for i in insights:
        print("-", i)
else:
    print(insights)
