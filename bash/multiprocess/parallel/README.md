# Start workers
`seq 1 10 | parallel --pipe -N1 -j num_workers.txt --roundrobin ./each.sh &`

# Change worker count
`echo 1 > num_workers.txt`
