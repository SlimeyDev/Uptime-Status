import requests

website_url = [
    "https://slimeydev.github.io/",
    "https://slimeyapi.onrender.com/random",
    "https://slimeyapi.onrender.com/weather?place=India",
    "https://spellgpt.onrender.com/"
]

statuses = {
    200: "Service Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}

for url in website_url:
    try:
        web_response = requests.get(url)
        print(url, statuses[web_response.status_code])

    except:
        print(url, statuses[web_response.status_code])