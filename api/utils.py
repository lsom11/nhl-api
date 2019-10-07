def url_query_builder(queryParams):
    query = '?'
    for queryParam in queryParams:
        if queryParams[queryParam]:
            query = query + '&' + queryParam + '=' + queryParams[queryParam]
    if len(query) == 1: return ''
    return query