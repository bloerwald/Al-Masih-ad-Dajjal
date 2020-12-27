# (C) Copyright 2017, 2019-2020 by Rocky Bernstein
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
"""
CPython 2.7 bytecode opcodes

This is a like Python 2.7's opcode.py with some classification
of stack usage.
"""

from xdis.opcodes.base import (
    compare_op,
    const_op,
    def_op,
    extended_format_ATTR,
    extended_format_CALL_FUNCTION,
    extended_format_MAKE_FUNCTION_older,
    extended_format_RAISE_VARARGS_older,
    extended_format_RETURN_VALUE,
    finalize_opcodes,
    format_CALL_FUNCTION_pos_name_encoded,
    format_extended_arg,
    format_MAKE_FUNCTION_default_argc,
    format_RAISE_VARARGS_older,
    free_op,
    init_opdata,
    jabs_op,
    jrel_op,
    local_op,
    name_op,
    nargs_op,
    store_op,
    update_pj3,
    varargs_op,
)

import xdis.opcodes.opcode_2x as opcode_2x

version = 2.7
python_implementation = "CPython"

l = locals()
init_opdata(l, opcode_2x, version)

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

# If the POP field is -1 and the opcode is var args operation
# (hasvargs | hasnargs) operation, then
# the operand holds the size.

#          OP NAME            OPCODE POP PUSH
#--------------------------------------------
def_op(l, "STOP_CODE",                0,  0,  0, fallthrough=False)
def_op(l, "POP_TOP",                  1,  1,  0)
def_op(l, "ROT_TWO",                  2,  2,  2)
def_op(l, "ROT_THREE",                3,  3,  3)
def_op(l, "DUP_TOP",                  4,  0,  1)
def_op(l, "ROT_FOUR",                 5,  4,  4)

def_op(l, 'NOP',                      9,  0,  0)
def_op(l, "UNARY_POSITIVE",          10,  1,  1)
def_op(l, "UNARY_NEGATIVE",          11,  1,  1)
def_op(l, "UNARY_NOT",               12,  1,  1)
def_op(l, "UNARY_CONVERT",           13,  1,  1)

def_op(l, "UNARY_INVERT",            15,  1,  1)

def_op(l, "BINARY_POWER",            19,  2,  1)
def_op(l, "BINARY_MULTIPLY",         20,  2,  1)
def_op(l, "BINARY_DIVIDE",           21,  2,  1)
def_op(l, "BINARY_MODULO",           22,  2,  1)
def_op(l, "BINARY_ADD",              23,  2,  1)
def_op(l, "BINARY_SUBTRACT",         24,  2,  1)
def_op(l, "BINARY_SUBSCR",           25,  2,  1)
def_op(l, "BINARY_FLOOR_DIVIDE",     26,  2,  1)
def_op(l, "BINARY_TRUE_DIVIDE",      27,  2,  1)
def_op(l, "INPLACE_FLOOR_DIVIDE",    28,  2,  1)
def_op(l, "INPLACE_TRUE_DIVIDE",     29,  2,  1)

def_op(l, "SLICE+0",                 30,  2,  2)
def_op(l, "SLICE+1",                 31,  2,  2)
def_op(l, "SLICE+2",                 32,  2,  2)
def_op(l, "SLICE+3",                 33,  3,  2)

store_op(l, "STORE_SLICE+0",         40,  2,  0)
store_op(l, "STORE_SLICE+1",         41,  3,  0)
store_op(l, "STORE_SLICE+2",         42,  3,  0)
store_op(l, "STORE_SLICE+3",         43,  4,  0)

def_op(l, "DELETE_SLICE+0",          50,  1,  0)
def_op(l, "DELETE_SLICE+1",          51,  2,  0)
def_op(l, "DELETE_SLICE+2",          52,  2,  0)
def_op(l, "DELETE_SLICE+3",          53,  3,  0)

