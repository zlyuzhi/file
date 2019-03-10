import time
# print(int(time.time()*1000))
import requests
import json
import jsonpath
'''

https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/datatransfer/index.json?timestamp=1552123784994  /流量计费

https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/us-east-1/ondemand(模式)/linux/index.json?timestamp=1552123786545

https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/us-east-1/ondemand/rhel/index.json?timestamp=1552123786552

https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/ap-northeast-2/ondemand/windows/index.json?timestamp=1552131728059
https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/ap-southeast-2/elastic-ips/index.json?timestamp=1552126738829
https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/us-east-1/ondemand/linux-web/index.json?timestamp=1552123786589

https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/{0}/ondemand/{1}/index.json?timestamp=time.time()*1000




a=["ap-south-1","eu-west-3", "eu-north-1","eu-west-2","eu-west-1","ap-northeast-3","ap-northeast-2","ap-northeast-1","us-gov-east-1","sa-east-1","ca-central-1","us-gov-west-1","ap-southeast-1","ap-southeast-2","eu-central-1","us-east-1","us-east-2","us-west-1","us-west-2"]

b=["suse","rhel","windows","linux-web","linux","windows-std","windows-enterprise","linux-std","linux-enterprise","windows-web"]
url="https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/{0}/ondemand/{1}/index.json?timestamp="

# USER_AGENT = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
headers = {"user_agent":'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
# url3 = None

for eare in a:
    for ondemand in b:
        url2 = url.format(eare, ondemand)
        url3 = url2 + str(int(time.time()*1000))
        r = requests.get(url3, headers=headers).text
        # 把json格式字符串转换成python对象
        jsonobj = json.loads(r)
        list1 = jsonpath.jsonpath(jsonobj, '$..prices/';.)
         
        print(url3)
        print(list1)


url4 = 'https://view-prod.us-east-1.prod.plc1-prod.pricing.aws.a2z.com/pricing/1.0/ec2/region/us-east-1/ondemand/linux-web/index.json?timestamp=1552123786589'
'''

