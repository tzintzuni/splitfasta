# splitfasta
Just a simple multi-sequence FASTA file splitter.

Splits a multi-sequence FASTA file into chunks. You can specify the number of chunks or the maximum number of sequences per chunk. It does not split individual sequences and is not meant to split a large sequence into smaller ones.

**Usage:**

```
python3 split_fasta.py --chunks N <FASTA>
python3 split_fasta.py --sequences N <FASTA>
```

Output is in the same location as the input <FASTA> file with .partN appended to the filenames

Concatenating the '.part' files in order will reconstruct the original file.
