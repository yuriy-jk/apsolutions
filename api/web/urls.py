from aiohttp import web


def setup_urls(app: web.Application):
    from apps.search.urls import setup_search_urls

    setup_search_urls(app)
