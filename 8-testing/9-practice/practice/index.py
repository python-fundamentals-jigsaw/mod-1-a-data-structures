import pdb
def params_string(params):
    return '&'.join([f'{k}={v}' for k, v in params.items()])
