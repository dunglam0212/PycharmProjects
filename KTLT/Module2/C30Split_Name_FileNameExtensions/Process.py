def Return_FileNameExtentions(path):
    parts = path.split("\\")
    return parts[len(parts)-1]

def Return_Filename(path):
    parts = path.split("\\")
    filename_parts = parts[len(parts)-1].split(".")
    return filename_parts[0]

