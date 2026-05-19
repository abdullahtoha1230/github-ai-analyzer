import pandas as pd

def analyze_repos(repos):
    df = pd.DataFrame(repos)

    # Sort by stars (most important metric)
    df_sorted = df.sort_values(by="stars", ascending=False)

    print("\n==============================")
    print("🔥 TOP GITHUB WEB FRAMEWORKS")
    print("==============================\n")

    print(df_sorted[["name", "stars", "forks", "language"]].to_string(index=False))

    print("\n==============================")
    print("📊 BASIC STATS")
    print("==============================")
    print("Total repositories:", len(df))
    print("Most common language:", df["language"].mode()[0])

    return df_sorted
