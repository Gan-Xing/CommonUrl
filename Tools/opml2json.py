import json
import re
import xmltodict

def opml_to_json(opml_file_path):
    with open(opml_file_path, 'r', encoding='utf-8') as opml_file:
        opml_content = opml_file.read()
    
    opml_dict = xmltodict.parse(opml_content)
    json_string = json.dumps(opml_dict, indent=4, ensure_ascii=False)

    return json_string

# 使用方法示例
opml_file_path = 'mindmap.opml'
json_string = opml_to_json(opml_file_path)

# JSON去除固定属性
def process_outline(outline):
    if isinstance(outline, list):
        return [process_outline(o) for o in outline]
    elif isinstance(outline, dict):
        result = {'@text': outline['@text']}
        if 'outline' in outline:
            result['outline'] = process_outline(outline['outline'])
        return result
data = json.loads(json_string)
processed_outline = process_outline(data['body']['outline'])  

processed_outline_str = json.dumps(processed_outline, indent=4, ensure_ascii=False)


# JSON压缩字符串
def compress_string(string):
    string = re.sub(r'(\r\n|\n|\r|\t| )+', ' ', string)
    string = re.sub(r'(?<=\{|\(|\[)\s+', '', string)
    string = re.sub(r'\s+(?=\}|\)|\])', '', string)
    return string.strip()

string = compress_string(processed_outline_str)

with open('output.text', 'w', encoding='utf-8') as json_file:
    json_file.write(string)

# 将JSON字符串保存到文件中
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(processed_outline_str)

print('OPML文件已成功转换为JSON格式。')
