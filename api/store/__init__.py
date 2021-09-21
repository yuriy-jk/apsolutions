from aiohttp import web


class Store:
    def __init__(self, app: web.Application):
        from store.pg import PgAccessor
        from store.gino import GinoAccessor

        self.pg = PgAccessor(app)
        self.gino = GinoAccessor(app)

        from apps.search.accessor import SearchAccessor

        self.search = SearchAccessor(app)

    def setup(self):
        self.pg.setup()
        self.gino.setup()
