for dir in 'dv' 'upload' 'h264' 'finished' 'thumbs'; do
    find $dir -type f | wc -l | xargs -I {} echo "${dir} files: {}"
done
