from aiohttp import web

from apps.search.views import SearchView


def setup_search_urls(app: web.Application):
    app.router.add_view("/search.id", SearchView)
