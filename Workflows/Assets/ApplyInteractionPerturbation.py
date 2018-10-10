
def getExportName(gs):
    for i in range(1,len(gs.args)):
        if "export:" in gs.args[i]:
             return gs.args[i].replace('export:', '')

def getPerturbationSize(gs):
    for i in range(1,len(gs.args)):
        if "size:" in gs.args[i]:
            s = str(gs.args[i]).replace('size:', '')
            splited_arg = s.split("-")
            if len(splited_arg)>1:
                return range(int(splited_arg[0]),int(splited_arg[1])+1)

            else:
                try:
                    return [int(s)]
                except Exception as e:
                    raise
    return [1]


def getInputFileName(gs):
    try:
        for i in range(1,len(gs.args)):
            if "input:" in gs.args[i]:
                s = str(gs.args[i]).split(":")
                return s[1]
    except Exception as e:
        return "not file"


def getInteractionPert(gs):
    for i in range(1,len(gs.args)):
        if "inter:" in gs.args[i]:
            s = str(gs.args[i]).replace("inter:","")
            return s


# def GraphPlot(gs,data):
#     for i in range(1,len(gs.args)):
#         if "graph:" in gs.args[i]:
#             makeGraph(data)

def getRestType(gs):
    for i in range(1,len(gs.args)):
        if "rest:" in gs.args[i]:
            s = str(gs.args[i]).split(":")
            v = [s[1],s[2]]
            return v

def getPerturbations(gs):
    for i in range(1,len(gs.args)):
        p = []
        if "pert:" in gs.args[i]:
            s = str(gs.args[i]).replace('pert:', '')
            splited_arg = s.split("-")
            if len(splited_arg)>1:
                for i in splited_arg:
                    p += i.split(",")
                return p
            else:
               try:
                   return splited_arg.split(",")
               except Exception as e:
                   raise
    return []
