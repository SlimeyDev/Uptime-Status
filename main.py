from flask import Flask, render_template
import requests

app = Flask(__name__)

website_urls = [
    "https://slimeydev.github.io/",
    "https://slimeyapi.onrender.com/",
    "https://spellgpt.onrender.com/",
    "https://slimey-bot.slimeydev.repl.co"
]

website_names = {
    "https://slimeydev.github.io/": "Website",
    "https://slimeyapi.onrender.com/": "SlimeyAPI",
    "https://spellgpt.onrender.com/": "SpellGPT",
    "https://slimey-bot.slimeydev.repl.co": "SlimeyBOT"
}

@app.route('/')
def index():
    website_status = {}
    for url in website_urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                website_status[url] = "up"
            else:
                website_status[url] = f"down with status code {response.status_code}"
        except:
            website_status[url] = "an error occurred"
    return render_template('index.html', website_status=website_status, website_names=website_names)

if __name__ == '__main__':
    app.run(debug=True)