dword-extractor
===============

This python script will extract the dword from the ELF file

Installation
------------
     Copy all the files to a local folder
     -commands.py
     -vault.o


Minimum requirements
--------------------
    --kali linux or r2 installed
    --You need to have r2 already installed in your linux machine


Explanation
-----------
    --commands.py - This file will execute r2 with a crafted commmand to extract the dwords
    --file.o -  This is an ELF file that will be parsed
    --r2 - RADARE2 should be already installed in your Linux command line machine

Example usage and output
------------------------

    $python commands.py vault.o