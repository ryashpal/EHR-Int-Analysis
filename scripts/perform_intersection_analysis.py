import os
import subprocess

import pandas as pd


def getTokensFile(tubeId):
    for file in os.listdir('./'):
            if('token_attributions.bed' in file):
                    if tubeId in file:
                            return file


data = []
for tubeId in ['AH18K016', 'AH19F045', 'AH19K027', 'AH21A007', 'AH21A010']:
    for featureType in ['CDS', 'ncRNA', 'oriC', 'oriT', 'rRNA', 'regulatory_region', 'tRNA', 'tmRNA']:
            annotationsFileName = tubeId + '_' + featureType + '.gff3'
            tokensFileName = getTokensFile(tubeId)
            ps1 = subprocess.run(['bedtools', 'intersect', '-a', tokensFileName, '-b', annotationsFileName, '-wa'], check=True, capture_output=True)
            ps2 = subprocess.run(['uniq'], input=ps1.stdout, capture_output=True)
            ps3 = subprocess.run(['wc', '-l'], input=ps2.stdout, capture_output=True)
            overlapCount = ps3.stdout.decode('utf-8').strip()

            ps4 = subprocess.run(['wc', '-l', tokensFileName], check=True, capture_output=True)
            totalTokensCount = ps4.stdout.decode('utf-8').strip()

            ps4 = subprocess.run(['wc', '-l', annotationsFileName], check=True, capture_output=True)
            totalAnnotationsCount = ps4.stdout.decode('utf-8').strip()

            data.append([tokensFileName.split('.')[0].split('_')[0], tubeId, featureType, totalTokensCount.split(' ')[0], totalAnnotationsCount.split(' ')[0], overlapCount])


print(pd.DataFrame(data))
