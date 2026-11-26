import os

class ReadFileException(Exception):
    pass

class ParseFileException(Exception):
    pass

def read_affil_file(infile=None):
    if infile and os.path.exists(infile):
        try:
            rows = []
            with open(infile, "r") as fr:
                for l in fr.readlines():
                    row = l.rstrip().split("\t")
                    rows.append(row)
            return rows
        except Exception as err:
            raise ParseFileException("Failed to parse affil file: %s" % err)
    else:
        raise ReadFileException("Unable to load affil file: file %s does not exist!" % infile)
