# splitfasta
Just a simple multi-sequence FASTA file splitter.

Splits a multi-sequence FASTA file into chunks. You can specify the number of chunks or the maximum number of sequences per chunk. It does not split individual sequences and is not meant to split a large sequence into smaller ones.

**Usage:**

```
python3 split_fasta.py --chunks N [--prefix /output/path] <FASTA>
python3 split_fasta.py --sequences N [--prefix /output/path] <FASTA>
```

Output is in the same location as the input <FASTA> file unless specified with [--prefix|-p] option. Output files will retain the same original filename with a suffix of `.partN` appended to the filenames where `N` is the non-padded serial chunk number.

Concatenating the '.part' files in order of `N` will reconstruct the original file.
