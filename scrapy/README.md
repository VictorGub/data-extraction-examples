# Installation
- Firstly install [docker-compose](https://docs.docker.com/compose/install/)

# How to run?
By default, the output data will be stored as `result.json` file in the project folder
```shell
docker-compose up
```
to change output file to JSON format, please take a look at `docker-compose.yml` file

# Notes
- The main codebase is located at `positions/spiders/ae.py`
- The crawler is based on [Scrapy](https://docs.scrapy.org/en/latest/)
