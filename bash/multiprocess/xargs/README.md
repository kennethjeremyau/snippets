# Start workers
`cat input.txt | xargs -P2 -I{} ./each.sh {} &`

# Increase worker count
`kill -USR1 <PID>`

# Decrease worker count
`kill -USR2 <PID>`
