from pdf_downloader import download_pdf
from pdf_analyzer import search_string_in_pdf
from cleaner import delete_directory


path = '/tmp/web_pdf_checker'

download_pdf(path)

# List of strings to check
strings_to_check = [    # ⚠️ Place for strings to check
]

for i in range(len(strings_to_check)):
    print(
        "The string " +
        str(i + 1) +
        " is found in the file: " +
        str(search_string_in_pdf(path + '/file_name.pdf', strings_to_check[i])) # TODO: print the name of the file with a string
    )

delete_directory(path)
