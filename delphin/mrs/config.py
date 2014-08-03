# encoding: UTF-8

# constants used throughout the mrs library
# In the future, these should probably move to a proper settings module

LTOP_NODEID    = 0
FIRST_NODEID   = 10000 # the nodeid assigned to the first node
# sortal values
UNKNOWNSORT    = 'u' # when nothing is known about the sort
HANDLESORT     = 'h' # for scopal relations
QUANTIFIER_SORT= 'q' # for quantifier preds
# Pred
GRAMMARPRED    = 'grammarpred' # only a string allowed
REALPRED       = 'realpred'    # may explicitly define lemma, pos, sense
STRINGPRED     = 'stringpred'  # string-form of realpred
# HCONS
QEQ            = 'qeq'
LHEQ           = 'lheq'
OUTSCOPES      = 'outscopes'
# ARGUMENTS
INTRINSIC_ARG  = 'IntrinsicArgument'
VARIABLE_ARG   = 'VariableArgument'
HOLE_ARG       = 'HoleArgument' # supertype of LABEL_ARG and HCONS_ARG
LABEL_ARG      = 'LabelArgument'
HCONS_ARG      = 'HconsArgument'
CONSTANT_ARG   = 'ConstantArgument'
# MRS strings
CVARG          = 'ARG0'
CONSTARG       = 'CARG'
# RMRS strings
ANCHOR_SORT    = HANDLESORT # LKB output is like h10001, but in papers it's a1
# DMRS strings
RSTR           = 'RSTR' # DMRS establishes that quantifiers have a RSTR link
EQ_POST        = 'EQ'
HEQ_POST       = 'HEQ'
NEQ_POST       = 'NEQ'
H_POST         = 'H'
NIL_POST       = 'NIL'
CVARSORT       = 'cvarsort'
