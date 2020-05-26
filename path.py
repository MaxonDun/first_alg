import os
def tree(folder):
    for root, dir, files in os.walk(folder):
        slash=root.count(os.sep)
        otstup = ' '*4*slash
        otstup_1 = ' '*4*(slash+1)
        print(f"{otstup}{os.path.basename(root)}")
        for file in files:
            print(f"{otstup_1}{files}")


tree("YOUR_PATH")