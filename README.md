# barcode-lossless-compressor
The goal of this project is to design and produce a compressor that losslessly compresses the gray-scale barcode images. It also includes a decoder that is capable of fully reverse the compression process.


# Usage
```bash
python3 barcode_encoder.py barcode_image.png compressed_file.bin
python3 barcode_decoder.py compressed_file.bin recovered_barcode_image.png
```

# Results
After encode and decode 514 gray-scale barcode images, the final average data rate in bits per sample (BPS) of the
compressed files is 0.783. 
