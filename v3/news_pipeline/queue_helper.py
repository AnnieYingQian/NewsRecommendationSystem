import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://yswgulya:EiuHknHaeHoaL_9Sk7pLYRmLnZ0sMKPH@wombat.rmq.cloudamqp.com/yswgulya"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://eukdbbeq:hm7ZHVwAGUyYVLFKTtTKUGXRQLpExcqJ@wombat.rmq.cloudamqp.com/eukdbbeq"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
