import os
import sys
import re
import subprocess

def main():
    """
    This script takes in a text file that may or may not include CVE-IDs and outputs every CVE that is found in the Metasploit database of exploits in a text file. 
    Note: Multiple CVE-IDs on the same line are detected and queried individually, but the output will be separated by a space on the same line
            If there are no CVE-IDs found in a line (from the input text file), the output will include a "\n" (blank line) corresponding to the same line numbers.  
    """
    in_filename = "cve_list.txt"
    exec_filename = "run.sh"
    msf_filename = "msf_output.txt" 
    out_filename = "results.txt"
    root = os.path.dirname(os.path.abspath(__file__))
    
    print("Reading CVEs from: " + root + "/" + in_filename)
    print("Building script to: " + root + "/" + exec_filename)

    # The following files are used:  
    # r = reads CVE_LIST, has entries like 2020-1234 or CVE-2020-1234
    # w = writes intermediate script, run.sh
    # f = reads msfconsole's output for additional parsing
    # o = writes all parsing matches to output file 
    
    with open(root + os.path.sep + in_filename, "r") as r,  \
            open(root + os.path.sep + exec_filename, "w") as w:
     
        w.write("#!/bin/bash\n")
        w.write("msfconsole -o " + "'" + msf_filename + "'" + " -q -x ")
        w.write("'\n")
        
        count = 1 
        for line in r:
            # tries to match any part of the line that has a YYYY-NNNNNNNN CVE-like entry 
            # match = re.search(r'(19|20)\d{2}-\d{4,}', line)
            for match in re.finditer(r'(19|20)\d{2}-\d{4,}', line):
                w.write("echo " + str(count) + "_CVE-" + match.group() + ";")
                w.write("search cve:" + match.group() + ";")
            count += 1
        w.write("exit'")
        print("Setting " + exec_filename + " permissions to 755")
        os.chmod(root + os.path.sep + exec_filename, 0o755)
        print("Done building script!")
        
    print("Running script " + exec_filename + ", saving results to: " + msf_filename + "...")
    subprocess.run([root + "/" + exec_filename])
   
    print("Parsing " + msf_filename + " for matches, saving results to: " + out_filename) 
    with open(root + os.path.sep + msf_filename, "r") as f, \
            open(root + os.path.sep + out_filename, "w") as o:
        matches_ok = True
        current_cve = None
        current_line = None 
        count = 1 
        for line in f: 
            if not matches_ok and line.strip(): 
                if line.startswith("[-] No results"): 
                    matches_ok = True # matching result found, but no hit in database
                else: 
                    matches_ok = True # matching result found, hit in database
                    
                    # write out match, newlines if count not up to date
                    while count != current_line: 
                        o.write("\n")
                        count += 1
                    o.write("CVE-" + current_cve + " ")
            elif line.startswith("[*] exec: echo"):
                matches_ok = False # start looking for a matching result line
                line_arr = (re.search(r'\d{1,}_CVE-(19|20)\d{2}-\d{4,}', line)).group()
                line_arr = line_arr.split("_CVE-")
                # parse the target line/group number from the echo line
                current_line = int(line_arr[0])
                # parse the target cve 
                current_cve = line_arr[1]
    print("Done!")


if __name__ == "__main__":
    main()
