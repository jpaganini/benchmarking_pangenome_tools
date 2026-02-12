#! /bin/bash

#Pass the miniconda3 installation directory with the -c flag.

while getopts c: flag
do
  	case "${flag}" in
                c) conda=${OPTARG};;
        esac
done

source ${conda}/etc/profile.d/conda.sh

#---------------------------------------------------------------------------------------

#conda env create -f ../envs/ectyper_mmbioit.yml
conda activate ectyper_mmbioit

#create folders for holding tools
#mkdir ../tools
cd ../tools

#download virulencefinder and virulencefinder db
#git clone https://bitbucket.org/genomicepidemiology/virulencefinder.git
#git clone https://bitbucket.org/genomicepidemiology/virulencefinder_db.git


#establish the path to the database by setting the VIRULENCE_DB variable
cd virulencefinder_db
VIRULENCE_DB=$(pwd)

#python3 INSTALL.py kma_index

#-------run the virulencefinder tool-------
#create the folder for holding the results
#mkdir ../../results/virulence_finder

#get a list with all the files for which we will run the tool
all_plasmids=$(cat ../../../2020_08_25_ecoli_metadata/results/final_strain_list.csv | sed 's/"//g' | sed 's/_genomic//g') #this step will be removed in the final script

cd ../virulencefinder

for strains in $all_plasmids
do
mkdir ../../results/virulence_finder/${strains}
python virulencefinder.py -i ../../../2020_08_25_ecoli_metadata/data/fasta_final/${strains}_genomic.fna -o ../../results/virulence_finder/${strains} -t 0.95 -x -p ${VIRULENCE_DB}
done
