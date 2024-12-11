if __name__ == "__main__":
    import os
    inDir = os.environ['GENOMICS_DATA_BASE'] + '/annotations/s_aureus/'
    outDir = os.environ['GENOMICS_DATA_BASE'] + '/genome_nlp_tokens/sample'
    for file in os.listdir(inDir):
        print('file: ', file)
        if (file.endswith('.gff3') and (('AH19F045' in file) or ('AH18K016' in file) or ('AH21A010' in file))):
            with open((inDir + '/' + file), mode='r') as in_file, open((outDir + '/' + file), mode='w') as out_file:
                for line in in_file.readlines():
                    if '##FASTA' in line:
                        break
                    out_file.write(line)
