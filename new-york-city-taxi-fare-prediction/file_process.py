import os
with open('tmp.csv','w') as tmp:

    with open('train.csv','r') as infile:
        for linenumber, line in enumerate(infile):
            if linenumber <= 1000000:
                tmp.write(line)

# copy back to original file. You can skip this if you don't
# mind (or prefer) having both files lying around
with open('tmp.csv','r') as tmp:
    with open('train.csv','w') as out:
        for line in tmp:
            out.write(line)

os.remove('tmp.csv') # remove the temporary file
