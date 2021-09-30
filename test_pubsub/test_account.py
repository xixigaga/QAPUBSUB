from QAPUBSUB import consumer


c = consumer.subscriber_routing(user='guest',password='guest', routing_key='100002', exchange='QAACCOUNT', durable=True)
c.callback = lambda x, y, body, z: print(z)
c.start()
