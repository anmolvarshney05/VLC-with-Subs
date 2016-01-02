import hashlib
import os
# lambda is another method of defining a function
# iter (callable function, iterate until you find this character)
# b"str" interpret b as binary
# with open takes care of closing file automatically

# My Version to get MD5
# def md5(file_path):
#     h = hashlib.md5()
#     with open(file_path, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             h.update(chunk)
#     return h.hexdigest()


def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()
