# Automotive-Web-Scraping
Scrapy project for scraping automotive news.

## Dependencies
Please ensure that virtual environment has been set in case if it is needed before installing each dependency.

1. Scrapy

Needed for scraping and starting project.
```
    pip install scrapy
```

2. Dataset

Needed for queries and storing news in DB.
```
    pip install dataset
```

## Procedure

In order to scrap from the website please add configurations in 'news.json' file in following format.

```
    {
        "[domain name]": {
            "allow": [[URLs that are allowed to scrape in form of list]],
            "startPath": [[Starting URLs in form of list]],
            "format": {
                    "individual_objects": "[CSS selector for repetitive news / items / objects acting as a parent to 'site_link', 'heading', etc.]"
                    "site_link": "[CSS Selectors]",
                    "heading": "[CSS Selectors]",
                    "body": "[CSS Selectors]",
                    "image_link": "[CSS Selectors]",
                    "publish_date": "[CSS Selectors]"
                }
            }
    }
```

After that please configure the db.json file.
```
    {
        "postgresql": {
            "username": "[user name]",
            "password": "[user password]",
            "database": "[database name]",
            "table": "[table name]"
        }
    }
```

News can be crawled from websites using following command
```
    scrapy crawl news -a site=[domain name available in news.json]
```