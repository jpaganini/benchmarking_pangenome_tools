#!/bin/bash

#create dir to hold results
mkdir ../results/sistr/modified_output

#get a list of files
isolates=$(ls ../results/sistr)

for i in ${isolates}
do
awk 'BEGIN { FS=OFS="," } {
    in_quotes=0
    for (i=1; i<=NF; i++) {
        if (in_quotes) {
            current = current OFS $i
            if (substr($i, length($i)) == "\"") {
                in_quotes=0
            }
        } else {
            if (substr($i, 1, 1) == "\"") {
                in_quotes=1
                current = $i
            } else {
                current = $i
            }
        }
        if (!in_quotes || i == NF) {
            gsub(",", "\t", current)
            printf "%s", current
            if (i < NF) {
                printf "%s", OFS
            }
            current = ""
        }
    }
    printf "\n"
}' ${i} > modified_output/${i}
