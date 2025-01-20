import fitz


def search_string_in_pdf(path, search_string):
    try:
        # Open the file
        document = fitz.open(path)

        # Iterate through each page
        for page_num in range(len(document)):
            page = document.load_page(page_num)

            # Search for the string in the page's text
            if search_string.lower() in page.get_text().lower():
                return True

        # If string is not found in any page
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False
