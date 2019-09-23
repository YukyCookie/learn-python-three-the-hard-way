import sys
script, input_encoding, error = sys.argv 

def main(language_file, encoding, errors):
    line = language_file.read()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)

languages = open("languages - 副本.txt", 'rb+')
# languages.truncate()
# # utf-8下的编码
# languages.write(b'\xe6\x96\x87\xe8\xa8\x80')
# # utf-16下的编码
# languages.write(b'\xff\xfe\x87e\x00\x8a')
# # utf-32下的编码
# languages.write(b'\xff\xfe\x00\x00\x87e\x00\x00\x00\x8a\x00\x00')

main(languages, input_encoding, error)

# with open('languages3.txt', encoding = 'utf-8') as fp:
#     main(fp, 'utf-8', 'strict')