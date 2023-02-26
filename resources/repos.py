from typing import Protocol, OrderedDict
from bs4 import BeautifulSoup
import requests
from . import models


class ItemsReposInteface(Protocol):
    
    def create_item(self, data: OrderedDict) -> None: ...

class ItemsReposV1():

    def create_item(self, data: OrderedDict) -> None:
        site = models.Resource.objects.get(resource_id=data['res_id'])
        url = site.resource_url
        top_tag = site.top_tag.split(',')

        resp = requests.get(url) #Хринит response по ссылке из переменной url
        bs = BeautifulSoup(resp.text, features='html.parser') #Хранитиь в себе HTML код
        news = bs.find_all(*top_tag)

        for link in news:
            resp = requests.get(link['href']) #Хринит response по ссылке из переменной link
            bs = BeautifulSoup(resp.text, features='html.parser') #Хранитиь в себе HTML код

            title = bs.find(*(site.title_cut.split(',')))
            content = bs.find(*(site.bottom_tag.split(',')))
            nd_date = bs.find(*(site.date_cut.split(',')))
            not_date = bs.find(*(site.date_cut.split(',')))

            models.Items.objects.create(
                res_id=site,
                link=link['href'], 
                title=title.text, 
                content=content.text, 
                nd_date=nd_date.text,
                not_date=not_date.text
            ).save()