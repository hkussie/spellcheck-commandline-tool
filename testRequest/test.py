import requests

url = "https://montanaflynn-spellcheck.p.rapidapi.com/check/"

querystring = {"text":"let'ss test this sentence"}

headers = {
    'x-rapidapi-host': "montanaflynn-spellcheck.p.rapidapi.com",
    'x-rapidapi-key': "3b2d1eb02fmsh98b6d725c983d35p1b42afjsn01388dd70d1d"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)