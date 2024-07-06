from datetime import datetime
from crewai import Task

class AiNewslatterTasks():
    def fatch_news_task(self, agent):
        return Task(
            description = f"Coleta noticias relevantes sobre IA nas ultimas 24h. O horario atual é {datetime.now()}.",
            agent = agent,
            async_execution = True,
            expected_output = """Uma Lista dos principais titulos de noticias de IA, URLs e um breve resumo de 
             cada historia das ultimas 24 horas.
              Exemplo de Saída: 
              [
                { 'Titulo': IA é destaque em comerciais do Suber Bowl,
                  'url': 'https://example.com/story1',
                  'resumo': 'A IA fez sucesso nos comerciais do Super Bowl deste ano...'
                },
                {{...}}
              ] """,
            tool = agent,
            params = {"topic": "Inteligência Artificial"},
            output_key = "news_data"
        )
    
    def analyze_news_task(self, agent, context):
        return Task(
            description = "Analisa os dados coletados sobre IA e extrai insights relevantes.",
            agent = agent,
            async_execution = True,
            context = context,
            expected_output = """Uma lista de insights relevantes sobre a IA formatada em markdown com título, resumo e uma referencia
            para a noticia original. Exemplo de Saída:
              '## Inteligência Artificial melhora a eficiência em comerciais\n\n
               **O Resumo:** A IA foi capaz de reduzir o tempo de processamento nas transações do Super Bowl...\n\n
               **Os Detalhes:** \n\n
               - O Comercial do Copilot da Microsoft apresentou seu assistente de IA...\n\n
               **Por que isso é importante:** Embora os anuncios relacionados a IA tenham sido abundantes no ultimo ano, sua presença no 
            """
        )
    
    def compile_newslatter_task(self, agent, context, callback_function):
        return Task(
            description = "Compila os insights relevantes em um boletim informativo.",
            agent = agent,
            context = context,
            callback = callback_function,
            expected_output = """Um boletim informativo em markdown com estilo e layout consistentes. 
            Exemplo de Saída:
              '# Principais noticias de IA hoje\n\n
              - IA é destaque nos comerciais do Super Bowl deste ano... \n\n
              **Os detalhes:**...\n\n
               **Por que isso é importante:** ...\n\n
               ## Altman busca trilhoes de dolares para iniciativa global de chips de IA\n\n
               **O Resumo:**  O CEO da OpenAI, Sam Altman, está supostaente tentando arrecadas trilhoes de dolares... \n\n
               **Os Detalhes:** ...\n\n
               **Por que isso é importante** ...\n\n
               """
        )