# Start workers
`seq 1 10 | parallel --linebuffer -j num_workers.txt --roundrobin ./each.sh > logfile.txt &`

# Change worker count
`echo 1 > num_workers.txt`
