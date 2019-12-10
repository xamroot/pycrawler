# pycrawler
## usage
pycrawler.py [-h] [-t THREADS] url [wordlist_filename]

positional arguments:
<br/>url &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;Target url to crawl 
<br/>wordlist_filename &nbsp; Wordlist file to use, default is wordlist.txt

optional arguments:
<br/>-h, --help &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; show this help message and exit
<br/>-t THREADS, --threads &nbsp; &nbsp;&nbsp; THREADS Number of threads to spin up, default is 10

## Example uses
pycrawler.py -t 25 https://www.google.com custom_wordlist.txt
<br />pycrawler.py -t 5 https://www.yahoo.com 
<br />pycrawler.py https://www.bing.com

## Roadmap
- Search pages for certain html tag
