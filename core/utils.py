def str2bool(inp:str)->bool:
    if type(inp) != str:
        return False
    inp = inp.lower()
    if inp == "true":
        return True
    else:
        return False