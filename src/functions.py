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


        split_text = old_node.text.split(delimiter)
        if len(split_text) == 0:
            continue
        if not len(split_text) % 2 == 1:
            raise Exception("Invalid text delimiter")

        for i in range(0, len(split_text)):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = []

    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    matches.extend(images)

    return matches

def extract_markdown_links(text):
    matches = []

    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    matches.extend(links)

    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type == TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for image in images:
            image_alt = image[0]
            image_url = image[1]

            remaining_text = original_text.split(f"![{image_alt}]({image_url})", 1)

            if remaining_text[0]:
                new_nodes.append(TextNode(remaining_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            original_text = remaining_text[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type == TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for link in links:
            link_alt = link[0]
            link_url = link[1]

            remaining_text = original_text.split(f"[{link_alt}]({link_url})", 1)

            if remaining_text[0]:
                new_nodes.append(TextNode(remaining_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))

            original_text = remaining_text[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):

    initial_nodes = [TextNode(text, TextType.TEXT)]
    bold_split_nodes = split_nodes_delimiter(initial_nodes, "**", TextType.BOLD)
    italic_split_nodes = split_nodes_delimiter(bold_split_nodes, "_", TextType.ITALIC)
    code_split_nodes = split_nodes_delimiter(italic_split_nodes, "`", TextType.CODE)
    image_extract_nodes = split_nodes_image(code_split_nodes)
    link_split_nodes = split_nodes_link(image_extract_nodes)
    return link_split_nodes























