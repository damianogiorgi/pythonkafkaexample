# Consumer.py
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import os,time, sys #, ssl

brokers = os.environ.get('KAFKA_BROKERS').split(',')
topic_prefix = os.environ.get('KAFKA_TOPIC_PREFIX')
sleeptime = float(os.environ.get('CONSUMER_SLEEP_TIME'))

print ("Wait 5s for kafka to settle...")
time.sleep(5)
print ("Done")
clientid= "consumer" + str(time.time())
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic_prefix + 'default',
                         group_id='my-group',
                         bootstrap_servers=brokers, fetch_max_wait_ms=50, auto_commit_interval_ms=100, client_id=clientid) #,
#                         security_protocol='SSL',
#                         ssl_context=ssl_context)
print ('Start consuming')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("Message received:", message.value)
    sys.stdout.flush()
    print ("sleeping for: " +str(sleeptime))
    time.sleep(sleeptime)
