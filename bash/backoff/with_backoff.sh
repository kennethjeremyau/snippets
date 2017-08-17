max_attempts=${ATTEMPTS-5}
timeout=${TIMEOUT-1}
attempt=0
exitCode=0

while [[ $attempt < $max_attempts ]]; do
	"$@"
	exitCode=$?

	if [[ $exitCode == 0 ]]; then
		break
    fi

    echo "Failure! Retrying in $timeout.." 1>&2
    sleep $timeout
    attempt=$(( attempt + 1 ))
    timeout=$(( timeout * 2 ))
done

if [[ $exitCode != 0 ]]; then
	echo "No more attempts. ($@)" 1>&2
fi

exit $exitCode
