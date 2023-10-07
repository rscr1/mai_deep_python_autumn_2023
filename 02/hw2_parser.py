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
                        if keyword_callback is not None and keyword in value:
                            keyword_callback(keyword, field, value)
                            break
