def url_builder(url, **kwargs):
    api_url = url
    for argument in kwargs:
        if kwargs[argument]:
            api_url = api_url + '?' + argument + '=' + kwargs[argument]
    return url