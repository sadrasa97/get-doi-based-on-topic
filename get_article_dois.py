import requests
import pandas as pd
def get_article_dois(topic,rows):
    '''
    Given a topic, returns a list of DOIs for articles related to the topic,
    using the Crossref API.
    '''
    base_url = 'https://api.crossref.org/works'
    query_params = {
        'query.bibliographic': topic,
        'rows': rows,
        'sort': 'relevance'
    }
    response = requests.get(base_url, params=query_params)

    if response.ok:
        article_data = response.json()['message']['items']
        dois = [article['DOI'] for article in article_data]
        df=pd.DataFrame({'topic':topic,'doi':dois})
        return df
    else:
        response.raise_for_status()

# Example usage:
topic = input("give me your topic :")
rows=input('give me your number of article :')
article_dois = get_article_dois(topic,rows)
print(article_dois)