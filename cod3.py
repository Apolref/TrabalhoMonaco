from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction

# Criar uma carteira Bitcoin
wallet = Wallet.create('my_wallet')

# Verificar o endereço de recebimento da carteira
print("Endereço de recebimento:", wallet.get_key().address)

# Criar uma transação simples
tx = Transaction()
tx.add_input(wallet.get_key())
tx.add_output('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0.001)  # Endereço de destino e valor

# Assinar a transação
tx.sign(wallet)

# Verificar transação antes de enviá-la
print("Transação assinada:", tx.as_dict())

# Enviar a transação (simulado, em uma rede real seria necessário um nó ou serviço como BlockCypher)
# tx.send()  # Descomentar para enviar na rede real


