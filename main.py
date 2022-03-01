from fastapi import FastAPI
import job_scrapper

app = FastAPI()


@app.get("/stackoverflow")
def root():
    return job_scrapper.scrape_jobs()