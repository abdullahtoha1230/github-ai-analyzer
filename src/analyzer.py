def analyze_repositories(df):

    analysis = {}

    analysis["total_repositories"] = len(df)

    analysis["top_language"] = (
        df["language"]
        .mode()[0]
    )

    analysis["average_stars"] = int(
        df["stars"].mean()
    )

    analysis["top_repository"] = (
        df.sort_values(
            by="stars",
            ascending=False
        ).iloc[0]
    )

    analysis["most_forked"] = (
        df.sort_values(
            by="forks",
            ascending=False
        ).iloc[0]
    )

    analysis["most_active"] = (
        df.sort_values(
            by="updated_at",
            ascending=False
        ).iloc[0]
    )

    return analysis