# Simple SMTP Server

O Simple SMTP Server é uma implementação simples de um servidor de e-mail,
que faz parte do trabalho de Redes 1.

A aplicação foi implementada em Python e pode ser executada a partir de um terminal linux,
Pycharm e VSCode.

## Funcionamento

Foram implementados 4 arquivos: 

    1 - client.py:
        É responsável pela parte do cliente, onde é possível criar uma menssagem para um destinatário.
    2 - server.py:
        É responsável pela parte do servidor SMTP. Ele processa os comandos enviados pelo 
        client.py e realiza as operações de acordo com a especificação do programa. 
    3 - input_output.py:
        É responsável pelo carregamento do arquivo de usuários, requisito para a configuração do servidor.
    4 - init.py:
        Efetua a configuração e a checagem do arquivo de usuários(users.txt), criando a caixa de entrada
        dos usuários na pasta "data", dentro do diretório raiz.

O cliente e o servidor se comunicam através de Sockets.

Exemplo de uso:

    C: RCP TO: <gabriel.araujo>
    S: Destinatário aceito
    C: DATA
    S: Escreve sua mensagem
    C: aksdfjasd sad fasdjfhas dhasd fakjhgfgfg  asjdhajsdha asjdhsda ansdjhasjdh
    C: DATA
    C: alsdkalskdasd asdkjasdk fg fgldk dfddofkd 3 efd  2134 234 2q3 4234 2 34
    C: .
    S: Mensagem enviada com sucesso
    C: 

## Instalação

Pycharm:

    1 - Após clonar o projeto, abra o projeto no pycharm.
    2 - Configure o interpretador para o python 3.8(outras versões devem funcionar, mas não foram testadas).

Terminal Linux:

    1 - Após clonar o projeto, abra a pasta do projeto no VSCode.
    2 - Configure o interpretador para o python 3.8(outras versões devem funcionar, mas não foram testadas).
    
## Como usar
Pycharm:

    1 - Clique no arquivo server.py com o botão direito e execute-o.
    2 - Após a inicializar o servidor com sucesso, repita a etapa acima para o arquivo client.py

Terminal Linux:
    
    1 - Abra uma janela do terminal na pasta do projeto e digite o comando 'python3 server.py'.
    2 - Abra outra janela do terminal na mesma pasta e digite o comando 'python3 client.py'.
    3 - Agora, basta inserir os comandos desejados na janela do terminal na qual foi executado o arquivo do cliente. 
    
Comandos SMTP implementados:

    1 - RCP TO: <destinatário>(seleciona o destinatário da mensagem) 
    2 - DATA (inicia o modo de escrita de mensagem)
    3 - . (envia a mensagem ao destinatário)
##Contribuição:

O programa foi implementado por: 
[Zamp98](https://github.com/Zamp98), 
[araujoG](https://github.com/araujoG) e 
[Goncazevedo](https://github.com/Goncazevedo)

## License
[MIT](https://choosealicense.com/licenses/mit/)
