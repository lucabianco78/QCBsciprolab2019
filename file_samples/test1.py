"""exercise2.py"""

from Bio import SeqIO
import matplotlib.pyplot as plt





def trimRead(read, minQ):
    """returns the read with all bases at 3' with qual < minQ trimmed off"""
    values = read.letter_annotations["phred_quality"]
    #print(read.seq)
    #print(values)
    ind = len(read)-1
    while(ind >= 0):
        if(values[ind] >= minQ):
            break
        ind -= 1
            
    s = read[0:ind]
    #print(s.seq)
    #print(s.letter_annotations["phred_quality"])
    return s

def cleanFile(in_file,out_file,minQ, minLen):
    """quality trims reads in input and writes those longer than minLen to out_file"""
    records = []
    cnt = 0
    for seq_record in SeqIO.parse(in_file, "fastq"):
        cnt += 1
        s=trimRead(seq_record,minQ)
        if(len(s) > minLen):
            records.append(s)
        
    print("Total number of reads in input: {}".format(cnt))
    print("Reads written to output file: {}".format(len(records)))
    SeqIO.write(records,out_file, "fastq")

def plotStats(in_file):
    dataDict = dict()
    for seq_record in SeqIO.parse(in_file, "fastq"):
        quals = seq_record.letter_annotations["phred_quality"]
        for i in range(0,len(quals)):
            if(i not in dataDict):
                dataDict[i] = [quals[i]]
            else:
                dataDict[i].append(quals[i])
    
    vals = []
    for el in range(len(dataDict)):
        vals.append(sum(dataDict[el])/len(dataDict[el]))
    
    plt.plot(vals)
    plt.xlabel("Position")
    plt.ylabel("Quality value")
    plt.show()
    plt.close()
    
    
myfile = "test_reads_75k.fastq"
outfile = "filtered_reads_75k.fastq"
cleanFile(myfile, outfile, 32,50)
print("Original file plot:")
plotStats(myfile)
print("Trimmed file plot:")
plotStats(outfile)
