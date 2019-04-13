#!/usr/bin/python

#--------- RULE MANAGER SCRIPT -----------#
# purpose: to continuously fetch snort rules, merge changes
#          script should be automatically ran every hour

# see https://github.com/jasonish/py-idstools/blob/master/idstools/scripts/rulecat.py
import hashlib 
import io
import tarfile
import wget
import os

def download_checksum(url, tmp_path):
    filename = wget.download(url, out = tmp_path, bar = None)
    with open(filename, 'r') as f:
	md5hash = f.read()
    return md5hash

def extract_tar(name,file_path):
    tar = tarfile.open(name)
    tar.extractall(path = file_path)
    tar.close()
    return 1    

def filemd5(filename, block_size=2**20):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
	for chunk in iter(lambda: f.read(4096), b''):
	    md5.update(chunk)
    return md5.hexdigest()

def fetch(url, path):
    print "Fetching %s." % (url)
    checksum_url = url + '.md5'

    tmp_dir = '/var/tmp/'

    if (os.path.exists(path + '/community-rules')):
	checksum = download_checksum(checksum_url, tmp_dir)

    	if (checksum == filemd5(path + '/community-rules.tar.gz')):
	    print "Checksums have not changed. No update, not downloading."
            return 0
	    
    # replace file here
    filename = wget.download(url, out = path)

    extract_tar(filename, path)
  
    return 1

def main():
    rule_path = '/etc/snort/rules'

    rule_url = 'https://www.snort.org/downloads/community/community-rules.tar.gz'

    if (fetch(rule_url, rule_path) == 1):
        print " Snort com rules update complete to %s" % (rule_path)
    

if __name__ == "__main__":
    main()
