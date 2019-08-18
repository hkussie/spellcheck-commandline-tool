import click 
import requests 
click.disable_unicode_literals_warning = True

@click.command()
@click.argument('sentence')
def main(sentence): 
	url = "https://montanaflynn-spellcheck.p.rapidapi.com/check/"
	querystring = {"text":"{}".format(sentence)}
	headers = {
    'x-rapidapi-host': "montanaflynn-spellcheck.p.rapidapi.com",
    'x-rapidapi-key': "3b2d1eb02fmsh98b6d725c983d35p1b42afjsn01388dd70d1d"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	click.echo(response.text)

if __name__ == "__main__":
	main()