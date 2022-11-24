# import OS for environment variables
import json
import os

# import requests
import requests


def google_search(query_text):
    url='https://customsearch.googleapis.com/customsearch/v1'
    cx='21f70c2b29d284393'
    search_key = os.environ['WEB_API_KEY']
    parameters = {
        "q" : query_text,
        "cx" : cx,
        'key' : search_key,
    }
    page=requests.request("GET",url,params=parameters)
    results = json.loads(page.text)
    print(type(results))
    print(results)

    try:
        if results.get('items') == None:
            return 'Please Crop your question or send clearer image'
        print(results['items'])
        # return [results['items'][3],results['items'][2],results['items'][1],results['items'][0]]
        
        top_output =  [results['items'][0],results['items'][1],results['items'][2],results['items'][3]]
        output = top_output[0]['snippet'] + '\n' + top_output[0]['link'] + '\n\n' + top_output[1]['snippet'] + '\n' + top_output[1]['link']
    except KeyError as error:
        return 'Mathcing results not found ! Please Crop your question or send clearer image or make sure doubt mostly comprise of text'
    return output







 