import urllib
import pathlib



def do_POST():
    pr_url = urllib.parse.url()

    match pr_url.path:
        case '/':
            print('t')
        case '/blog':
            self.render    

