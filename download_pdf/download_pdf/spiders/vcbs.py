#import scrapy
import urllib
import scrapy
import os
from datetime import datetime
from download_pdf.items import DownloadPdfItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests
from pathlib import Path

class VcbsSpider(scrapy.Spider):
    name = 'vcbs'
    allowed_domains = ['www.vcbs.com.vn']
    start_urls = ['https://www.vcbs.com.vn/vn/Services/AnalysisReports/4']
    rules = [Rule(LinkExtractor(allow=""), callback='parse_httpresponse', follow=True)]

    def parse(self, response):
        base_url  = 'https://www.vcbs.com.vn'
        for a in response.xpath('//a[contains(@href, "/vn/Communication/GetReport")]/@href'):
            link = a.extract()
            print("Đây là link: ",link)
            parsed = urlparse.urlparse(link)
            index = parse_qs(parsed.query)['reportId']
            print(index)
            url = base_url + link
            print("url", url)
            pdfname = 'PDF/' + index[0] + '.pdf'
            filename = Path(pdfname)
            print(filename)
            response = requests.get(url)
            filename.write_bytes(response.content)
