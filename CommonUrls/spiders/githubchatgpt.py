# github 提取器
import scrapy
import json
import os
from urllib.parse import urljoin
import logging
from bs4 import BeautifulSoup
import html2text

# 配置日志记录器
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')


class ExampleSpider(scrapy.Spider):
    name = "githubchat"
    allowed_domains = ['github.com']
    use_selenium = True
    start_urls = [f'https://github.com/search?p={page}&q=chatgpt&type=Repositories' for page in range(1, 11)]
    all_data = {"desc": [], "links": []}  # 所有数据

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取仓库链接和描述信息
        repos = soup.select('div.codesearch-results ul li div.mt-n1.flex-auto div.d-flex div.text-normal a')
        descriptions = soup.select('div.codesearch-results ul li div.mt-n1.flex-auto p')

        # 将提取到的信息保存到本地JSON文件
        for repo, desc in zip(repos, descriptions):
            repo_link = repo['href']
            repo_desc = desc.text.strip()
            self.all_data["desc"].append(repo_desc)
            self.all_data["links"].append(urljoin(response.url, repo_link))

        # 如果目录不存在，则创建目录
        if not os.path.exists('output'):
            os.makedirs('output')
        with open('output/github.json', 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=2)

        # 对链接进行访问，并保存为 Markdown 格式的文件
        for link in self.all_data["links"]:
            yield scrapy.Request(link, callback=self.parse_repo)

    def parse_repo(self, response):
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取 README.md 的内容
        readme_content = soup.select_one('#readme > div.Box-body.px-5.pb-5, #readme > div.Box-body.px-5.pb-5 > article, #repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > readme-toc')

        if readme_content is not None:
            # 将内容从 HTML 转换为 Markdown
            h = html2text.HTML2Text()
            h.body_width = 0
            markdown_content = h.handle(str(readme_content))

            # 获取仓库名称
            md_name = response.url.split("/")[-2]+response.url.split("/")[-1]

            # 将内容保存为 Markdown 文件
            folder_name = 'github'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            file_name = f'{folder_name}/{md_name}.md'
            if not os.path.exists(file_name):
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
        else:
            logging.warning(f"README content not found for {response.url}")


