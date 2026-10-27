"""AutoGraphQL: schema-driven generation of NL2GraphQL datasets.

Turns a GraphQL SDL schema into validated (schema, natural-language query,
GraphQL query) triples, covering aliases, directives, fragments, inline
fragments, filters, pagination and mutations.
"""
try:
    # Written at build time by hatch-vcs from the git tag.
    from ._version import __version__
except ImportError:                      # running from a source tree, not installed
    __version__ = "0.0.0.dev0"

from .query_generator_app import GraphQLQueryGeneratorApp

__all__ = ["GraphQLQueryGeneratorApp", "__version__"]
