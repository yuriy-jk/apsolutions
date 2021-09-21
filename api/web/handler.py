import json
from typing import Optional, Mapping, NoReturn

from aiohttp import web
from marshmallow import ValidationError


def my_error_handler(
    error: ValidationError,
    error_headers: Optional[Mapping[str, str]] = None,
) -> NoReturn:
    raise web.HTTPBadRequest(
        body=json.dumps(
            {
                "code": "invalid_data",
                "description": "Invalid data",
                "data": error.messages,
            }
        ),
        headers=error_headers,
        content_type="application/json",
    )
