dvgrab -a -t -rewind -showstatus $(dirname $0)/grab/${1}.dv 
curl -s --form-string "token=aCyP1YV268ER9XTNKfHvezW15XDqLX" --form-string "user=uqcWNJo8Hbk7BHTxhoiu9YmmNrN3fu" --form-string "message=dvgrab of $1 done" https://api.pushover.net/1/messages.json > /dev/null
