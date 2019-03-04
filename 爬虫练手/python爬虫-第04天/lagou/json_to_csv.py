#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
import json

def json_to_csv():
    json_file = open("lagou.json", "r")
    csv_file = open("lagou.csv", "w")

    item_list = json.load(json_file)

    #[]
    key_data = item_list[0].keys()
    #[[], [], [], []]
    value_data = [item.values() for item in item_list]

    # csv文件写入对象
    csv_writer = csv.writer(csv_file)
    # 先写入表头字段数据
    csv_writer.writerow(key_data)
    # 再写入表的值数据
    csv_writer.writerows(value_data)

    csv_file.close()
    json_file.close()

if __name__ == "__main__":
    json_to_csv()
