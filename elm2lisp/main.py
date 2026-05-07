#!/usr/bin/env python3
# elm2lisp - Elm to lisp preprocessor
#

# FIXME: Deprecation warning when importing the Language
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from tree_sitter import Language, Parser
import tree_sitter_elm
language = Language(tree_sitter_elm.language())

parser = Parser(language)
# parser.set_language(language)

elm = b"""module Main exposing (main)

import Html exposing (text)

main =
  text "Hello!"
"""

tree = parser.parse(elm)
print(tree.root_node)
