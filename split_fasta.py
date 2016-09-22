import math
from argparse import ArgumentParser


def index_sequences(filename):
    sequence_index = []
    with open(filename) as f:
        pos = f.tell()
        line = f.readline()
        while len(line) > 0:
            if line.startswith('>'):
                sequence_index.append(pos)
            pos = f.tell()
            line = f.readline()
        # add position of end of file
        sequence_index.append(pos)
    return sequence_index


def write_chunk(sourcefile, offset, length, destination):
    with open(sourcefile) as sf:
        sf.seek(offset)
        chunk = sf.read(length)
        with open(destination, 'w') as dest:
            dest.write(chunk)


def get_chunk_end(index, offset, chunk_size):
    if offset + chunk_size < len(index):
        return index[offset + chunk_size]
    else:
        return index[-1]


def iter_n_chunks(index, N):
    chunk_size = math.ceil(len(index) / N)
    offset = 0
    while offset < len(index):
        chunk_end = get_chunk_end(index, offset, chunk_size)
        chunk_length = chunk_end - index[offset]
        yield (index[offset], chunk_length)
        offset += chunk_size


def iter_size_chunks(index, seqs):
    chunk_size = seqs
    offset = 0
    while offset < len(index):
        chunk_end = get_chunk_end(index, offset, chunk_size)
        chunk_length = chunk_end - index[offset]
        yield (index[offset], chunk_length)
        offset += chunk_size


def isset(x):
    return x is not None

if __name__ == "__main__":
    parser = ArgumentParser(description="Split Multi-FASTA file into smaller files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--chunks', '-c', type=int, default=None)
    group.add_argument('--sequences', '-s', type=int, default=None)
    parser.add_argument('--prefix', '-p', type=str, default=None)
    parser.add_argument('fasta')
    args = parser.parse_args()

    index = index_sequences(args.fasta)
    fileparts = args.fasta.rsplit('/', 1)
    if len(fileparts) > 1:
        (path, fasta) = fileparts
    else:
        fasta = fileparts[0]
        path = './'

    if args.prefix is not None:
        outfile = '{}/{}'.format(args.prefix, fasta)
    else:
        outfile = '{}/{}'.format(path, fasta)

    if isset(args.chunks):
        part = 0
        for (offset, length) in iter_n_chunks(index, args.chunks):
            part += 1
            chunkfile = '{}.part{}'.format(outfile, part)
            write_chunk(args.fasta, offset, length, chunkfile)

    if isset(args.sequences):
        part = 0
        for (offset, length) in iter_size_chunks(index, args.sequences):
            part += 1
            chunkfile = '{}.part{}'.format(outfile, part)
            write_chunk(args.fasta, offset, length, chunkfile)
