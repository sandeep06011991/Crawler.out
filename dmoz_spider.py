import scrapy
from scrapy.selector import *
from scrapy.contrib.spiders import CrawlSpider, Rule
import json
class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = []
	
    def __init__(self, category=None, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
	for i in range(1,84):
		string="http://www.snapdeal.com/acors/json/product/get/search/322/"+str(i*50)+"/50"
		self.start_urls.append(string)
	self.out=open("data.txt",'w')
	
    def parse(self, response):
	true=True
	false=False	
	dump=eval(response.body)
	for prod in dump["productDtos"]:
		self.out.write(str(prod["id"])+","+prod["name"].replace(',','.')+","+str(prod["price"])+","+str(prod["discount"])+","+str(prod["displayPrice"])+"\n")
