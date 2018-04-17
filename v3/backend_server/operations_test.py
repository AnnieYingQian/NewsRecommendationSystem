import operations

def test_get_one_news_basic():
    news = operations.get_one_news()
    print(news)
    assert news is not None
    print('test_get_one_news_basic passed!')

if __name__ == '__main__':
    test_get_one_news_basic()
