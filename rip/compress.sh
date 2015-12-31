echo "watching for files in $(dirname $0)/dv/ ..."
while [ 1 ]; do
    for f in `find $(dirname $0)/dv -type f`; do
        ffmpeg -i "$f" -vf fps=1/15 "$(dirname $0)/thumbs/$(basename $f '.dv')_%03d.jpg"
        ffmpeg -threads 2 -f dv -i "$f" -vcodec h264 -b:v 5000k -acodec mp3 -y "$(dirname $0)/h264/$(basename $f '.dv').avi"
        if [ $? -eq 0 ]; then
            for splitfile in `$(dirname $0)/lib/split_video_for_youtube.sh "$(dirname $0)/h264/$(basename $f '.dv').avi"`; do
                mv $splitfile $(dirname $0)/upload/
            done
            rm -f $f
        fi
    done
    sleep 1
done
