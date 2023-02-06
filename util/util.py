from flask_apispec.views import MethodResource
from flask import Blueprint

from settings import docs


def swagger_docs_register(view_object: MethodResource, blueprint: Blueprint) -> None:
    docs.register(view_object, blueprint=blueprint.name, endpoint=view_object.__name__.lower())
