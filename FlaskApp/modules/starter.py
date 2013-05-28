import subprocess

def start(cmd=None):
    # cmd = "./test.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=256*1024*1024)
    output, errors = p.communicate()
    if p.returncode:
        raise Exception(errors)
    else:
        # Print stdout from cmd call
        return output

# Or just import it )))