import unittest
from functions import *

class TestFunctions(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_delimiter_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE),
                         [
                             TextNode("This is text with a ", TextType.TEXT),
                             TextNode("code block", TextType.CODE),
                             TextNode(" word", TextType.TEXT),
                         ]
                         )
    def test_delimiter_split_bold(self):
        node = TextNode("This is text with a **bold block** word and a **second bold block** right here", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD),
                         [
                             TextNode("This is text with a ", TextType.TEXT),
                             TextNode("bold block", TextType.BOLD),
                             TextNode(" word and a ", TextType.TEXT),
                             TextNode("second bold block", TextType.BOLD),
                             TextNode(" right here", TextType.TEXT),
                         ]
                         )
    def test_delimiter_split_no_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE),
                         [TextNode("This is a text node", TextType.ITALIC)]
                         )

    def test_delimiter_split_no_delimiter(self):
        node = TextNode("This is __a italic__ text node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)



if __name__ == '__main__':
    unittest.main()
