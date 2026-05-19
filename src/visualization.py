import matplotlib.pyplot as plt

def plot_stars(repos):
    names = [repo["name"] for repo in repos]
    stars = [repo["stars"] for repo in repos]

    plt.figure(figsize=(12, 6))
    plt.bar(names, stars)

    plt.title("GitHub Web Framework Popularity (Stars)")
    plt.xlabel("Framework")
    plt.ylabel("Stars")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
