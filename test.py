from crpapi import CRP
crp = CRP('94fa7641a896614ab429750e81691137')

# get a specific legislator by CID
cand = crp.candidates.get('N00007360')
print(cand['@attributes']['lastname'])
