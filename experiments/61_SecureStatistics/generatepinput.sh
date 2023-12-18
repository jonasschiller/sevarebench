#!/bin/bash

REPO2_DIR=$(pos_get_variable repo2_dir --from-global)
amount=$1
partysize=$2
inputtype="-t"

echo "create matrix with base-size: $amount"
for i in $(seq 0 $((partysize-1))); do
    "$REPO2_DIR"/helpers/inputgen.py $inputtype "$((amount*3))" "$((amount*amount*2))" "$i" > Player-Data/Input-P"$i"-0
done