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

import csv

rows = []
match = 0
full_match = 0
match_count = 0
no_match_count = 0
attachment_file = "./experimentC/experimentC-filePaths"    # "/tmp/attachments.txt"
dataset_names = ["HCT116_H3K27me3-H3K4me3", "HCT116_H3K4me2-H3K36me3", "HCT116_H3K9me3-H4K20me3"]

def process_line(line, count, match, rows):
    # /uod/idr/filesets/idr0082-pennycuick-lesions/20200417-ftp/S1_HandE.ndpi.ndpa
    # /uod/idr/filesets/idr0082-pennycuick-lesions/20200417-ftp/S2_HandE.ndpi.ndpa
    parts = line.split('/')
    length = len(parts)
#    print(parts[length-1])
    parts_of_im_names = parts[length-1].split('_')
    for dataset_name in dataset_names:
        dataset_name_parts = dataset_name.split('_')
        if (dataset_name_parts[0] in line):
            if(dataset_name_parts[1] in line):
                match = 1
                print (dataset_name)
                rows.append(['Dataset:name:'+dataset_name, line])
            if ((dataset_name_parts[1] == "Scc1") & (match == 0)):
                if (dataset_name_parts[1].lower() in line.lower()):
                    match = 1
                    print (dataset_name)
                    rows.append(['Dataset:name:'+dataset_name, line])
    return match, dataset_name

def write_tsv(rows):
    with open('experimentC/idr0086-experimentC-filePaths.tsv', mode='w') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t')
        tsv_writer.writerows(rows)

with open(attachment_file) as fp:
    line = fp.readline().strip()
    count = 0
    while line and len(line) > 0:
        count += 1

        print("Line %d" % count)
        print (line)
        (match,dataset_name) = process_line(line, count, 0, rows)
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
write_tsv(rows)

