
def getExportName(gs):
    for i in range(1,len(gs.args)):
        if "export" in str(gs.args[i]):
            s = str(gs.args[i]).replace('export:', '')
            print "exporting file to :"+s
            return s
    return False

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
    for i in range(1,len(gs.args)):
        if "input:" in gs.args[i]:
            s = str(gs.args[i]).split(":")
            return s[1]
        else:
            return False


def getModelFile(gs):
    for i in range(1,len(gs.args)):
        if "model:" in gs.args[i]:
            s = str(gs.args[i]).replace("model:","")
            return s
        else:
            return False


def getInterArg(gs):
    for i in range(1,len(gs.args)):
        if "inter:" in gs.args[i]:
            s = str(gs.args[i]).replace("inter:","")
            return s
        else:
            return str(gs.args[i])


def getInteractionFileName(gs):
   for i in range(1,len(gs.args)):
       if "input:" in gs.args[i]:
           s = str(gs.args[i]).replace("input:","")
           return s
       else:
           return False


def getInteractionPert(gs):
    for i in range(1,len(gs.args)):
        if "inter:" in gs.args[i]:
            s = str(gs.args[i]).replace("inter:","")
            return s
        else:
            return False



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

def getPattern(gs):
    for i in range(1,len(gs.args)):
        if "pattern:" in gs.args[i]:
            s = str(gs.args[i]).replace("pattern:", "" )
            return s

def getInputPattern(gs):
    for i in range(1,len(gs.args)):
        if "in:" in gs.args[i]:
            s = str(gs.args[i]).replace("in:", "" )
            return s



def getFix(gs):
    for i in range(1,len(gs.args)):
        if "fix:" in gs.args[i]:
            s = str(gs.args[i]).replace("fix:", "" )
            return s

def getType(gs):
    for i in range(1,len(gs.args)):
        if "type:" in gs.args[i]:
            s = str(gs.args[i]).replace("type:", "" )
            return s


def getSize(gs):
    for i in range(1,len(gs.args)):
        if "sizep:" in gs.args[i]:
            s = str(gs.args[i]).replace("sizep:", "" )
            return s

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
                   if isinstance(splited_arg, list):
                       return splited_arg
                   return splited_arg.split(",")
               except Exception as e:
                   raise
    return []
def getSinglePerturbation(gs):
    for i in range(1,len(gs.args)):
        if "pert:" in gs.args[i]:
            s = str(gs.args[i]).replace('pert:', '')
            return s
    return False
