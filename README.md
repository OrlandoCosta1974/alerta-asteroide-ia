# 🪐 Alerta Asteroide IA

Uma aplicação web em Python que utiliza IA para monitorar e pesquisar informações sobre Asteroides Potencialmente Perigosos (PHAs) que possam representar risco para a Terra.

---

## 📖 Descrição

Este agente é especializado em:

- Receber o nome de um asteroide (ex: Apophis, Bennu) ou gerar um relatório geral.  
- Buscar, via API e/ou IA, dados relevantes como:  
  - Diâmetro estimado  
  - Probabilidade de aproximação  
  - Data do próximo encontro  
  - Consequências de impacto  
- Apresentar de forma clara no navegador, com interface construída em Streamlit.

---

## ⚙️ Funcionalidades Principais

- **Entrada de nome**: campo para digitar o nome do asteroide.  
- **Relatório geral**: opção de obter um overview de todos os PHAs conhecidos.  
- **Monitoramento em tempo real**: (opcional) atualização automática de dados.  
- **Alertas por e-mail/Slack**: (opcional) notificação quando um asteroide atingir certo limiar de proximidade.

---

## 🛠 Tecnologias & Dependências

- **Linguagem**: Python 3.8+  
- **Framework web**: Streamlit  
- **IA**: OpenAI GPT-3.5/4 via `openai` Python SDK  
- **Chamadas HTTP**: `requests` (para consumo de APIs externas, ex: NASA)  
- **Gerenciamento de ambiente**: `python-dotenv`  

> _Veja o arquivo `requirements.txt` para a lista completa de pacotes._

---

## 📋 Pré-requisitos

1. Ter instalado:
   - Python 3.8 ou superior  
   - Git  
2. Conta na OpenAI (para obter sua `OPENAI_API_KEY`)  
3. _(Opcional)_ Conta na NASA Developer (para `NASA_API_KEY`)  

---

## 🚀 Instalação e execução local

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/AlertaAsteroideIA.git
cd AlertaAsteroideIA

# 2. Crie e ative um ambiente virtual
python -m venv .venv
# no Windows
.venv\Scripts\activate
# no macOS/Linux
source .venv/bin/activate

# 3. Instale as dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configure variáveis de ambiente
cp .env.example .env
# Edite o `.env` e insira suas chaves:
# OPENAI_API_KEY=...
# NASA_API_KEY=...  (se usar dados da NASA)

# 5. Execute a aplicação
streamlit run app.py

☁️ Deploy
Você pode hospedar seu app de várias formas:

Streamlit Community Cloud

Faça login em https://share.streamlit.io

Aponte para seu repositório

Configure as variáveis de ambiente no painel

Heroku

Crie um Procfile com:
web: streamlit run app.py --server.port=$PORT

git push heroku main

Defina suas Config Vars no dashboard do Heroku

Docker

Crie um Dockerfile (exemplo abaixo)

docker build -t alerta-asteroide-ia .

docker run -e OPENAI_API_KEY=... -p 8501:8501 alerta-asteroide-ia

FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

🎯 Uso
Abra a página principal.

No campo “Digite o nome de um asteroide…”, informe o nome (ex: Apophis) ou deixe em branco para relatório geral.

Aguarde a IA/API retornar o texto.

Visualize dados de risco e próximos passos.

🤝 Contribuição
Faça um fork deste repositório.

Crie uma branch com sua feature:
git checkout -b feature/nova-funcionalidade

Faça seus commits e push para o seu fork.

Abra um Pull Request detalhando as mudanças.

📄 Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

👤 Autor
Orlando Costa

📧 orlando.trafegopago@gmail.com

🔗 LinkedIn

yaml
Copiar
Editar


---

> **Próximos passos**:  
> - Ajuste as seções de **Funcionalidades** e **Variáveis de ambiente** conforme suas implementações reais.  
> - Atualize links (GitHub, LinkedIn) e versões de bibliotecas.  

Qualquer dúvida é só falar! Estou à disposição para refinarmos juntos. 😊



