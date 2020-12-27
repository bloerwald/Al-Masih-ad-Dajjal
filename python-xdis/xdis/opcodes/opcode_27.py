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
def_op(l, "STOP_CODE",              255,  0,  0, fallthrough=False) # todo
def_op(l, "POP_TOP",                 68,  1,  0) # GET_ITER
def_op(l, "ROT_TWO",                 58,  2,  2) # INPLACE_DIVIDE
def_op(l, "ROT_THREE",               62,  3,  3) # BINARY_LSHIFT
def_op(l, "DUP_TOP",                 84,  0,  1) # IMPORT_STAR
def_op(l, "ROT_FOUR",               254,  4,  4) # todo

def_op(l, 'NOP',                      9,  0,  0) #                   unverified
def_op(l, "UNARY_POSITIVE",          10,  1,  1)
def_op(l, "UNARY_NEGATIVE",          11,  1,  1)
def_op(l, "UNARY_NOT",               12,  1,  1)
def_op(l, "UNARY_CONVERT",           13,  1,  1)

def_op(l, "UNARY_INVERT",            15,  1,  1)

def_op(l, "BINARY_POWER",            19,  2,  1)
def_op(l, "BINARY_MULTIPLY",         80,  2,  1) # BREAK_LOOP
def_op(l, "BINARY_DIVIDE",           22,  2,  1) # BINARY_MODULO
def_op(l, "BINARY_MODULO",           83,  2,  1) # RETURN_VALUE
def_op(l, "BINARY_ADD",              89,  2,  1) # BUILD_CLASS
def_op(l, "BINARY_SUBTRACT",          1,  2,  1) # POP_TOP
def_op(l, "BINARY_SUBSCR",           24,  2,  1) # BINARY_SUBTRACT, guess, 25??????
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

store_op(l, "STORE_MAP",             78,  3,  1) # INPLACE_XOR
def_op(l, "INPLACE_ADD",              2,  2,  1) # ROT_TWO
def_op(l, "INPLACE_SUBTRACT",        20,  2,  1) # BINARY_MULTIPLY
def_op(l, "INPLACE_MULTIPLY",        60,  2,  1) # STORE_SUBSCR
def_op(l, "INPLACE_DIVIDE",          23,  2,  1) # BINARY_ADD
def_op(l, "INPLACE_MODULO",          63,  2,  1) # BINARY_RSHIFT
store_op(l, "STORE_SUBSCR",           3,  3,  0) # ROT_THREE,       guess -- Implements TOS1[TOS] = TOS2.
def_op(l, "DELETE_SUBSCR",           75,  2,  0) # INPLACE_LSHIFT,  guess -- Implements del TOS1[TOS].
def_op(l, "BINARY_LSHIFT",           61,  2,  1) # DELETE_SUBSCR
def_op(l, "BINARY_RSHIFT",            0,  2,  1) # STOP_CODE
def_op(l, "BINARY_AND",              57,  2,  1) # INPLACE_MULTIPLY
def_op(l, "BINARY_XOR",              65,  2,  1)
def_op(l, "BINARY_OR",               55,  2,  1) # INPLACE_ADD
def_op(l, "INPLACE_POWER",           64,  2,  1) # BINARY_AND
def_op(l, "GET_ITER",                59,  1,  1) # INPLACE_MODULO

def_op(l, "PRINT_EXPR",              70,  1,  0)
def_op(l, "PRINT_ITEM",              71,  1,  0)
def_op(l, "PRINT_NEWLINE",           72,  0,  0)
def_op(l, "PRINT_ITEM_TO",           73,  2,  0)
def_op(l, "PRINT_NEWLINE_TO",        74,  1,  0)
def_op(l, "INPLACE_LSHIFT",          85,  2,  1) # EXEC_STMT
def_op(l, "INPLACE_RSHIFT",          66,  2,  1) # BINARY_OR
def_op(l, "INPLACE_AND",             86,  2,  1) # YIELD_VALUE
def_op(l, "INPLACE_XOR",             21,  2,  1) # BINARY_DIVIDE
def_op(l, "INPLACE_OR",               4,  2,  1) # DUP_TOP
def_op(l, "BREAK_LOOP",               5,  0,  0, fallthrough=False) # ROT_FOUR
def_op(l, 'WITH_CLEANUP',            81,  4,  3)
def_op(l, "LOAD_LOCALS",             76,  0,  1) # INPLACE_RSHIFT
def_op(l, "RETURN_VALUE",            88,  1,  0, fallthrough=False) # END_FINALLY
def_op(l, "IMPORT_STAR",             54,  1,  0) # STORE_MAP
def_op(l, "EXEC_STMT",               67,  3,  0) # INPLACE_POWER
def_op(l, "YIELD_VALUE",             79,  1,  1) # INPLACE_OR
def_op(l, "POP_BLOCK",               82,  0,  0) # LOAD_LOCALS
def_op(l, "END_FINALLY",             87,  3,  0) # POP_BLOCK
def_op(l, "BUILD_CLASS",             77,  2,  0) # INPLACE_AND

HAVE_ARGUMENT = 90              # Opcodes from here have an argument:

store_op(l, "STORE_NAME",           135,  1,  0, is_type="name")  # LOAD_CLOSURE -- Operand is in name list
name_op(l, "DELETE_NAME",           120,  0,  0)  # SETUP_LOOP -- ""
varargs_op(l, "UNPACK_SEQUENCE",     92, -1,  1)  # TOS is number of tuple items
jrel_op(l, "FOR_ITER",              121,  0,  1)  # SETUP_EXCEPT -- TOS is read
def_op(l, "LIST_APPEND",            124,  2,  1)  # from thin air          guess -- Calls list.append(TOS[-i], TOS).

