from textnode import TextNode
from textnode import TextType as tt
def main():
    text = TextNode(
        "Ja moin",
        tt.PLAIN_TEXT,
        "https://boot.dev"
    )
    print(text)



if __name__ == "__main__":
    main()