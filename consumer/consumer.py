# Consumer.py
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import os,time #, ssl

# First get all info from the env
 #ca = os.environ.get('CLOUDKARAFKA_CA')
 #cert = os.environ.get('CLOUDKARAFKA_CERT')
 #key = os.environ.get('CLOUDKARAFKA_PRIVATE_KEY')

 #with open("/tmp/ca.pem", "w") as f:
 #    f.write(ca)
 #with open("/tmp/cert.pem", "w") as f:
 # #    f.write(cert)
 #with open("/tmp/key.pem", "w") as f:
  #   f.write(key)

 #ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

 #ssl_context.verify_mode = ssl.CERT_REQUIRED
 #ssl_context.check_hostname = True
 #ssl_context.load_verify_locations("/tmp/ca.pem")
 #ssl_context.load_cert_chain('/tmp/cert.pem', '/tmp/key.pem')

brokers = os.environ.get('KAFKA_BROKERS').split(',')
topic_prefix = os.environ.get('KAFKA_TOPIC_PREFIX')
sleeptime = float(os.environ.get('CONSUMER_SLEEP_TIME'))

print ("Wait 5s for kafka to settle...")
time.sleep(5)
print ("Done")
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic_prefix + 'default',
                         group_id='my-group',
                         bootstrap_servers=brokers) #,
#                         security_protocol='SSL',
#                         ssl_context=ssl_context)
print ('Start consuming')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("key=%s value=%s" % (message.key, message.value))
    time.sleep(sleeptime)
