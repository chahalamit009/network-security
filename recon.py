import requests
from bs4 import BeautifulSoup as bs
import optparse
import socket
def host_ip(link_list):
    for url in link_list:
        print url+'--->  '+str(socket.gethostbyname(url))
def extract_href(target_url):
    req = requests.get(target_url)
    html_soup = bs(req.text, 'html.parser')
    link = html_soup.find_all('a',href=True)
    link_list = []
    for a in link:
        if '//' in a['href']:
            url = a['href'].split("//")[-1].split("/")[0]
            if url :
                url = url.encode("utf-8")
                link_list.append(url)
    link_list= list(set(link_list))
    host_ip(link_list)
def main():
    parser = optparse.OptionParser("usage%prog"+"-U <url>")
    parser.add_option('-U', dest='url', type='string', help='specify target url')
    (options, args) = parser.parse_args()
    target_url = options.url
    if target_url == None:
        print '[-] You must specify a target_url'
        exit(0)
    extract_href(target_url)
if __name__ == '__main__':
    main()