store_op(l, "STORE_ATTR",           126,  2,  0, is_type="name")  # DELETE_FAST -- Operand is in name list
name_op(l, "DELETE_ATTR",           107,  1,  0)  # COMPARE_OP -- ""
store_op(l, "STORE_GLOBAL",         106,  1,  0, is_type="name")  # LOAD_ATTR -- ""
name_op(l, "DELETE_GLOBAL",          96,  0,  0)  # DELETE_ATTR -- ""
nargs_op(l, "DUP_TOPX",             115, -1,  2)  # POP_JUMP_IF_TRUE,     guess -- number of items to duplicate
const_op(l, "LOAD_CONST",           100,  0,  1)  # Operand is in const list

name_op(l, "LOAD_NAME",             101,  0,  1)  # Operand is in name list
varargs_op(l, "BUILD_TUPLE",        102, -1,  1)  # TOS is number of tuple items
varargs_op(l, "BUILD_LIST",          99, -1,  1)  # DUP_TOPX -- TOS is number of list items
varargs_op(l, 'BUILD_SET',          134, -1,  1)  # MAKE_CLOSURE -- TOS is count of set items
def_op(l, "BUILD_MAP",               93,  0,  1)  # FOR_ITER -- count is in argument
name_op(l, "LOAD_ATTR",             114,  1,  1)  # POP_JUMP_IF_FALSE -- Operand is in name list
compare_op(l, "COMPARE_OP",         146) # SET_ADD

name_op(l, "IMPORT_NAME",           108,  2,  1)  # Index in name list
name_op(l, "IMPORT_FROM",           109,  0,  1)
jrel_op(l, "JUMP_FORWARD",          110,  0,  0, fallthrough=False) # Number of bytes to skip
jabs_op(l, "JUMP_IF_FALSE_OR_POP",  111)  # Target byte offset from beginning of code
jabs_op(l, "JUMP_IF_TRUE_OR_POP",   112)  # ""
jabs_op(l, "JUMP_ABSOLUTE",         113,  0,  0, fallthrough=False) # Target byte offset from beginning of code
jabs_op(l, "POP_JUMP_IF_FALSE",      94,  2,  1, conditional=True)  # LIST_APPEND -- ""
jabs_op(l, "POP_JUMP_IF_TRUE",      104,  2,  1, conditional=True)  # BUILD_SET -- ""

name_op(l, "LOAD_GLOBAL",           116,  0,  1)  # Operand is in name list

jabs_op(l, "CONTINUE_LOOP",          90,  0,  0, fallthrough=False)  # STORE_NAME -- Target address
jrel_op(l, "SETUP_LOOP",            105,  0,  0, conditional=True)  # BUILD_MAP -- Distance to target address
jrel_op(l, "SETUP_EXCEPT",          137,  0,  0, conditional=True)  # STORE_DEREF -- ""
jrel_op(l, "SETUP_FINALLY",         147,  0,  0, conditional=True)  # MAP_ADD -- ""

local_op(l, "LOAD_FAST",             95,  0,  1) # STORE_ATTR,           not reused (124) -- Local variable number

store_op(l, "STORE_FAST",           103,  1,  0, is_type="local")  # BUILD_LIST -- Local variable number

local_op(l, "DELETE_FAST",           97,  0,  0) # STORE_GLOBAL -- Local variable number is in operand


nargs_op(l, "RAISE_VARARGS",        130, -1,  2, fallthrough=False) # Number of raise arguments (1, 2, or 3)
nargs_op(l, "CALL_FUNCTION",        131, -1,  2) # TOS is #args + (#kwargs << 8)
nargs_op(l, "MAKE_FUNCTION",        132, -1,  2) # TOS is number of args with default values
varargs_op(l, "BUILD_SLICE",        133,  2,  1) # unverified -- TOS is number of items
def_op(l, "MAKE_CLOSURE",           119, -3,  1) # CONTINUE_LOOP
free_op(l, "LOAD_CLOSURE",           91,  0,  1) # DELETE_NAME

free_op(l, "LOAD_DEREF",            125,  0,  1) # STORE_FAST

store_op(l, "STORE_DEREF",          136,  1,  0, is_type="free") # LOAD_DEREF


nargs_op(l, "CALL_FUNCTION_VAR",    140, -2,  1)  # #args + (#kwargs << 8)
nargs_op(l, "CALL_FUNCTION_KW",     141, -2,  1)  # #args + (#kwargs << 8)
nargs_op(l, "CALL_FUNCTION_VAR_KW", 142, -3,  1)  # #args + (#kwargs << 8)

jrel_op(l, "SETUP_WITH",            143,  0,  4)

def_op(l, "EXTENDED_ARG",           145) # unverified

def_op(l, "SET_ADD",                 98,  1,  0)  # DELETE_GLOBAL,        guess -- Calls set.add(TOS1[-i], TOS).
def_op(l, "MAP_ADD",                122,  3,  1)  # SETUP_FINALLY,        guess -- Calls dict.setitem(TOS1[-i], TOS, TOS1)

const_op(l, "LOAD_FAST_ZERO_LOAD_CONST",         173,  0,  1)  # from thin air,         custom -- Operand is in const list


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
