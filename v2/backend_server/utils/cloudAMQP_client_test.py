from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://yltcwjbm:iO0njiOeQ0MJI8UgNhhz6wFwUVxCsFJK@wombat.rmq.cloudamqp.com/yltcwjbm"
QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

    sentMsg = {'test': 'test'}
    client.sendMessage(sentMsg)

    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg

    print('test_basic passed.')

if __name__ == "__main__":
    test_basic()
