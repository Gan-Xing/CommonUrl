import scrapy
import re
import os
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ExampleSpider(scrapy.Spider):
    name = "openaidoc"
    allowed_domains = ['platform.openai.com']  # 网站域名
    start_urls = ['https://platform.openai.com/docs/']  # 起始 URL
    use_selenium = True  # 是否使用 Selenium
    all_data = {"text": [],"preformatted": [], "links": []}  # 所有数据
    p_set = set()  # 提取过的文本集合
    links_set = set()  # 提取过的链接集合
    start_urls_prefix = 'https://platform.openai.com/docs/'  # 起始 URL 前缀
    visited_urls = set()  # 已访问过的 URL 集合
    crawl_counter = 0  # 爬取计数器

    def parse(self, response):
        # 记录访问过的 URL
        self.visited_urls.add(response.url)
        # 解析当前页面并提取相关数据
        extracted_data = self.parse_and_extract(response)
        # 将提取到的数据合并到 all_data
        for text in extracted_data["text"]:
            if text not in self.p_set:
                self.all_data["text"].append(text)
                self.p_set.add(text)
        # 添加和过滤链接
        filtered_links = []
        for link in extracted_data["links"]:
            if link["url"].startswith(self.start_urls_prefix) and not self.contains_anchor(link["url"]) and link["url"] not in self.links_set:
                self.all_data["links"].append(link)
                self.links_set.add(link["url"])
                filtered_links.append(link)
        # 更新提取到的链接
        extracted_data["links"] = filtered_links

        self.crawl_counter += len(filtered_links)

        log_message = f"已完成爬取 {self.crawl_counter} 条 URL，共 {len(self.links_set)} 条符合条件的 URL。"

        self.write_log_to_file('output/crawl_log.txt', log_message)

        # 寻找下一层子链接
        for link in extracted_data["links"]:
            url = link["url"]
            if url.startswith(self.start_urls_prefix) and url not in self.visited_urls:
                yield scrapy.Request(url, callback=self.parse)

        # 如果输出目录不存在，则创建它
        if not os.path.exists("output"):
            os.mkdir("output")

        # 将提取到的信息保存到本地JSON文件
        with open('output/openAI.json', 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=2)

        yield {'openAI': json.dumps(self.all_data, ensure_ascii=False, indent=2)}

    def write_log_to_file(self, filename, message):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")

    def parse_and_extract(self, response):
        # 获取源代码
        html_content = response.text

        # 解析HTML并删除样式
        soup = BeautifulSoup(html_content, "html.parser")

        # 提取相关信息
        extracted_data = self.extract_relevant_data(soup)

        return extracted_data

    def extract_relevant_data(self, soup):
        extracted_data = {}

        docs_body_elements = soup.find_all(class_="docs-body")
        extracted_data["text"] = [elem.text.strip() for elem in docs_body_elements]
        extracted_data["links"] = [{"text": link.text.strip(), "url": urljoin(self.start_urls_prefix, link["href"])} for link in soup.find_all("a")]

        return extracted_data

    def contains_anchor(self, url):
        _, _, anchor = url.partition("#")
        return bool(anchor)
    






# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     allowed_domains = ['platform.openai.com']  # 网站域名
#     start_urls = ['https://platform.openai.com/docs/']  # 起始 URL
#     use_selenium = True  # 是否使用 Selenium
#     all_data = {"text": [],"preformatted": [], "links": []}  # 所有数据
#     p_set = set()  # 提取过的文本集合
#     links_set = set()  # 提取过的链接集合
#     start_urls_prefix = 'https://platform.openai.com/docs/'  # 起始 URL 前缀
#     visited_urls = set()  # 已访问过的 URL 集合
#     crawl_counter = 0  # 爬取计数器

#     def parse(self, response):
#         # 记录访问过的 URL
#         self.visited_urls.add(response.url)
#         # 解析当前页面并提取相关数据
#         extracted_data = self.parse_and_extract(response)
#         # 将提取到的数据合并到 all_data
#         for text in extracted_data["text"]:
#             if text not in self.p_set:
#                 self.all_data["text"].append(text)
#                 self.p_set.add(text)
#         # 添加和过滤链接
#         filtered_links = []
#         for link in extracted_data["links"]:
#             if link["url"].startswith(self.start_urls_prefix) and not self.contains_anchor(link["url"]) and link["url"] not in self.links_set:
#                 self.all_data["links"].append(link)
#                 self.links_set.add(link["url"])
#                 filtered_links.append(link)
#         # 更新提取到的链接
#         extracted_data["links"] = filtered_links

#         self.crawl_counter += len(filtered_links)

#         log_message = f"已完成爬取 {self.crawl_counter} 条 URL，共 {len(self.links_set)} 条符合条件的 URL。"

#         self.write_log_to_file('output/crawl_log.txt', log_message)