store_op(l, "STORE_MAP",             54,  3,  1)
def_op(l, "INPLACE_ADD",             55,  2,  1)
def_op(l, "INPLACE_SUBTRACT",        56,  2,  1)
def_op(l, "INPLACE_MULTIPLY",        57,  2,  1)
def_op(l, "INPLACE_DIVIDE",          58,  2,  1)
def_op(l, "INPLACE_MODULO",          59,  2,  1)
store_op(l, "STORE_SUBSCR",          60,  3,  0) # Implements TOS1[TOS] = TOS2.
def_op(l, "DELETE_SUBSCR",           61,  2,  0) # Implements del TOS1[TOS].
def_op(l, "BINARY_LSHIFT",           62,  2,  1)
def_op(l, "BINARY_RSHIFT",           63,  2,  1)
def_op(l, "BINARY_AND",              64,  2,  1)
def_op(l, "BINARY_XOR",              65,  2,  1)
def_op(l, "BINARY_OR",               66,  2,  1)
def_op(l, "INPLACE_POWER",           67,  2,  1)
def_op(l, "GET_ITER",                68,  1,  1)

def_op(l, "PRINT_EXPR",              70,  1,  0)
def_op(l, "PRINT_ITEM",              71,  1,  0)
def_op(l, "PRINT_NEWLINE",           72,  0,  0)
def_op(l, "PRINT_ITEM_TO",           73,  2,  0)
def_op(l, "PRINT_NEWLINE_TO",        74,  1,  0)
def_op(l, "INPLACE_LSHIFT",          75,  2,  1)
def_op(l, "INPLACE_RSHIFT",          76,  2,  1)
def_op(l, "INPLACE_AND",             77,  2,  1)
def_op(l, "INPLACE_XOR",             78,  2,  1)
def_op(l, "INPLACE_OR",              79,  2,  1)
def_op(l, "BREAK_LOOP",              80,  0,  0, fallthrough=False)
def_op(l, 'WITH_CLEANUP',            81,  4,  3)
def_op(l, "LOAD_LOCALS",             82,  0,  1)
def_op(l, "RETURN_VALUE",            83,  1,  0, fallthrough=False)
def_op(l, "IMPORT_STAR",             84,  1,  0)
def_op(l, "EXEC_STMT",               85,  3,  0)
def_op(l, "YIELD_VALUE",             86,  1,  1)
def_op(l, "POP_BLOCK",               87,  0,  0)
def_op(l, "END_FINALLY",             88,  3,  0)
def_op(l, "BUILD_CLASS",             89,  2,  0)

HAVE_ARGUMENT = 90              # Opcodes from here have an argument:

store_op(l, "STORE_NAME",            90,  1,  0, is_type="name")  # Operand is in name list
name_op(l, "DELETE_NAME",            91,  0,  0)  # ""
varargs_op(l, "UNPACK_SEQUENCE",     92, -1,  1)  # TOS is number of tuple items
jrel_op(l, "FOR_ITER",               93,  0,  1)  # TOS is read
def_op(l, "LIST_APPEND",             94,  2,  1)  # Calls list.append(TOS[-i], TOS).

store_op(l, "STORE_ATTR",            95,  2,  0, is_type="name")  # Operand is in name list
name_op(l, "DELETE_ATTR",            96,  1,  0)  # ""
store_op(l, "STORE_GLOBAL",          97,  1,  0, is_type="name")  # ""
name_op(l, "DELETE_GLOBAL",          98,  0,  0)  # ""
nargs_op(l, "DUP_TOPX",              99, -1,  2)  # number of items to duplicate
const_op(l, "LOAD_CONST",           100,  0,  1)  # Operand is in const list

name_op(l, "LOAD_NAME",             101,  0,  1)  # Operand is in name list
varargs_op(l, "BUILD_TUPLE",        102, -1,  1)  # TOS is number of tuple items
varargs_op(l, "BUILD_LIST",         103, -1,  1)  # TOS is number of list items
varargs_op(l, 'BUILD_SET',          104, -1,  1)  # TOS is count of set items
def_op(l, "BUILD_MAP",              105,  0,  1)  # count is in argument
name_op(l, "LOAD_ATTR",             106,  1,  1)  # Operand is in name list
compare_op(l, "COMPARE_OP",         107)

