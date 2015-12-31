inotifywait -q -e close_write -m $(dirname $0)/grab --format='%f' | while read -r line; do
	#echo "moving $line"
	mv $(dirname $0)/grab/$line $(dirname $0)/dv/
done
