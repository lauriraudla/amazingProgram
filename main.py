import git
#from git import Repo
import os

a = 0
count = 0

file = open("last_cp.txt")

for x in file:
    if count == 0:
        count = int(x)
    elif a == 0:
        a = int(x)
file.close()


folder = os.getcwd()
repo = git.Repo(folder)

def git_push():
    try:
        repo = git.Repo(folder)
        repo.git.add(update=True)
        repo.index.commit(str(count))
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print("pizdets")

while True:
    b = str(a)[::-1]
    if str(a) == b:
        break
    else:
        a = a+int(b)
        count += 1
        if count % 1000 == 0:
            file = open("last_cp.txt",'w')
            file.write(str(count)+"\n")
            file.write(str(a)+"\n")
            file.close()
            print(count)
            git_push()
        #print(a)

file = open("last_cp.txt",'w')
file.write(str(count)+"\n")
file.write(str(a)+"\n")
file.close()
git_push()
