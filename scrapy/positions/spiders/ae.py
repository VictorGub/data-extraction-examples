import scrapy

START_URL = "https://www.join.agileengine.com/open-positions/"
FILTER_PARAMS = "job__seniority_spec=lead&non__engineering__technical__flow_spec=none"
INPUT_DATA_CSV_FILE = "data.csv"


class AeSpider(scrapy.Spider):
    name = "ae"

    def start_requests(self):
        yield scrapy.Request(url=f"{START_URL}?{FILTER_PARAMS}", callback=self.parse)

    def parse(self, response):
        self.log(f"URL {response.request.url}")

        request_url = response.request.url

        for position in response.css(".awsm-job-listings > a"):
            url = position.attrib["href"]
            title = position.css(".awsm-job-post-title::text").extract_first()
            tags = position.css(".awsm-job-specification-term::text").extract()
            yield self.format_output(title, tags, url)

    def format_output(self, title, tags, url):
        return {
            "title": title,
            "tags": tags,
            "url": url
        }
