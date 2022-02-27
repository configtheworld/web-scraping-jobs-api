import requests as _requests
from bs4 import BeautifulSoup 
from typing import List

def _genrate_url(query:str,location:str,remote:bool,visa:bool)-> str:
    url = "https://stackoverflow.com/jobs?q={query}&l={location}&r={remote}&v={visa}"
    return url

def _get_page(url: str)-> BeautifulSoup:
    page=_requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    return soup

def list_of_jobs(query:str,location:str,remote:bool,visa:bool)->List[str]:
    url = _genrate_url(query,location,remote,visa)
    page = _get_page(url)
    raw_events= page.find_all(class_="-job js-result")
    print(raw_events)

list_of_jobs("front-end","germany",True,True)
