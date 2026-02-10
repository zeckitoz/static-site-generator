from textnode import *
from htmlnode import *
import re

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid text type")
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    return None

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if not old_node.text_type == TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if delimiter not in old_node.text:
            raise Exception("Invalid Markdown-Syntax")

        split_text = old_node.text.split(delimiter)
        if len(split_text) == 0:
            continue

        for i in range(0, len(split_text)):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = []

    alt_text = re.findall(r"!\[(.*?)\]", text)
    urls= re.findall(r"\((\w+:\/\/.*?)\)", text)

    for i in range(0, len(alt_text)):
        matches.append((alt_text[i], urls[i]))

    return matches



















