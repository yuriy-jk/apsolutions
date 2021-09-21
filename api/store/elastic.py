# from aiohttp import web
# from elasticsearch import AsyncElasticsearch
#
# from store.accessor import Accessor
#
#
# class ElasticAccessor(Accessor):
#     def __init__(self, app: web.Application):
#         super().__init__(app)
#         self.es = None
#
#     async def _on_connect(self, _):
#         self.es = AsyncElasticsearch()
#
#     async def _on_disconnect(self, _) -> None:
#         await self.es.close()
