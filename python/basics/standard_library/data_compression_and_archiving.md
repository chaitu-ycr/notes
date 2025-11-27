# Python Data Compression and Archiving Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to data compression and archiving.

---

## compression.zstd — Compression Compatible with the Zstandard Format

**Description:**  
Provides support for Zstandard (zstd) compression and decompression.

**Usage Example:**
```python
import zstandard as zstd

data = b"example data"
cctx = zstd.ZstdCompressor()
compressed = cctx.compress(data)

dctx = zstd.ZstdDecompressor()
decompressed = dctx.decompress(compressed)
print(decompressed)  # b'example data'
```

---

## zlib — Compression Compatible with gzip

**Description:**  
Provides functions for compressing and decompressing data using the zlib library (compatible with gzip).

**Usage Example:**
```python
import zlib

data = b"example data"
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)
print(decompressed)  # b'example data'
```

---

## gzip — Support for gzip Files

**Description:**  
Enables reading and writing of gzip-compressed files.

**Usage Example:**
```python
import gzip

data = b"example data"
with gzip.open('example.gz', 'wb') as f:
	f.write(data)

with gzip.open('example.gz', 'rb') as f:
	content = f.read()
	print(content)  # b'example data'
```

---

## bz2 — Support for bzip2 Compression

**Description:**  
Provides support for bzip2 compression and decompression.

**Usage Example:**
```python
import bz2

data = b"example data"
compressed = bz2.compress(data)
decompressed = bz2.decompress(compressed)
print(decompressed)  # b'example data'
```

---

## lzma — Compression Using the LZMA Algorithm

**Description:**  
Supports compression and decompression using the LZMA algorithm.

**Usage Example:**
```python
import lzma

data = b"example data"
compressed = lzma.compress(data)
decompressed = lzma.decompress(compressed)
print(decompressed)  # b'example data'
```

---

## zipfile — Work with ZIP Archives

**Description:**  
Allows reading, writing, and extracting ZIP archive files.

**Usage Example:**
```python
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zf:
	zf.writestr('file.txt', 'Hello, ZIP!')

with zipfile.ZipFile('example.zip', 'r') as zf:
	print(zf.read('file.txt'))  # b'Hello, ZIP!'
```

---

## tarfile — Read and Write Tar Archive Files

**Description:**  
Enables reading and writing of tar archive files.

**Usage Example:**
```python
import tarfile

with tarfile.open('example.tar', 'w') as tf:
	tf.add('file.txt')

with tarfile.open('example.tar', 'r') as tf:
	tf.extract('file.txt')
```

---
