from aiohttp.web_response import Response
from apps.search.models import Post
from elasticsearch import AsyncElasticsearch
from store.accessor import Accessor
from web.exceptions import NotFound

es = AsyncElasticsearch([{"host": "elasticsearch"}])


class SearchAccessor(Accessor):
    async def get(self, text):
        id_list = []
        resp = await es.search(
            index="posts_index",
            body={
                "from": 0,
                "size": 20,
                "query": {"match": {"text": text}},
                "sort": {"created_date": {"order": "desc"}},
            },
        )
        for hit in resp["hits"]["hits"]:
            _id = hit["_source"]["id"]
            id_list.append(_id)
        posts = (
            await Post.query.where(Post.id.in_(id_list))
            .order_by(Post.created_date.desc())
            .gino.all()
        )
        return posts

    async def delete(self, id):
        post = await Post.query.where(Post.id == id).gino.first()
        if post is None:
            raise NotFound
        await es.delete(index="posts_index", id=id)
        await Post.delete.where(Post.id == id).gino.status()

        return Response(body="Post Deleted", status=200)
