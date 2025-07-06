# I want to define a documnent type like this
# Document number 1 / document title / textx


from typing import List, Dict, Any

from megacoref.dataset.RawConllDocument import RawConllDocument


def parse_nll_file(nll_file_path):
    documents: List[RawConllDocument] = []
    current_document = None

    with open(nll_file_path, 'r', encoding="utf-8") as file:
        content = file.readlines()

    for line in content:
        line = line.strip()
        if line.startswith("#end document"):
            if current_document is not None:
                documents.append(current_document)
                current_document = None
                print(documents)
        elif line.startswith("#begin document"):
            line_parts = line.split()
            title = line_parts[2] if len(line_parts) > 2 else "Untitled"
            subtitle = ' '.join(line_parts[3:]) if len(line_parts) > 3 else "Untitled Subtitle"
            current_document = RawConllDocument(title=title, subtitle=subtitle)
        else:
            if current_document is None:
                continue  # Skip lines that appear before a document begins

            line_parts = line.split()
            if len(line_parts) == 0:
                # If the line is empty, we add a new line to the current document
                current_word = '\n'
            elif len(line_parts) > 3:  # Make sure we have enough elements
                # The third word is picked (index 3)
                current_word = line_parts[3]
            else:
                continue  # Skip lines with insufficient elements

            current_document.add_word(current_word)

    # Don't forget to add the last document if we haven't reached an end marker
    if current_document is not None:
        documents.append(current_document)

    return documents



parse_nll_file("D:\Projects\MegaCoref\src\megacoref\dataset\dem_all_corrected.conll")
