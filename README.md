# django-sqs-lambda

Este projeto consiste em uma API simples que tem operações de CRUD para um
recurso e durante a criação do recurso envia uma mensagem para uma fila AWS SQS.

## Configuração

Para configurar, deve-se ter os seguintes recursos instalados e configurados na máquina:
- _Docker_
- _awscli_, ou apenas configurar as credenciais da AWS no arquivo _~/.aws/credentials_.
- NodeJS (o projeto foi testado na versão 16.19.1)

Com as ferramentas configuradas, vamos fazer o clone do seguinte projeto 
[projeto SQS-Consumer usando o Framework Serverless](https://github.com/carlosTJunior/aws-python-sqs-worker-project.git).
Ao fazer o clone desse projeto, devemos entrar no projeto e executar os comandos:
- **npm install**: vai instalar as dependências e colocá-las no diretório _node_modules_
- **sls deploy**: vai executar o arquivo _serverless.yml_ e criar toda a infraestrutura necessária
na AWS usando o framework Serverless.

Após criar a infraestrutura na AWS, verificar a URL da fila SQS gerada, que deverá ser utilizada posteriormente
Antes de executar o arquivo _docker-compose.yml_ é importante exportar as seguintes
variáveis de sistema:

- **AWS_ACCESS_KEY_ID**: indica o atributo correspondente no arquivo _~/.aws/credentials_.
- **AWS_SECRET_ACCESS_KEY**: indica o atributo correspondente no arquivo _~/.aws/credentials_.
- **AWS_DEFAULT_REGION**: indica o atributo correspondente no arquivo _~/.aws/credentials_.
- **AWS_SQS_QUEUE_URL**: indica a URL da fila para o qual será enviado a mensagem.

Essas variáveis são necessários para que a aplicação que executa dentro do container 
consiga enviar os dados para a AWS.

## API

O recurso utilizado na API se chama _TransferOrder_ e é uma simples representação de
uma ordem de transferência de algo contável(poderia ser dinheiro, nesse caso deveria 
ser indicado a moeda utilizada, além de usar um tipo de dado mais preciso, porém,
é apenas uma representação) de uma conta para outra. A motivação para usar esse recurso
é instigar a pensar numa forma de se processar a mensagem apenas uma vez, já que uma transferência
não necessariamente é uma operação idempotente (quem vai processar a operação deverá utilizar
mecanismos que permitam identificar que uma transação já foi processada antes).

## Metodos da API

### GET
### POST
### DELETE
### UPDATE
