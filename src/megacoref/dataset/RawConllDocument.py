from typing import List


class RawConllDocument:
    """
    Represents a document with its number, title, and text content.

    Attributes:
        doc_id (str): Document identifier number
        title (str): Document title
        content (List[str]): Lines of text in the document
    """

    def __init__(self, title: str = "Untitled" , subtitle: str = "None", content: List[str] = None):
        self.title = title
        self.subtitle = subtitle
        self.content = content or []

    def add_line(self, line: str) -> None:
        """Add a line to the document content."""
        self.content.append(line)

    def add_word(self, word: str) -> None:
        """Add a word to the document content."""
        if not self.content or self.content[-1] == '\n':
            self.content.append(word)
        else:
            self.content[-1] += ' ' + word

    def __str__(self) -> str:
        """String representation of the document."""
        title_string = f"Document {self.title} / {self.subtitle}"


        return title_string + '\n' + '\n'.join(self.content)

    def __repr__(self) -> str:
        return self.__str__()