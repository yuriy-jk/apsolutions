from aiohttp_apispec import response_schema, json_schema, docs

from apps.search.schema import Post, Search, Delete
from web.views import BaseView


class SearchView(BaseView):
    @docs(
        tags=["text_search"],
        summary="Text search view",
        description="Post text for search in elastic",
        responses={200: {"description": "Ok"},
                   500: {"description": "Server error"}},
    )
    @json_schema(Search.Schema)
    @response_schema(Post.Schema)
    async def post(self):
        data = self.request["json"]
        return await self.store.search.get(data.text)

    @docs(
        tags=["delete_post"],
        summary="Delete post view",
        description="Post delete in db and elastic by id",
        responses={200: {"description": "Ok"},
                   500: {"description": "Server error"}},
    )
    @json_schema(Delete.Schema)
    async def delete(self):
        data = self.request["json"]
        return await self.store.search.delete(data.id)
