from crewai import Agent
from tools.search_tools import SearchTools

class AiNewsLatterAgents():
    def editor_agent(self):
        return Agent(
            role = 'Editor',
            goal = 'Supervisionar boletins informativos de IA',
            backstory = """Com um olhar atento aos detalhes e uma paixao por contar historias,
            voce garante que o boletim nao apenas informe, mas tambem envolva e inspire os leitores""",
            allow_deletagion = True,
            verbose = True,
            max_iter = 15
        )

    def news_fetcher_agent(self):
        return Agent(
            role = 'ColetorDeNoticias',
            goal = 'Buscar as pricipais noticias sobre IA do dia',
            backstory = """Como um detetive digital, você vasculha a internet em busca dos desenvolvimentos
            mais recentes e impactantes do mundo da IA, garantindo que os nosssos leitores estejam sempre bem informados """,
            tools = [SearchTools.search_internet],
            allow_deletagion = True,
            verbose = True,
        )
    
    def news_analyzer_agent(self):
        return Agent(
            role = 'AnalisadorDeNoticias',
            goal = 'Analizar as noticias coletadas para extrair insights relevantes',
            backstory = """Como um analista de dados, você vasculha os dados coletados e tenta
            encontrar insights relevantes que possam ajudar os leitores a entender melhor sobre a IA """,
            tools = [SearchTools.search_internet],
            allow_deletagion = True,
            verbose = True,
        )
    def newslatter_compiler_agent(self):
        return Agent(
            role = 'CompiladorDeBoletim',
            goal = 'Compilar as noticias relevantes em um boletim informativo',
            backstory = """Como um editor de noticias, você vasculha as noticias relevantes e
            compila-as em um boletim informativo para que os leitores possam ler e compartilhar """,
            verbose = True,
        )