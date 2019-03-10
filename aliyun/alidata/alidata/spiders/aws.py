# -*- coding: utf-8 -*-
import scrapy
import json

#到时候要灵活处理
import time

a=["ap-south-1","eu-west-3", "eu-north-1","eu-west-2","eu-west-1","ap-northeast-3","ap-northeast-2","ap-northeast-1","us-gov-east-1","sa-east-1","ca-central-1","us-gov-west-1","ap-southeast-1","ap-southeast-2","eu-central-1","us-east-1","us-east-2","us-west-1","us-west-2"]

b=["suse","rhel","windows","linux-web","linux","windows-std","windows-enterprise","linux-std","linux-enterprise","windows-web"]
url="https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/{0}/ondemand/{1}/index.json?timestamp="

class AwsSpider(scrapy.Spider):
    name = 'aws'
    allowed_domains = ['https://amazonaws-china.com']
    global url3
ddc
    for eare in a:
        for ondemand in b:
            url2 = url.format(eare, ondemand)
            url3 = url2 + str(int(time.time() * 1000))
    start_urls = url3
    def parse(self, response):
        response.jsonpath
