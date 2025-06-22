import streamlit as st
from dotenv import load_dotenv
import os # Importamos a biblioteca OS para acessar as variáveis de ambiente

from langchain_openai import ChatOpenAI  # <-- ESTA É A LINHA QUE PRECISA ESTAR AQUI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate

# -- Configuração da Página e Carregamento de Variáveis de Ambiente --

# Esta função ainda é importante! Ela lê o .env e o torna acessível para o os.getenv()
load_dotenv()

st.set_page_config(page_title="Alerta Asteroide IA", page_icon="☄️")
st.title("☄️ Alerta Asteroide IA")
st.markdown("Este agente é especializado em monitorar e pesquisar informações sobre Asteroides Potencialmente Perigosos (PHAs) que possam representar um risco para a Terra.")


# -- MUDANÇA PRINCIPAL: Carregamento explícito das chaves --

# 1. Carregamos as chaves do ambiente para variáveis Python.
openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# 2. Criamos uma verificação. Se a chave não for encontrada, o programa para com uma mensagem clara.
#    Isso é MUITO melhor para depurar do que o erro genérico.
if not openai_api_key:
    st.error("ERRO: Chave da OpenAI (OPENAI_API_KEY) não encontrada no seu arquivo .env.")
    st.error("Por favor, verifique seu arquivo .env e reinicie a aplicação.")
    st.stop() # Para a execução do app se as chaves não existirem.

if not tavily_api_key:
    st.error("ERRO: Chave da Tavily (TAVILY_API_KEY) não encontrada no seu arquivo .env.")
    st.error("Por favor, verifique seu arquivo .env e reinicie a aplicação.")
    st.stop() # Para a execução do app se as chaves não existirem.


# -- Inicialização do Modelo e Ferramentas com as chaves explícitas --

try:
    # 3. Passamos a chave diretamente para o construtor do ChatOpenAI
    llm = ChatOpenAI(
        model_name="gpt-4o",
        temperature=0.5,
        api_key=openai_api_key # MUDANÇA AQUI
    )

    # 4. Passamos a chave diretamente para a ferramenta da Tavily
    tools = [
        TavilySearchResults(
            max_results=5,
            description="Uma ferramenta de busca na web para encontrar as informações mais atuais sobre astronomia, asteroides, NEOs e PHAs.",
            api_key=tavily_api_key # MUDANÇA AQUI
        )
    ]

    # -- Criação do Prompt do Agente (sem mudanças aqui) --
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
        Você é um analista de dados astronômicos especializado em Objetos Próximos da Terra (NEOs) e Asteroides Potencialmente Perigosos (PHAs). Sua missão é usar a ferramenta de busca para encontrar as informações mais recentes e confiáveis sobre asteroides que possam representar um risco de colisão com a Terra.
        O seu relatório final DEVE tentar incluir os seguintes pontos, se a informação estiver disponível:
        - **Nome do Asteroide:**
        - **Data da Descoberta:**
        - **Diâmetro Estimado:** (em metros ou quilômetros)
        - **Distância Mínima de Passagem da Órbita (MOID):** (em unidades astronômicas ou quilômetros)
        - **Probabilidade de Impacto:** (Mencione a Escala de Palermo ou Torino, se aplicável)
        - **Data da Próxima Passagem Próxima:**
        - **Resumo do Risco Atual:** (Explique de forma clara se há algum risco real segundo as agências espaciais).
        Termine SEMPRE seu relatório com a seguinte nota de rodapé:
        ---
        *Fonte: Informações compiladas a partir de dados públicos na web. Para dados oficiais e em tempo real, consulte o site da NASA (JPL CNEOS) ou da ESA.*
        """),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # -- Construção e Execução do Agente --
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # -- Interface do Usuário com Streamlit --
    user_input = st.text_input("Digite o nome de um asteroide (ex: Apophis, Bennu) ou peça um relatório geral:")

    if user_input:
        with st.spinner("O Agente está escaneando os céus em busca de informações... 🔭"):
            response = agent_executor.invoke({"input": user_input})
            st.subheader("Relatório de Análise de Risco:")
            st.markdown(response["output"])

except Exception as e:
    st.error(f"Ocorreu um erro durante a execução do agente: {e}")