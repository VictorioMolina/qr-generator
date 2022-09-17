# @victoriomolina

# Command Line Arguments
# argv[1] = data to be encoded
# argv[2] = output file name

import sys
import qrcode

# Get the program args
data = sys.argv[1];
output_file_name = sys.argv[2];

# Generate the QR
img = qrcode.make(data);

# Fave the QR in the file system
img.save(output_file_name);
