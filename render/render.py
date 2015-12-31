import json, sys, os.path, datetime, re, math

MAX_STILLS = 18

def header():
    return """<!doctype html>
<html>
    <head>
    <style type="text/css">
    .thumb-sm {
        background-color: gray;
        width: 200px;
        height: 133px;
    }
    .dadOverlay {
        border: 5px solid rgba(255, 255, 255, 0.8);
    }
    </style>
    <script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
    </head>
    <body>
"""

def footer():
    return """
    <script type="text/javascript">
    var mouseX, mouseY;
    (function() {
        $(document).mousemove(function(event){
            mouseX = event.pageX;
            mouseY = event.pageY;
        });

        $('.thumb-sm')
        .mouseover(function() {
            var left = (mouseX > (window.innerWidth / 2)) ? 20 : window.innerWidth - 750;
            var top = (mouseY > ($(window).scrollTop() + (window.innerHeight / 2))) ? $(window).scrollTop() + 20 : $(window).scrollTop() + window.innerHeight - 500;

            var newElement = $('<img class="dadOverlay" style="position:absolute; top: ' + top + 'px; left: ' + left + 'px" src="' + this.src.replace('thumbs-small', 'thumbs') + '" />');
            this.dadOverlay = $('body').append(newElement);
        })
        .mouseout(function() {
            $('.dadOverlay').remove();
        });
    })();
    </script>
    </body>
</html>
"""

def main():
    with open(sys.argv[1]) as f:
        videos = json.load(f)

    index_out = header()
    for video in sorted(videos.keys()):
        video_html = header()
        video_html += '<h1>%s</h1>' % re.sub(r'\-$', '', video)

        index_out += '<div class="video"><h1><a href="html/%s.html">%s</a></h1>' % (video, re.sub(r'\-$', '', video))

        index_out_candidates = []

        video_dates = []
        for date in videos[video]:
            ds = [int(x) for x in date.split('.')]
            video_dates.append((datetime.datetime(ds[0], ds[1], ds[2]), date))

        for date in sorted(video_dates, key=lambda x: x[0]):
            video_html += '<h2>%s</h2>' % date[0].strftime('%B %d, %Y')

            subdates = []
            for subdate in videos[video][date[1]]:
                parts = [int(x) for x in subdate.split('-')]
                subdates.append((((parts[0] * 3600) + (parts[1] * 60) + parts[0]), subdate))
            for subdate in sorted(subdates, key=lambda x: x[0]):
                target = videos[video][date[1]][subdate[1]]
                midpoint = math.floor(int(target[1]) / 2)

                for i in range(1, int(target[1])):
                    index_out_candidates.append('<a href="html/%s.html"><img class="thumb-sm" src="https://s3.amazonaws.com/sbma44-dadvideo/thumbs-small/%s%s_%s_%03d.jpg"/></a>' % (video, video, date[1], subdate[1], i))
                    video_html += '<a href="https://www.youtube.com/watch?v=%s&t=%d"><img class="thumb-sm" src="https://s3.amazonaws.com/sbma44-dadvideo/thumbs-small/%s%s_%s_%03d.jpg"/></a>' % (target[0], (i-1)*15, video, date[1], subdate[1], i)

        everyth = max(1, len(index_out_candidates) / MAX_STILLS)
        second_pass = []
        for (i, cand) in enumerate(index_out_candidates):
            if (i % everyth) == 0:
                second_pass.append(cand)
        second_pass = second_pass[:MAX_STILLS]
        index_out += ''.join(second_pass)

        index_out += '</div>'

        video_html += footer()

        with open('html/%s.html' % video, 'w') as f:
            f.write(video_html)

    index_out += footer()

    with open('html/index.html', 'w') as f:
        f.write(index_out)


if __name__ == '__main__':
    main()