def compress_running(text):
    compressed_text = ""
    i = 0
    while i < len(text):
        char = text[i]
        count = 1
        while i + count < len(text) and text[i + count] == char:
            count += 1
        if count > 2:
            compressed_text += str(count) + char
        else:
            compressed_text += char * count
        i += count
    return compressed_text

def decompress_running(compressed_text): 
    decompressed_text = "" 
    i = 0 
    while i < len(compressed_text): 
        if compressed_text[i].isdigit(): 
            count_str = ""
            while i < len(compressed_text) and compressed_text[i].isdigit():
                count_str += compressed_text[i]
                i += 1
            count = int(count_str)
            char = compressed_text[i]
            decompressed_text += char * count 
            i += 1 
        else: 
            decompressed_text += compressed_text[i] 
            i += 1 
    return decompressed_text


def compress_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        text = file.read()
    
    compressed_text = compress_running(text)
    
    with open(output_filename, 'w') as file:
        file.write(compressed_text)

def decompress_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        compressed_text = file.read()
    
    decompressed_text = decompress_running(compressed_text)
    
    with open(output_filename, 'w') as file:
        file.write(decompressed_text)

def main():
    input_filename = "c:/Users/karny/OneDrive/Рабочий стол/study/ИБ/lab_1/Pushkin.txt"
    output_filename = "compressed.txt"
    decompressed_output_filename = "decompressed.txt"
    
    compress_file(input_filename, output_filename)
    decompress_file(output_filename, decompressed_output_filename)

if __name__ == "__main__":
    main()
