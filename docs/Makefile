
all: imagelayout.py.1 imagelayout.py.html

configfile.md: configoptions-dynalist.txt dynalist2md.py
	./dynalist2md.py $< > $@

manu.md: manu1.md configfile.md manu2.md
	cat $^ > $@

imagelayout.py.1: manu.md metadata.yaml
	pandoc -s -f gfm -t man --metadata-file metadata.yaml $< -o $@

imagelayout.py.html: manu.md metadata.yaml
	pandoc -s -f gfm -t html --metadata-file metadata.yaml $< -o $@
