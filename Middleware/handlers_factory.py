# middleware拦截器，可以将通用的功能从每个URL处理函数中
# 提取出来，集中放在一处

# log处理，不再受限于url
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        # 记录日志
        logging.info('Request: %s %s' % (request.method, request.path))
        # 继续处理请求
        return (yield from handler(request))
    return logger


# 可以在response中不断添加url处理函数
@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(boby=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            resp = web.Response(boby=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            ... # other methods
