import json


def parse_json(json_str, required_fields=None, keywords=None, keyword_callback=None):
    '''
    Parser function to parse JSON string

    :param json_str: JSON string to parse
    :param required_fields: list of required fields to check
    :param keywords: list of keywords to match in the fields
    :param keyword_callback: callback function to handle matching keywords
    '''
    json_dict: dict = json.loads(json_str)
    if required_fields is not None:
        for field in required_fields:
            if field in json_dict:
                value: str = json_dict[field]
                if keywords is not None:
                    for keyword in keywords:
                        if keyword_callback is not None:
                            keyword_callback(keyword, field, value)
                            break


def keyword_handler(keyword, field, value):
    '''
    Test function to handle matching keywords in fields

    :param keyword: keyword found
    :param field: field name where the keyword was found
    :param value: value of the field
    '''
    print(f"Keyword '{keyword}' found in field '{field}' with value '{value}'")


JSON: str = "{'key1': 'Word1 word2', 'key2': 'word2 word3'}"
REQUIRED: list = ['key1']
KEYWORDS: list = ['word2']

parse_json(JSON, REQUIRED, KEYWORDS, keyword_handler)
