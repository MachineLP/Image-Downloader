
import os 

f = open("./data/category.txt")
lines = f.readlines()
key_word = ""
for line in lines:
    per_line = line.strip().split('    ')
    if per_line[1] != "null":
        key_word = per_line[2]
    
    print ("key_word>>>>>>>>", key_word)
    dst_dir = "./download_images/{}".format(key_word)
    if not os.path.exists(dst_dir):
        if key_word != "":
            os.system( " python image_downloader.py '{}' --max-number 2000 ".format( key_word + ' ads' ) )

f.close()