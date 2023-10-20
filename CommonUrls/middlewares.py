
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from aiohttp_socks import ProxyConnector, ProxyType


class RandomUserAgentMiddleware:

    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent_list=crawler.settings.get("USER_AGENT_LIST"))

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.user_agent_list)


class TorProxyMiddleware(RetryMiddleware):

    def __init__(self, settings, *args, **kwargs):
        self.tor_proxy = settings.get("TOR_PROXY")
        super().__init__(settings, *args, **kwargs)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    async def _retry(self, request, reason, spider):
        proxy_connector = ProxyConnector.from_url(self.tor_proxy)
        request.meta["proxy"] = self.tor_proxy
        request.meta["proxy_connector"] = proxy_connector
        return await super()._retry(request, reason, spider)

class SeleniumMiddleware:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        self.driver = webdriver.Chrome(options=options)

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        if getattr(spider, 'use_selenium', False):
            self.driver.get(request.url)
            return HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=request)

    def spider_closed(self):
        self.driver.quit()