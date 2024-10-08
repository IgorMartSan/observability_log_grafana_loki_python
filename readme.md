# Tutoriais que foram utilizandos:

https://www.youtube.com/watch?v=8rJ0rYb4c_U
https://docs.techdox.nz/loki/


# Projeto de Monitoramento com Loki, Promtail e Grafana

Este projeto configura um ambiente de monitoramento de logs usando Loki, Promtail e Grafana. Ele permite a coleta, processamento e visualização de logs em tempo real, facilitando a análise e o diagnóstico de sistemas distribuídos. Para simular os logs basta executar o log_creator direcinado para a pasta ${PATH_LOGS} no .env.

### Serviços

- **Loki**: Configurado para escutar na porta `3100`. O arquivo de configuração do Loki é montado a partir de um arquivo local (`./loki-config.yaml`).
  
- **Promtail**: Depende do Loki e é configurado para escutar logs de um diretório no host definido pela variável de ambiente `${PATH_LOGS}`. Ele é responsável por enviar esses logs para o Loki. Ele usa a porta `9080`.

- **Grafana**: Interface web para visualização e análise dos logs armazenados no Loki. A interface web é acessível na porta `4000` do host (mapeada para a porta `3000` do contêiner).


## Instruções para Execução

### Pré-requisitos

- Docker e Docker Compose instalados no sistema.
- A variável de ambiente `${PATH_LOGS}` deve apontar para o diretório onde os logs a serem coletados estão localizados.

### Passos para Executar

Docker compose up --build

Após execute o criador de log para testar a arquitetura referênciando a pasta onde os logs estão sendo monitorados


## Descrição dos Serviços

Este projeto utiliza três serviços principais:

1. **Loki**: Um sistema de agregação de logs altamente escalável desenvolvido pela Grafana. Ele coleta, indexa e armazena logs para consulta posterior.
2. **Promtail**: Responsável por coletar logs de arquivos no sistema e enviar para o Loki. Ele é configurado para coletar os logs de um diretório específico no host.
3. **Grafana**: Plataforma de visualização que se conecta ao Loki para exibir os logs em dashboards customizados.

## Arquitetura do Projeto

O projeto utiliza Docker para orquestrar os contêineres dos três serviços, configurando-os em uma rede Docker chamada `loki`. Os volumes são montados para compartilhar arquivos de configuração e logs entre o host e os contêineres.



## Configuração Personalizada

Você pode ajustar as configurações do Loki e Promtail editando os arquivos `loki-config.yaml` e `promtail-config.yaml`. Certifique-se de reiniciar os serviços após qualquer alteração de configuração.
