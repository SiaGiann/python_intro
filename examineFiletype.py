def examineFiletype(bin, signature):
    bytes = [{'decimal': bin[i], 'hex': hex(bin[i])} for i in range(3)]
    for byte in bytes:
        print(byte['decimal'], byte['hex'])
    return bytes[0]["hex"]+bytes[1]["hex"]+bytes[2]["hex"] == signature

try:
    with open('imag', 'rb') as img:
        data = img.read()
except:
    print("There was an error opening file \"imag\"")
else:
    if examineFiletype(data, '0xff0xd80xff'):
        print("The file is jpg")
    else:
        print("The file is not jpg")
