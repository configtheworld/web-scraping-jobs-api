from datetime import datetime
import scrapy

class MySpider(scrapy.Spider):
    name="stackoverflow"

    allowed_domains = ["https://stackoverflow.com/jobs"] 

    async def start_requests(self): 
        yield await scrapy.Request("https://stackoverflow.com/jobs", self.parse) 


    async def parse(self, response): 

        stackoverflow_jobs = [] 

        for job in response.css("js-result"): 

            try: 
                title=await job.css(".stretched-link::text").extract()
                #company=
                #location=
                #tags=[]
                #attributes=[]
                stackoverflow_jobs.append(title)
            except Exception as e: 

                with open("exception.log", "a+") as exception_file: 
                    exception_file.write( 
                     "time: " + str(datetime.datetime.now()) + "\n" + str(e) 
                    )
        yield stackoverflow_jobs


def scrape_jobs():
    so= MySpider()
    res = so.start_requests()    
    print(res)
