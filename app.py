from flask import Flask, render_template_string, request 
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

from src.github_api import fetch_repos
from src.analyzer import analyze_repositories
from src.ai_insights import generate_ai_insights

app = Flask(__name__)


def generate_chart(df):

    language_counts = df["language"].value_counts()

    plt.figure(figsize=(8, 5))

    language_counts.plot(kind="bar")

    plt.title("Programming Languages")

    plt.xlabel("Language")

    plt.ylabel("Repositories")

    buffer = io.BytesIO()

    plt.savefig(buffer, format="png")

    buffer.seek(0)

    image_png = buffer.getvalue()

    buffer.close()

    graph = base64.b64encode(image_png)

    graph = graph.decode("utf-8")

    plt.close()

    return graph


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>

<head>

    <title>GitHub AI Analyzer</title>

    <style>

        body {
            font-family: Arial;
            margin: 40px;
            background: #121212;
            color: white;
        }

        h1 {
            color: white;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            background: #1e1e1e;
            color: white;
        }

        th, td {
            border: 1px solid #333;
            padding: 12px;
            text-align: left;
        }

        th {
            background: #333;
            color: white;
        }

        .card {
            background: #1e1e1e;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
        }

        input {
            padding: 10px;
            width: 300px;
            border-radius: 8px;
            border: none;
            background: #2a2a2a;
            color: white;
        }

        button {
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            background: #333;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #555;
        }

        img {
            max-width: 100%;
            border-radius: 10px;
        }

    </style>

</head>

<body>

    <h1>🚀 GitHub AI Analyzer</h1>
    <h3>
    Results for: "{{ query }}"
    </h3>

    <form method="GET">

    <input
        type="text"
        name="query"
        placeholder="Search GitHub topic..."
    >

    <button type="submit">
        Search
    </button>

    <button
        type="button"
        id="downloadBtn"
    >
        Download CSV
    </button>

     </form>

<script>

         document.getElementById("downloadBtn").addEventListener(
         "click",
         function () {

        let answer = confirm(
            "Do you want to download the CSV report?"
        );

        if (answer) {

            window.location.href =
                "/download?query={{ query }}";

        }

    }
);

</script>

    </form>

    <br>

    <div class="card">

    <h2>📊 Analytics</h2>

    <p>
        <b>Total repositories:</b>
        {{ analysis.total_repositories }}
    </p>

    <p>
        <b>Top language:</b>
        {{ analysis.top_language }}
    </p>

    <p>
        <b>Average stars:</b>
        {{ analysis.average_stars }}
    </p>

</div>


<div class="card">

    <h2>🤖 AI Insights</h2>

    <p style="line-height: 1.8;">
        {{ insights }}
    </p>


</div>


 <div class="card">

    <h2>🔥 Highlights</h2>

    <p>
        ⭐ <b>Top Repository:</b>
        {{ analysis.top_repository.name }}
    </p>

    <p>
        🍴 <b>Most Forked:</b>
        {{ analysis.most_forked.name }}
    </p>

    <p>
        🚀 <b>Most Active:</b>
        {{ analysis.most_active.name }}
    </p>

</div>


        <p>
            <b>Total repositories:</b>
            {{ analysis.total_repositories }}
        </p>

        <p>
            <b>Top language:</b>
            {{ analysis.top_language }}
        </p>

        <p>
            <b>Average stars:</b>
            {{ analysis.average_stars }}
        </p>

        <p>
            <b>Top repository:</b>
            {{ analysis.top_repository.name }}
        </p>

    </div>

    <div class="card">

        <h2>📈 Language Distribution</h2>

        <img src="data:image/png;base64,{{ chart }}">

    </div>

    <div class="card">

        <h2>📂 Repositories</h2>

        {{ table | safe }}

    </div>

</body>

</html>
"""


@app.route("/")
def home():

    query = request.args.get(
        "query",
        "web framework"
    )

    repos = fetch_repos(query)

    df = pd.DataFrame(repos)

    analysis = analyze_repositories(df)

    insights = generate_ai_insights(df)

    df["name"] = df.apply(
        lambda row:
        f'<a href="{row["url"]}" target="_blank" style="color:#4ea1ff;">{row["name"]}</a>',
        axis=1
    )

    table = df.to_html(
        index=False,
        escape=False
    )

    chart = generate_chart(df)

    return render_template_string(
        HTML_TEMPLATE,
        analysis=analysis,
        table=table,
        chart=chart,
        query=query,
        insights=insights
    )


if __name__ == "__main__":
    app.run(debug=True)