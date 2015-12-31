source $HOME/.env.personal

aws s3 cp html/index.html s3://sbma44-dadvideo/index.html
ls html/*.html | grep -v index.html | parallel -j4 aws s3 cp {} s3://sbma44-dadvideo/{}