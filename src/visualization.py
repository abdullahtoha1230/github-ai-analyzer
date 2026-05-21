import matplotlib.pyplot as plt


def plot_language_distribution(df):

    language_counts = df["language"].value_counts()

    plt.figure(figsize=(8, 8))

    language_counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Language Distribution")

    plt.ylabel("")

    plt.show()


def plot_top_repositories(df):

    top_repos = df.sort_values(
        by="stars",
        ascending=False
    ).head(5)

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_repos["name"],
        top_repos["stars"]
    )

    plt.title("Top GitHub Repositories")

    plt.xlabel("Repository")

    plt.ylabel("Stars")

    plt.xticks(rotation=15)

    plt.show()
