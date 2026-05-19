from github_api import fetch_repos
from analyzer import analyze_repos
from visualization import plot_stars

def main():
    print("\n🚀 GitHub AI Analyzer Starting...\n")

    repos = fetch_repos("web framework", 10)

    if not repos:
        print("No data fetched")
        return

    analyze_repos(repos)

    print("\n📊 Generating visualization...")
    plot_stars(repos)

    print("\n✅ Done Successfully")

if __name__ == "__main__":
    main()