name_op(l, "IMPORT_NAME",           108,  2,  1)  # Index in name list
name_op(l, "IMPORT_FROM",           109,  0,  1)
jrel_op(l, "JUMP_FORWARD",          110,  0,  0, fallthrough=False) # Number of bytes to skip
jabs_op(l, "JUMP_IF_FALSE_OR_POP",  111)  # Target byte offset from beginning of code
jabs_op(l, "JUMP_IF_TRUE_OR_POP",   112)  # ""
jabs_op(l, "JUMP_ABSOLUTE",         113,  0,  0, fallthrough=False) # Target byte offset from beginning of code
jabs_op(l, "POP_JUMP_IF_FALSE",     114,  2,  1, conditional=True)  # ""
jabs_op(l, "POP_JUMP_IF_TRUE",      115,  2,  1, conditional=True)  # ""

name_op(l, "LOAD_GLOBAL",           116,  0,  1)  # Operand is in name list

jabs_op(l, "CONTINUE_LOOP",         119,  0,  0, fallthrough=False)  # Target address
jrel_op(l, "SETUP_LOOP",            120,  0,  0, conditional=True)  # Distance to target address
jrel_op(l, "SETUP_EXCEPT",          121,  0,  0, conditional=True)  # ""
jrel_op(l, "SETUP_FINALLY",         122,  0,  0, conditional=True)  # ""

local_op(l, "LOAD_FAST",            124,  0,  1) # Local variable number

store_op(l, "STORE_FAST",           125,  1,  0, is_type="local")  # Local variable number

local_op(l, "DELETE_FAST",          126,  0,  0) # Local variable number is in operand


nargs_op(l, "RAISE_VARARGS",        130, -1,  2, fallthrough=False) # Number of raise arguments (1, 2, or 3)
nargs_op(l, "CALL_FUNCTION",        131, -1,  2) # TOS is #args + (#kwargs << 8)
nargs_op(l, "MAKE_FUNCTION",        132, -1,  2) # TOS is number of args with default values
varargs_op(l, "BUILD_SLICE",        133,  2,  1) # TOS is number of items
def_op(l, "MAKE_CLOSURE",           134, -3,  1)
free_op(l, "LOAD_CLOSURE",          135,  0,  1)

free_op(l, "LOAD_DEREF",            136,  0,  1)

store_op(l, "STORE_DEREF",          137,  1,  0, is_type="free")


nargs_op(l, "CALL_FUNCTION_VAR",    140, -2,  1)  # #args + (#kwargs << 8)
nargs_op(l, "CALL_FUNCTION_KW",     141, -2,  1)  # #args + (#kwargs << 8)
nargs_op(l, "CALL_FUNCTION_VAR_KW", 142, -3,  1)  # #args + (#kwargs << 8)

jrel_op(l, "SETUP_WITH",            143,  0,  4)

def_op(l, "EXTENDED_ARG",           145)

def_op(l, "SET_ADD",                146,  1,  0)  # Calls set.add(TOS1[-i], TOS).
def_op(l, "MAP_ADD",                147,  3,  1)  # Calls dict.setitem(TOS1[-i], TOS, TOS1)


update_pj3(globals(), l)

opcode_arg_fmt = {
    "MAKE_FUNCTION": format_MAKE_FUNCTION_default_argc,
    "EXTENDED_ARG": format_extended_arg,
    "CALL_FUNCTION": format_CALL_FUNCTION_pos_name_encoded,
    "RAISE_VARARGS": format_RAISE_VARARGS_older,
}

finalize_opcodes(l)

opcode_extended_fmt = {
    "CALL_FUNCTION": extended_format_CALL_FUNCTION,
    "LOAD_ATTR": extended_format_ATTR,
    "MAKE_FUNCTION": extended_format_MAKE_FUNCTION_older,
    "RAISE_VARARGS": extended_format_RAISE_VARARGS_older,
    "RETURN_VALUE": extended_format_RETURN_VALUE,
    "STORE_ATTR": extended_format_ATTR,
}
