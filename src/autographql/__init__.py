"""AutoGraphQL: schema-driven generation of NL2GraphQL datasets.

Turns a GraphQL SDL schema into validated (schema, natural-language query,
GraphQL query) triples, covering aliases, directives, fragments, inline
fragments, filters, pagination and mutations.
"""
__version__ = "0.1.0"

from .query_generator_app import GraphQLQueryGeneratorApp

__all__ = ["GraphQLQueryGeneratorApp", "__version__"]
