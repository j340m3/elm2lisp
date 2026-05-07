#!/usr/bin/env python3
# elm2lisp - Elm to lisp preprocessor
#

# FIXME: Deprecation warning when importing the Language
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from tree_sitter import Language, Parser
import tree_sitter_elm

def handle_type_declaration(node):
    pass

def handle_type_alias_declaration(node):
    pass

def handle_type_annotation(node):
    pass

def handle_value_declaration(node):
    pass

def handle_case_of_expr(node):
    pass

language = Language(tree_sitter_elm.language())

parser = Parser(language)
# parser.set_language(language)

elm2 = b"""module Main exposing (main)

import Html exposing (text)

main =
  text "Hello!"
"""

elm = b"""bla : Int -> Int
bla x =
    case x of
        1 -> 2
        2 -> 4
        x -> 2*x"""

tree = parser.parse(elm)
cursor = tree.walk()

done = False
while not done:
    match cursor.node.type:
        case "type_declaration":
            handle_type_declaration(cursor.node)
        case "type_alias_declaration":
            handle_type_alias_declaration(cursor.node)
        case "type_annotation":
            handle_type_annotation(cursor.node)
        case "value_declaration":
            handle_value_declaration(cursor.node)
        case "case_of_expr":
            handle_case_of_expr(cursor.node)
        case _:
            pass
    print(cursor.node.type,":", cursor.node.text)
    if not cursor.goto_first_child():
        if not cursor.goto_next_sibling():
            if cursor.goto_parent():
                while not cursor.goto_next_sibling():
                    if not cursor.goto_parent():
                        done = True
                        break
print(tree.root_node)
