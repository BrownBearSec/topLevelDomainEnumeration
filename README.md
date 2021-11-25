# Top Level Domain Enumerating

### The process of how I enumerate some domains for a tld

1) google `"site:*.tld"`, eg `"site:.*gov"`
2) append `&num=1000` to the url. This will show more results on the page 
3) ctrl + a, ctrl + c, ctrl + v into vscode. Yes this is primative, but its genuinely one of the most efficient ways to scrape google as google doesnt like being scraped.
4) in vscode, ctrl + f, then enter `https?:\/\/(www\.)?[-a-zA-Z0-9@:%.\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%\+.~#?&//=]*)` making sure it is in regex mode
5) ctrl + shift + L, ctrl c, ctrl a, del, ctrl v. This copys all the urls, and isolates them
6) ctrl f, `^https?://` , ctrl + shift + L, del. This removes all the http or https prefixes
7) cat file | sort | uniq > out. This removes duplicates
8) `python domainparser.py out tld` This will remove subdomains and clean the domains
9) cat rootdomains.txt | sort | uniq > final.txt

You've got a list of nice root domains fairley quickly, you're welcome.