import scrapy
import os
from bs4 import BeautifulSoup
import logging
import json
import execjs
from xml.etree.ElementTree import Element, SubElement, tostring

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')


class ExampleSpider(scrapy.Spider):
    name = "openai_text_embedding"
    allowed_domains = ['python.langchain.com']
    start_urls = ['https://python.langchain.com/en/latest']
    use_selenium = True

    def parse(self, response):
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        sidebar_primary_items = soup.find_all(class_="sidebar-primary-items__start")
        if sidebar_primary_items:
            extracted_html = str(sidebar_primary_items[0])
            json_data = self.html_to_json(extracted_html)
            self.save_json(json_data, "abcd.json")
        else:
            logging.error("No elements found with class 'sidebar-primary-items__start'")


    def html_to_json(self, html):
        with open("html2json_converter.js", "r") as js_file:
            js_code = js_file.read()

        context = execjs.compile(js_code)
        json_data = context.call("convert", html)
        return json_data

    def save_json(self, data, filename):
            with open(filename, "w") as json_file:
                json.dump(data, json_file)


    #     content = soup.select_one('body > div.bd-container > div > div > div.sidebar-primary-items__start.sidebar-primary__section')




    # github 提取器import scrapy
    # import json
    # import os
    # from urllib.parse import urljoin
    # import logging
    # from bs4 import BeautifulSoup
    # import html2text

    # # 配置日志记录器
    # logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')


    # class ExampleSpider(scrapy.Spider):
    #     name = "example"
    #     allowed_domains = ['github.com']
    #     use_selenium = True
    #     start_urls = [f'https://github.com/search?p={page}&q=chatgpt&type=Repositories' for page in range(1, 11)]
    #     all_data = {"desc": [], "links": []}  # 所有数据

    #     def start_requests(self):
    #         for url in self.start_urls:
    #             yield scrapy.Request(url=url, callback=self.parse)

    #     def parse(self, response):
    #         # 使用 BeautifulSoup 解析 HTML
    #         soup = BeautifulSoup(response.text, 'html.parser')

    #         # 提取仓库链接和描述信息
    #         repos = soup.select('div.codesearch-results ul li div.mt-n1.flex-auto div.d-flex div a')
    #         descriptions = soup.select('div.codesearch-results ul li div.mt-n1.flex-auto p')

    #         # 将提取到的信息保存到本地JSON文件
    #         for repo, desc in zip(repos, descriptions):
    #             repo_link = repo['href']
    #             repo_desc = desc.text.strip()
    #             self.all_data["desc"].append(repo_desc)
    #             self.all_data["links"].append(urljoin(response.url, repo_link))

    #         with open('output/github.json', 'w', encoding='utf-8') as f:
    #             json.dump(self.all_data, f, ensure_ascii=False, indent=2)

    #         # 对链接进行访问，并保存为 Markdown 格式的文件
    #         for link in self.all_data["links"]:
    #             yield scrapy.Request(link, callback=self.parse_repo)

    #     def parse_repo(self, response):
    #         # 使用 BeautifulSoup 解析 HTML
    #         soup = BeautifulSoup(response.text, 'html.parser')

    #         # 提取 README.md 的内容
    #         readme_content = soup.select_one('#readme > div.Box-body.px-5.pb-5, #readme > div.Box-body.px-5.pb-5 > article, #repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > readme-toc')

    #         if readme_content is not None:
    #             # 将内容从 HTML 转换为 Markdown
    #             h = html2text.HTML2Text()
    #             h.body_width = 0
    #             markdown_content = h.handle(str(readme_content))

    #             # 获取仓库名称
    #             repo_name = response.url.split("/")[-1]

    #             # 将内容保存为 Markdown 文件
    #             folder_name = 'github'
    #             if not os.path.exists(folder_name):
    #                 os.makedirs(folder_name)
    #             file_name = f'{folder_name}/{repo_name}.md'
    #             if not os.path.exists(file_name):
    #                 with open(file_name, 'w', encoding='utf-8') as f:
    #                     f.write(markdown_content)
    #         else:
    #             logging.warning(f"README content not found for {response.url}")

















    # import scrapy
    # import re
    # import os
    # import json
    # import html2text
    # from bs4 import BeautifulSoup
    # from urllib.parse import urljoin

    # class ExampleSpider(scrapy.Spider):
    #     name = "example"
    #     allowed_domains = ['github.com']
    #     start_urls = [f'https://github.com/search?p={page}&q=chatgpt&type=Repositories' for page in range(1, 11)]
    #     use_selenium = True  # 是否使用 Selenium
    #     all_data = {"desc": [], "links": []}  # 所有数据
    #     p_set = set()  # 提取过的文本集合
    #     links_set = set()  # 提取过的链接集合
    #     start_urls_prefix = 'https://platform.openai.com/docs/'  # 起始 URL 前缀
    #     visited_urls = set()  # 已访问过的 URL 集合
    #     crawl_counter = 0  # 爬取计数器

    #     def parse(self, response):

    #         # 提取仓库链接和描述信息
    #         repos = response.xpath('//li[contains(@class, "repo-list-item")]/div/h3/a')
    #         descriptions = response.xpath('//li[contains(@class, "repo-list-item")]/div/p')

    #         # 将提取到的信息保存到本地JSON文件
    #         for repo, desc in zip(repos, descriptions):
    #             repo_link = repo.attrib['href']
    #             repo_desc = desc.xpath('string(.)').get().strip()
    #             self.all_data["desc"].append(repo_desc)
    #             self.all_data["links"].append(urljoin(response.url, repo_link))


    #         with open('output/github.json', 'w', encoding='utf-8') as f:
    #             json.dump(self.all_data, f, ensure_ascii=False, indent=2)

        #     yield {'github': json.dumps(self.all_data, ensure_ascii=False, indent=2)}

        #     # 对链接进行访问，并保存为 Markdown 格式的文件
        #     for link in self.all_data["links"]:
        #         yield scrapy.Request(link, callback=self.parse_repo)

        # def parse_repo(self, response):
        #     # 提取文档标题和 Markdown 格式内容
        #     title = response.xpath('//title/text()').get()
        #     body_html = response.xpath('//article[contains(@class, "markdown-body")]/node()')
        #     body_markdown = html2text.html2text(body_html.getall(), bodywidth=0)

        #     # 将内容保存为 Markdown 文件
        #     folder_name = 'githubgpt'
        #     if not os.path.exists(folder_name):
        #         os.makedirs(folder_name)
        #     file_name = f'{folder_name}/{title}.md'
        #     if not os.path.exists(file_name):
        #         with open(file_name, 'w', encoding='utf-8') as f:
        #             f.write(body_markdown)