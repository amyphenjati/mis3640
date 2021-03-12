def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    with open(source, 'r') as f_r:  #  r is for read
        with open(dest, 'w') as f_w:  # w for write
            for line in f_r:
                new_line = line.replace(pattern, replace)
                f_w.write(new_line)


def main():
    pattern = " man "
    replace = " woman "
    source = "data/output.txt"
    dest = "data/output2.txt"
    sed(pattern, replace, source, dest)


if __name__ == "__main__":
    main()
