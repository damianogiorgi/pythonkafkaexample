# Producer.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
import os, time #ssl

# First get all info from the env
#ca = os.environ.get('CLOUDKARAFKA_CA')
#cert = os.environ.get('CLOUDKARAFKA_CERT')
#key = os.environ.get('CLOUDKARAFKA_PRIVATE_KEY')
#with open("/tmp/ca.pem", "w") as f:
#    f.write(ca)
#with open("/tmp/cert.pem", "w") as f:
#    f.write(cert)
#with open("/tmp/key.pem", "w") as f:
#    f.write(key)

#ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

#ssl_context.verify_mode = ssl.CERT_REQUIRED
#ssl_context.check_hostname = True
#ssl_context.load_verify_locations("/tmp/ca.pem")
#ssl_context.load_cert_chain('/tmp/cert.pem', '/tmp/key.pem')

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
