
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '8596D899C68E3D18E6C91874D0C1D990'
    
_lr_action_items = {'DEDENT':([5,17,18,21,23,31,],[-3,-2,-4,-6,-5,32,]),'ASS_EQ':([1,],[13,]),'INDENT':([29,],[30,]),'NAME':([0,2,4,5,6,7,10,12,21,22,23,24,25,30,],[1,-11,15,1,-10,1,22,-12,-6,-15,-5,-13,-14,1,]),'INT':([13,14,26,],[24,25,28,]),'NEWLINE':([2,6,7,8,11,12,19,20,22,24,25,27,32,],[-11,-10,-8,21,23,-12,-7,-9,-15,-13,-14,29,-16,]),'LT':([15,],[26,]),'WHILE':([0,5,21,23,30,],[4,4,-6,-5,4,]),'COLON':([16,28,],[27,-17,]),'AUG_ASSIGN_PLUS':([1,],[14,]),'PRINT':([0,2,5,6,7,12,21,22,23,24,25,30,],[10,-11,10,-10,10,-12,-6,-15,-5,-13,-14,10,]),'$end':([3,5,9,17,18,21,23,],[-1,-3,0,-2,-4,-6,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assign_ext':([1,],[12,]),'stmt_ext':([5,],[17,]),'small_stmt':([0,5,7,30,],[7,7,7,7,]),'stmt':([0,5,30,],[5,5,5,]),'assign_stmt':([0,5,7,30,],[6,6,6,6,]),'small_ext':([7,],[19,]),'print_stmt':([0,5,7,30,],[2,2,2,2,]),'while_stmt':([0,5,30,],[8,8,8,]),'module':([0,],[9,]),'cmp_expr':([4,],[16,]),'stmts':([0,5,30,],[3,18,31,]),'small_stmts':([0,5,7,30,],[11,11,20,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> stmts','module',1,'p_module','hw5.py',152),
  ('stmts -> stmt stmt_ext','stmts',2,'p_stmts','hw5.py',158),
  ('stmt_ext -> <empty>','stmt_ext',0,'p_stmt_ext','hw5.py',164),
  ('stmt_ext -> stmts','stmt_ext',1,'p_stmt_ext','hw5.py',165),
  ('stmt -> small_stmts NEWLINE','stmt',2,'p_stmt','hw5.py',174),
  ('stmt -> while_stmt NEWLINE','stmt',2,'p_stmt','hw5.py',175),
  ('small_stmts -> small_stmt small_ext','small_stmts',2,'p_small_stmts','hw5.py',184),
  ('small_ext -> <empty>','small_ext',0,'p_small_ext','hw5.py',190),
  ('small_ext -> small_stmts','small_ext',1,'p_small_ext','hw5.py',191),
  ('small_stmt -> assign_stmt','small_stmt',1,'p_small_stmt','hw5.py',200),
  ('small_stmt -> print_stmt','small_stmt',1,'p_small_stmt','hw5.py',201),
  ('assign_stmt -> NAME assign_ext','assign_stmt',2,'p_assign_stmt','hw5.py',207),
  ('assign_ext -> ASS_EQ INT','assign_ext',2,'p_assign_ext','hw5.py',220),
  ('assign_ext -> AUG_ASSIGN_PLUS INT','assign_ext',2,'p_assign_ext','hw5.py',221),
  ('print_stmt -> PRINT NAME','print_stmt',2,'p_print_stmt','hw5.py',230),
  ('while_stmt -> WHILE cmp_expr COLON NEWLINE INDENT stmts DEDENT','while_stmt',7,'p_while_stmt','hw5.py',235),
  ('cmp_expr -> NAME LT INT','cmp_expr',3,'p_cmp_expr','hw5.py',239),
]