#!/usr/bin/env python

# This has to run as user omero-server.
# Assumes that omero-upload was installed on the server.
# git clone https://gitlab.com/idr/idr0082-pennycuick-lesions.git
# cd idr0082....
# cp attachments.txt /tmp
# cp upload_attachments.py /tmp
# chmod +x /tmp/upload_attachments.py
# sudo su omero-server
# cd /tmp
# . /opt/omero/server/venv3/bin/activate
# python upload_attachments.py

match = 0
match_count = 0
no_match_count = 0
attachment_file = "./experimentA/experimentA-filePaths"    # "/tmp/attachments.txt"
dataset_names = ["C127_H4K5ac", "C127_H3K36me2", "C127_RNAPIIS2P", "C127_H3K4me2",
                 "C127_H3K27me3", "C127_H3K9me2", "C127_SAF-A", "C127_Smc3", "C127_CTCF", "C127_Macro-H2A", 
                 "C127_H3K4me3", "C127_aHP1", "C127_SCC1", "C127_H3K36me3", "C127_H4K20me1",
                 "C127_30min-BrUTP", "C127_H3K9me3", "C127_H4K20me3", "C127_hnRNP", "HeLa_Rad21",
                 "HeLa_H3K4me3", "HeLa_H3K9me3", "HeLa_H3K27me3", "HeLa_hnRNPC", "HeLa_RNAP-S2P"]

def process_line(line, count, match):
    # /uod/idr/filesets/idr0082-pennycuick-lesions/20200417-ftp/S1_HandE.ndpi.ndpa
    # /uod/idr/filesets/idr0082-pennycuick-lesions/20200417-ftp/S2_HandE.ndpi.ndpa
    parts = line.split('/')
    length = len(parts)
#    print(parts[length-1])
    parts_of_im_names = parts[length-1].split('_')
    for dataset_name in dataset_names:
        dataset_name_parts = dataset_name.split('_')
        for parts_of_im_name in parts_of_im_names:
            if (parts_of_im_name == dataset_name_parts[1]):
                match = 1
                #print (parts_of_im_name)
                #print ("match")
            detailed_parts_of_names = parts_of_im_name.split('-')
            if (match == 0): 
                for detailed_parts_of_name in detailed_parts_of_names:
                    #print (detailed_parts_of_name)
                    if (dataset_name_parts[1] in detailed_parts_of_name):
                        match = 1
                    if (detailed_parts_of_name in dataset_name_parts[1]):
                        match = 1
    return match


with open(attachment_file) as fp:
    line = fp.readline().strip()
    count = 0
    while line and len(line) > 0:
        count += 1

        print("Line %d" % count)
        print (line)
        match = process_line(line, count, 0)
        line = fp.readline().strip()
        if (match == 1):
            match_count += 1
            print ("match")
        else:
            no_match_count += 1
            print ("no match")
print ("match_count")
print (match_count)
print ("no match_count")
print (no_match_count)


