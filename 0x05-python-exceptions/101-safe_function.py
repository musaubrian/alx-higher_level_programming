#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        function_result = fct(*args)
        return function_result
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
