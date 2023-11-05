from flask import Flask, render_template, request
from markupsafe import escape
from googleAPI import get_webtags
from reddit import parse
from buddy import summarize_user_advice, create_html_links

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/test")
def test_route():
    return "<p> This was a tag using htmx</p>"


@app.route("/query", methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query = escape(request.form['search'])
        print(query)
        webtags = get_webtags(query, 1)
        # print(webtags)
        urls = []
        for tag in webtags:
            urls.append(tag["link"])

        print(urls[:2])
        ret_string, ret_comments = parse(urls, 1)

        print(ret_string)
        summed_text = summarize_user_advice(ret_string)
        print(summed_text)
        return create_html_links(summed_text)
