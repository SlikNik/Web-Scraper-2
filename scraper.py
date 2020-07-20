import requests
import argparse
from bs4 import BeautifulSoup, SoupStrainer
import sys
import re

__author__ = 'Nikal Morgan'


def scraper(link):
    """Scrapes website for all links, email addresses, phone numbers,
    and images"""
    res = requests.get(link)
    # print(res.text)
    print('-----------------URLs-----------------')
    
    print('-----------------Email Addresses-----------------')
    
    print('-----------------Phone Numbers-----------------')
   
    print('-----------------Images-----------------')
  


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='link of page to scrape')
    return parser


def main(args):
    parser = create_parser()
    args = parser.parse_args(args)
    link = args.link
    return scraper(link)


if __name__ == '__main__':
    main(sys.argv[1:])
