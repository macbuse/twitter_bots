import re 
import requests

url = 'https://www.brainyquote.com/topics/problems-quotes'
url = 'https://www.brainyquote.com/topics/science-quotes'

pp = re.compile('<a href="/quotes/(.*?)_\d+.*?>(.*?)</a>',re.DOTALL)


r = requests.get(url)

def clean(x):
    author, quote = x
    bits = [x[0].upper() + x[1:] for x in author.split('_')]
    return ' '.join(bits), html.unescape(quote)
    

list_of_quotes = [ clean(xx) for xx in pp.findall(r.text)]
