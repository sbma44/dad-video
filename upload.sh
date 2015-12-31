echo "watching for files in $(dirname $0)/upload/ ..."
while [ 1 ]; do
    for f in `find $(dirname $0)/upload -type f`; do
        echo "uploading $f"
        PLAYLIST="`echo $(basename $f) | perl -ple 's/\-?\d{4}\.\d{2}\.\d{2}_\d{2}\-\d{2}\-\d{2}.*$//'`"
        $(dirname $0)/../.virtualenv/youtube-upload/bin/youtube-upload --title $(basename $f) --playlist "$PLAYLIST" --client-secrets=$(dirname $0)/lib/client_secret.json $f | tee $(dirname $0)/logs/$(basename $f).log
        if [ $? -eq 0 ]; then
            echo 'done.'
            mv $f $(dirname $0)/finished
        fi
    done
    sleep 1
done
