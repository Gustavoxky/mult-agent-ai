import json
import os
import requests
from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """useful to search the internet about a given topic and return relevant results"""
        print("Searching the internet...")
        top_result_to_teturn = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps(
            {"q": query, "num": top_result_to_teturn, "tbm": "nws"}
        )
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "No relevant results found in the internet."
        else:
            results = response.json(['organic'])
            string = []
            print("Results:", results[:top_result_to_teturn])
            for result in results[:top_result_to_teturn]:
                try:
                    date = result.get('date', 'Date not available')
                    string.append('\n'.join([
                        f'Title: {result["title"]}',
                        f'URL: {result["link"]}',
                        f'Date: {date}',
                        f'Snippet: {result["snippet"]}',
                        "\n--------------------"
                    ]))
                except KeyError:
                    continue
            return '\n'.join(string)



# GOOGLE_SEARCH_ENGINE_API