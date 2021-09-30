from QAPUBSUB import producer

import json

c = producer.publisher_routing(exchange='qamdgateway',exchange_type='fanout', durable=True)

c.pub(json.dumps({'account_cookie': 'aa', 'code': '000001'}), routing_key='All')
