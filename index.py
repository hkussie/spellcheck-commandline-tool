import click 
import requests 
click.disable_unicode_literals_warning = True

@click.command()
def main(): 
	click.echo("This is a CLI built with Click ✨")

if __name__ == "__main__":
	main()
