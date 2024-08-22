# Automotive-Web-Scraping
Scrapy project for scraping automotive news.

## Dependencies
Please ensure that virtual environment has been set in case if it is needed before installing each dependency.
All dependencies are available inside requirements.txt. These dependencies must be downloaded before scrapy project 
is run. In addition to above requirements, 'scrapy v2.11.2' must also be installed.

## Procedure

In order to scrap from the website please add configurations in configurations directory in following formats. 

1. news.json

```
    {
        "[domain name]": {
            "allow": URL paths that are allowed to scrape in form of string[],
            "startPath": Starting URL paths from where the scrapy must start crawling in form of string[],
            "deny": URL paths which scrapy is not allowed to crawl in form of string[],
            "format": {
                    "common_parent": CSS selector in string for repetitive common parent to 'site_link', 'heading', etc.
                    "site_link": CSS Selector in string for scraping site link of news,
                    "heading": CSS Selector in string for scraping heading of the news,
                    "body": CSS Selector in string for scraping body of the news,
                    "image_link": CSS Selector in string for scraping image of the news,
                    "publish_date": CSS Selector in string for scraping publish date of the news,
                    "date_format": date format of the publish date to help convert before storing in DB | uses strptime
                }
            },...
    }
```

2. db.json

```
    {
    "credentials": {
        "database": database such as postgresql, mysql, sqlite, in string,
        "username": username in string,
        "password": password in string,
        "db_name": database name in string,
        "host": hostname in string,
        "port": port number in string
        }
    }

``` 

3. mail.json

```
    {
    "sender": sender email in string,
    "password": sender email password in string | app password from gmail,
    "recipients": recipients in string[] format
    }
```

## Execution


News can be crawled from individual websites in case needed using following command

```
    scrapy crawl news -a site=domain name available in news.json in string format
```

All websites in news.json can be crawled at once by running script using this command
```
    python run.py
```