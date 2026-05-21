import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def fetch_repos(query="web framework", per_page=10):

    headers = {
        "Accept": "application/vnd.github+json"
    }

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }

    response = requests.get(
        GITHUB_API_URL,
        headers=headers,
        params=params
    )

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("ERROR:", response.text)
        return []

    data = response.json()

    repos = []

    for item in data["items"]:

        repos.append({

            "name": item["name"],

            "stars": item["stargazers_count"],

            "forks": item["forks_count"],

            "language": item["language"],

            "updated_at": item["updated_at"],

            "url": item["html_url"]

        })

    return repos


if __name__ == "__main__":

    repos = fetch_repos()

    for r in repos:
        print(r)