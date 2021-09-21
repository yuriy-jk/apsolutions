from aiohttp import web


class BaseView(web.View):
    @property
    def store(self):
        return self.request.app["store"]