#         # 寻找下一层子链接
#         for link in extracted_data["links"]:
#             url = link["url"]
#             if url.startswith(self.start_urls_prefix) and url not in self.visited_urls:
#                 yield scrapy.Request(url, callback=self.parse)

#         # 如果输出目录不存在，则创建它
#         if not os.path.exists("output"):
#             os.mkdir("output")

#         # 将提取到的信息保存到本地JSON文件
#         with open('output/openAI.json', 'w', encoding='utf-8') as f:
#             json.dump(self.all_data, f, ensure_ascii=False, indent=2)

#         yield {'openAI': json.dumps(self.all_data, ensure_ascii=False, indent=2)}

#     def write_log_to_file(self, filename, message):
#         with open(filename, 'a', encoding='utf-8') as f:
#             f.write(f"{message}\n")

#     def parse_and_extract(self, response):
#         # 获取源代码
#         html_content = response.text

#         # 解析HTML并删除样式
#         soup = BeautifulSoup(html_content, "html.parser")

#         # 提取相关信息
#         extracted_data = self.extract_relevant_data(soup)

#         return extracted_data

#     def extract_relevant_data(self, soup):
#         extracted_data = {}

#         docs_body_elements = soup.find_all(class_="docs-body")
#         extracted_data["text"] = [elem.text.strip() for elem in docs_body_elements]
#         extracted_data["links"] = [{"text": link.text.strip(), "url": urljoin(self.start_urls_prefix, link["href"])} for link in soup.find_all("a")]

#         return extracted_data

#     def contains_anchor(self, url):
#         _, _, anchor = url.partition("#")
#         return bool(anchor)



        # # 单独提取某个网页的内容

        # main_data = {}

        # html_content = response.text

        # # 解析HTML并删除样式
        # soup = BeautifulSoup(html_content, "html.parser")

        # def compress_code(code):
        #     code = re.sub(r'(\r\n|\n|\r|\t| )+', ' ', code)
        #     code = re.sub(r'(?<=\{|\(|\[)\s+', '', code)
        #     code = re.sub(r'\s+(?=\}|\)|\])', '', code)
        #     return code.strip()

        # main_data["preformatted"] = [compress_code(pre.text) for pre in soup.find_all("pre")]
        # main_data["text"] = [compress_code(line) for line in soup.text.split('\n') if line.strip()]

        # # 如果输出目录不存在，则创建它
        # if not os.path.exists("output"):
        #     os.mkdir("output")

        # # 将提取到的信息保存到本地JSON文件
        # with open('output/test.json', 'w', encoding='utf-8') as f:
        #     json.dump(main_data, f, ensure_ascii=False, indent=2)

        # yield {'test': json.dumps(main_data, ensure_ascii=False, indent=2)}




# import re
# import os
# import json
# import scrapy
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse, urljoin
# from html.parser import HTMLParser

# class HyperlinkParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.hyperlinks = []

#     def handle_starttag(self, tag, attrs):
#         attrs = dict(attrs)
#         if tag == "a" and "href" in attrs:
#             self.hyperlinks.append(attrs["href"])

# def get_hyperlinks(html):
#     parser = HyperlinkParser()
#     parser.feed(html)
#     return parser.hyperlinks

# class CustomSpider(scrapy.Spider):
#     name = "custom_spider"
#     allowed_domains = ['platform.openai.com']
#     start_urls = ['https://platform.openai.com/']
#     visited_urls = set()

#     def parse(self, response):
#         self.visited_urls.add(response.url)

#         html_content = response.text
#         soup = BeautifulSoup(html_content, "html.parser")

#         hyperlinks = get_hyperlinks(str(soup))
#         domain = urlparse(response.url).netloc

#         for link in hyperlinks:
#             clean_link = None
#             if re.search(r'^http[s]*://.+', link):
#                 url_obj = urlparse(link)
#                 if url_obj.netloc == domain:
#                     clean_link = link
#             else:
#                 if link.startswith("/"):
#                     link = link[1:]
#                 elif link.startswith("#") or link.startswith("mailto:"):
#                     continue
#                 clean_link = "https://" + domain + "/" + link

#             if clean_link is not None:
#                 if clean_link.endswith("/"):
#                     clean_link = clean_link[:-1]

#                 if clean_link not in self.visited_urls:
#                     self.visited_urls.add(clean_link)
#                     yield scrapy.Request(clean_link, callback=self.parse)

#         text = soup.get_text()
#         if ("You need to enable JavaScript to run this app." in text):
#             print("Unable to parse page " + response.url + " due to JavaScript being required")

#         if not os.path.exists("text/"):
#             os.mkdir("text/")

#         if not os.path.exists("text/"+domain+"/"):
#             os.mkdir("text/" + domain + "/")

#         with open('text/'+domain+'/'+response.url[8:].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
#             f.write(text)

