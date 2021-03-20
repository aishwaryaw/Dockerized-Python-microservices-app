import pika , json, django, os

# as we are accessing Product model outside of the admin module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product
 
params = pika.URLParameters('rabbitmq_url')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Recived in admin')
    body = body.decode('utf-8').replace('\0', '')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased !')

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()