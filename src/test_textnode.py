import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode(
            "This is a test node",
            TextType.BOLD
        )
        node2 = TextNode(
            "This is a test node",
            TextType.BOLD
        )
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode(
            "This is a test node",
            TextType.CODE,
            "https://boot.dev"
        )
        node2 = TextNode(
            "This is a test node",
            TextType.CODE,
            "https://boot.dev"
        )
        self.assertEqual(node, node2)

    def test_not_eq_without_url(self):
        node = TextNode(
            "This is a test node",
            TextType.BOLD
        )
        node2 = TextNode(
            "This is a test node",
            TextType.ITALIC
        )
        self.assertNotEqual(node, node2)

    def test_not_eq_with_url(self):
        node = TextNode(
            "This is a test node",
            TextType.CODE,
            "https://boot.dev"
        )
        node2 = TextNode(
            "This is a test node",
            TextType.CODE,
            "https://google.com"
        )
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()