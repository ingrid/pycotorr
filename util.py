# Utility methods!

def extract_meta_data(file):
    meta_data = bdecode(open(file, 'rb').read())
    return meta_data
