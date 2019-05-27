
in_file = 'referat.txt'
out_file = 'referat2.txt'

def write_to_referat2(str1: str):
    with open(out_file, "a") as f:
        f.write(str1)

with open(in_file, 'r') as f:
    content = f.read()

    write_to_referat2("String length: {}\n".format(len(content)))
    write_to_referat2("Words count: {}\n".format(len(content.replace(",","").split())))
    write_to_referat2("\n===============================\n\n")
    write_to_referat2("{}\n".format(content.replace(".","!")))


