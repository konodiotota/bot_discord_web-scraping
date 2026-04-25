🎬 Anitube Discord Bot
Bot para Discord que monitora e envia automaticamente os novos episódios do Anitube diretamente por mensagem privada.

✨ Funcionalidades

Notificação automática diária: A cada 24 horas, o bot busca os últimos lançamentos do Anitube e envia uma mensagem privada para os usuários configurados.
Comando manual: Use .anitube em qualquer canal para ver os lançamentos mais recentes na hora.


🛠️ Tecnologias utilizadas

Python 3
discord.py
BeautifulSoup4
Requests
python-dotenv


📦 Instalação

Clone o repositório:

bash   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

Crie e ative um ambiente virtual (opcional, mas recomendado):

bash   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

Instale as dependências:

bash   pip install discord.py beautifulsoup4 requests python-dotenv

Configure o arquivo .env:
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

env   TOKEN=seu_token_do_bot_aqui

⚙️ Configuração
Token do Bot

Acesse o Discord Developer Portal.
Crie uma aplicação e um bot.
Copie o token e cole no arquivo .env.

IDs dos Usuários
No arquivo bot_anitube_disc.py, edite a lista USUARIOS_ID com os IDs dos usuários que devem receber as notificações:
pythonUSUARIOS_ID = [123456789012345678, 987654321098765432]

Para obter o ID de um usuário no Discord, ative o Modo Desenvolvedor em Configurações → Aparência → Modo Desenvolvedor, depois clique com o botão direito no usuário e selecione "Copiar ID".


▶️ Como usar
Execute o bot com:
bashpython bot_anitube_disc.py
Comandos disponíveis
ComandoDescrição.anitubeExibe os últimos lançamentos do Anitube no chat.

🔔 Notificações automáticas
Assim que o bot iniciar, ele agenda o envio automático de novos episódios uma vez por dia via mensagem privada para todos os usuários listados em USUARIOS_ID.
