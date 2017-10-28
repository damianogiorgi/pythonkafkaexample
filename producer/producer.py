# Producer.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
import os, time #ssl

# Load the rest of the env variables
brokers = os.environ.get('KAFKA_BROKERS').split(',')
topic_prefix = os.environ.get('KAFKA_TOPIC_PREFIX')
sleep_time = float(os.environ.get('PRODUCER_SLEEP_TIME'))

print ("Wait 5s for kafka to settle...")
time.sleep(5)
print ("Done")

producer = KafkaProducer(bootstrap_servers=brokers)#,
                  #       security_protocol='SSL',
                  #       ssl_context=ssl_context)

# Asynchronous by default
i=0
while True:
	print("Sending message " + str(i))
	future = producer.send(topic_prefix + 'default', b'Message: ' + str(i) )
	# Block for 'synchronous' sends
	try:
	    record_metadata = future.get(timeout=10)
	except KafkaError:
	    pass
	i=i+1
	time.sleep(sleep_time)
