graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy","alice"]
graph["alice"] = ["peggy","you"]
graph["claire"] = ["thosm", "jonny"]
graph["anuj"] = ["bob"]
graph["peggy"] = ["anuj"]
graph["thosm"] = []
graph["jonny"] = ["asfas"]
graph["asfas"] = ["thom"]

path = []
mark = []
target = "thom"
def find_the_guy(name, target):
    mark.append(name)
    for guy in graph[name]:
        if guy == target:
            path.append(guy)
            path.append(name)
            return True
        elif mark.__contains__(guy):
            continue
        else:
            if find_the_guy(guy, target):
                path.append(name)
                return True
            else:
                continue
    return False

if find_the_guy("peggy", "thom"):
    print("Found!!")
    while path:
        print(path.pop())
else:
    print("pity~")