INPUTFIELD = 'INPUTFIELD'


def check(line):
    if INPUTFIELD in line:
        return ''
    return line



def parse(FILE):
    with open(FILE) as fr:
        with open(FILE+'.tmp', 'w') as fw:
            for line in fr.readlines():
                 fw.write(check(line))


