# Contracts library
from contracts.contracts import input_contract, output_contract
from contracts.exceptions import InputContractException, OutputContractException
from contracts.qualifiers import *

name = "contracts"

# Abbreviated names
ic = input_contract
oc = output_contract

# Alternate names
pre = input_contract
post = output_contract