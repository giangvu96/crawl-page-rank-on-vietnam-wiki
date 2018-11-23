from scrapy import spider,Request
from wikiPageRank.items import WikipagerankItem

class WikiSpider(spider.Spider):
    name = "wiki"

    allowed_domains = ["vi.wikipedia.org"]

    start_urls = [
        'https://vi.wikipedia.org/wiki/Chi%E1%BA%BFn_tranh_bi%C3%AAn_gi%E1%BB%9Bi_Vi%E1%BB%87t%E2%80%93Trung_1979'
    ]

    def parse(self, response):
        # print("------------------------------------------------------------")
        # with open("result2.txt","a") as file :
        #     file.writelines(response.url + "\n")
        # print(response.url)
        # print("------------------------------------------------------------")

        substring = "https://vi.wikipedia.org/w/"
        list_dst = []
        for url in response.xpath('//div[@id="mw-content-text"]/div[@class="mw-parser-output"]/p/a/@href').extract():
            if "#" in url:
                continue
            url = response.urljoin(url)
            if substring in url:
                continue
            list_dst.append(url)

        item = WikipagerankItem()
        item["src"] = response.url
        item["dst"] = set(list_dst)
        yield item

        for url in list_dst:
            yield Request(url, callback=self.parse)
