import logging
import time
import os

# Criação da pasta de logs se não existir
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração básica do logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'service.log'),
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Loop para gerar logs a cada minuto
while True:
    print("Criando log")
    try:
        # Simulando uma exceção
        raise ValueError("Simulated exception")
    except Exception as e:
        logging.error("An exception occurred", exc_info=True)
    time.sleep(4)
