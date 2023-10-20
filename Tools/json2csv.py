import json
import csv

# 读取JSON文件
with open('../output/github.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将数据写入CSV文件
with open('../output/github.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # 写入表头
    writer.writerow(['desc', 'links'])

    # 写入数据行
    for i in range(len(data['desc'])):
        writer.writerow([data['desc'][i], data['links'][i]])
