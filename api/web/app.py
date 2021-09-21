from aiohttp import web
from aiohttp_apispec import validation_middleware, setup_aiohttp_apispec

from store import Store
from web.handler import my_error_handler
from web.middlewares import resp_middleware, error_mw
from web.urls import setup_urls


def setup_store(app: web.Application):
    store = Store(app)
    app["store"] = store
    store.setup()


def create_app():
    app = web.Application()
    setup_store(app)
    setup_urls(app)
    app.middlewares.extend([error_mw, resp_middleware, validation_middleware])
    setup_aiohttp_apispec(
        app=app,
        title="My Documentation",
        version="v1",
        url="/docs/open_api.json",
        swagger_path="/docs",
        error_callback=my_error_handler,
    )

    return app


# if __name__ == "__main__":
#     web.run_app(create_app())
