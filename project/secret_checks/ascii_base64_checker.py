import base64

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        ascii = f.read().isascii()
        print(ascii)
        base64 = isBase64(f.read())
        print(base64)

def main():
    text_file = open("E:\\repos\\neanders-repo\\project\\secret_checks\\swanagent2.txt", "r")
    data = text_file.read()
    ascii = data.isascii()
    print(ascii)
    base64 = isBase64(data)
    print(base64)

if __name__ == "__main__":
    main()