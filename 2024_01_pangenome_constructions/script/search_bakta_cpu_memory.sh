
cd /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/bakta_complete_slurm_jobs/

jobs=$(ls -1 | grep 'slurm-.*\.out' | sed 's/^slurm-\(.*\)\.out$/\1/')

for strains in $jobs
do
sacct -j ${strains} --format=JobID,MaxRSS,MaxVMSize,AllocCPUs,TotalCPU,Start,End,Elapsed | awk 'NR==4' >>/hpc/uu_vet_iras/pliu/remove_bad_result/bakta_cpu_memory/173_complete_complete_bakta_cpu_memory.csv
done
