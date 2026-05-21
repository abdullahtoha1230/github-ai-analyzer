import pandas as pd

from github_api import fetch_repos
from analyzer import analyze_repositories
from ai_insights import generate_ai_insights

from visualization import (
    plot_language_distribution,
    plot_top_repositories
)

print("🚀 GitHub AI Analyzer Starting...\n")

search_query = input(
    "Enter GitHub topic to analyze: "
)

repos = fetch_repos(search_query)

df = pd.DataFrame(repos)
df.to_csv("github_repositories.csv", index=False)

print("\n✅ Data exported to github_repositories.csv")

print(df[["name", "stars", "language"]])

print("\n==============================")
print("📊 ANALYTICS")
print("==============================\n")

analysis = analyze_repositories(df)

print(f"Total repositories: {analysis['total_repositories']}")
print(f"Top language: {analysis['top_language']}")
print(f"Average stars: {analysis['average_stars']}")

print(
    f"Top repository: "
    f"{analysis['top_repository']['name']}"
)

print(
    f"Stars: {analysis['top_repository']['stars']}"
)

print(
    f"Forks: {analysis['top_repository']['forks']}"
)

print(
    f"Repository Score: "
    f"{analysis['top_repository']['score']}"
)

print("\nRecommended for Beginners:")

print(
    f"{analysis['beginner_friendly']['name']} "
    f"with {analysis['beginner_friendly']['forks']} forks"
)

print("\nMost Active Repository:")

print(
    f"{analysis['most_active']['name']}"
)

# Charts
plot_language_distribution(df)

plot_top_repositories(df)

print("\n==============================")
print("🤖 AI INSIGHTS")
print("==============================\n")

insights = generate_ai_insights(df)

print(insights)
