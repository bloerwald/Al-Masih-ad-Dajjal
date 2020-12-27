# (C) Copyright 2018, 2020 by Rocky Bernstein
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""CPython core set of bytecode opcodes based on version 2.3

This is used in bytecode disassembly among other things. This is
similar to the opcodes in Python's opcode.py library.

If this file changes the other opcode files may have to be adjusted accordingly.
"""

l = locals()

# FIXME: DRY this with opcode_3x.

hascompare   = []
hascondition = [] # conditional operator; has jump offset
hasconst     = []
hasfree      = []
hasjabs      = []
hasjrel      = []
haslocal     = []
hasname      = []
hasnargs     = []  # For function-like calls
hasstore     = []  # Some sort of store operation
hasvargs     = []  # Similar but for operators BUILD_xxx
nofollow     = []  # Instruction doesn't fall to the next opcode

# opmap[opcode_name] => opcode_number
opmap = {}

# opcode[i] => opcode name
opname = [''] * 256

# oppush[op] => number of stack entries pushed
oppush = [0] * 256

# oppop[op] => number of stack entries popped
# 9 means handle special. Note his forces oppush[i] - oppop[i] negative
oppop  = [0] * 256

for op in range(256): opname[op] = '<%r>' % (op,)
del op
