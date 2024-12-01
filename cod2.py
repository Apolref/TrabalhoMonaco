from confluent_kafka import Producer, Consumer, KafkaError

# Função de callback do produtor (para confirmação de entrega)
def delivery_report(err, msg):
    if err is not None:
        print('Falha ao enviar mensagem: {}'.format(err))
    else:
        print('Mensagem enviada para {} [{}]'.format(msg.topic(), msg.partition()))

# Configuração do produtor
producer = Producer({
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
})

# Enviar uma mensagem
producer.produce('my_topic', key='key1', value='Hello Kafka!', callback=delivery_report)
producer.flush()  # Espera a entrega das mensagens

# Configuração do consumidor
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest',
})

consumer.subscribe(['my_topic'])

# Consumir mensagens
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            print('Nenhuma mensagem recebida.')
        elif msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Fim da partição: {}'.format(msg))
            else:
                print('Erro: {}'.format(msg.error()))
        else:
            print('Mensagem recebida: {}'.format(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    consumer.close()