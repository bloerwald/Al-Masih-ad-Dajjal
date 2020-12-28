#!/usr/bin/env python3

import argparse
import gc
import io
import os
import sys
import zlib

for mod in ['uncompyle6', 'spark', 'xdis']:
    sys.path.insert(
        0,
        os.path.dirname(
            os.path.abspath(__file__)) +
        '/python-' +
        mod)

import xdis
import uncompyle6

def find_xor_and_decrypt(blob):
    blob = bytearray(blob)
    for key_len in range(0, len(blob)):
        blob[key_len] = int(blob[key_len]) ^ 0x9a
        try:
            return zlib.decompress(bytes(blob))
        except Exception as ex:
            pass
    raise Exception(
        'unable to decompress: no key len decompressed without error')


def write_to_file(blob, filename, mode=''):
    if not os.path.isdir(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'w' + mode) as output:
        output.write(blob)


seen_files = dict()


def decompress(input, output_prefix):
    gc.collect()
    unpacked_data = find_xor_and_decrypt(
        open(os.path.join(input), 'rb').read())

    (version, _, _, code, _, _, _) = xdis.load.load_module_from_file_object(
        io.BytesIO(unpacked_data))

    if version != 2.7:
        raise Exception(
            'unexpected module version {} (not 2.7)'.format(version))

    filename = code.co_filename
    output_filename = os.path.join(output_prefix, filename)

    # todo: unable to decompile: parsing is inefficient for 80k element lists of
    # 3-tuples
    if filename == 'entities/client/data/waypoint_data.py':
        return

    write_to_file(unpacked_data, output_filename + 'c', 'b')

    global seen_files
    if not filename in seen_files:
        seen_files[filename] = input
    else:
        raise Exception(
            '{} exists twice?! {} vs {}' %
            (filename, input, seen_files[filename]))

    if os.path.exists(output_filename):
        return
    print('----', output_filename)

    output = io.StringIO()
    try:
        uncompyle6.main.decompile(version, code, output)

        write_to_file(output.getvalue(), output_filename)
    except Exception as e:
        raise Exception(
            'failed to process {}: {}'.format(
                filename, e))


def main():
    # entities/common/UiTipsConst.py has waaaaay too deep AST which fails
    # assembling due to using recursion.
    sys.setrecursionlimit(10000)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--source-dir',
        dest="source_dir",
        type=str,
        required=True,
        help="location of 'encrypted' files")
    parser.add_argument(
        '--output-dir',
        dest="output_dir",
        type=str,
        required=True,
        help="directory to decrypted files to")
    args = parser.parse_args()

    for root, _, dir_files in os.walk(args.source_dir):
        for df in dir_files:
            try:
                decompress(os.path.join(root, df),
                           args.output_dir)
            except Exception as e:
                print('failed to process file {}: {}'.format(df, e))


main()
