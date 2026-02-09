from textnode import *
from htmlnode import *
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








