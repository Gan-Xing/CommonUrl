import json

# 读取JSON文件
with open('extracted_information.json', 'r') as f:
    data = json.load(f)

# 对p进行去重操作
p_unique = list(set(data['p']))

# 对links进行去重操作
links_unique = []
url_set = set()  # 用于记录已经出现过的URL

for link in data['links']:
    if link['url'] not in url_set:
        links_unique.append(link)
        url_set.add(link['url'])

# 将去重后的结果保存到另一个JSON文件中
result = {'p': p_unique, 'links': links_unique}

with open('result.json', 'w') as f:
    json.dump(result, f)

# 添加每1000次循环打印一次的逻辑，还有打印总循环次数
total_length = len(data['p']) + len(data['links'])
step = 1000
count = 0

for i in range(total_length):
    # 在这里进行处理

    count += 1
    if count % step == 0:
        print(f'Processed {count} of {total_length} items')
        
print(f'Total iterations: {count}')
