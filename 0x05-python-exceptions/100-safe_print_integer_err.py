#!/us/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("Exception: {}".format(sys.stderr.write(Exception))
                return False
