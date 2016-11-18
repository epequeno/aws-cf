from requests import get
from datetime import datetime

page = """\
<html>
    <head>
        <title>My instance info</title>
    </head>
    <body>
        <p>My instance id is: {my_id}</p>
        <p>I am in AZ: {my_az}</p>
        <p>File created at: {now}</p>
    </body>
</html>"""

base_url = 'http://169.254.169.254/latest/meta-data/{}'

instance_id = get(base_url.format('instance-id')).content
az = get(base_url.format('placement/availability-zone')).content
now = str(datetime.now())

page = page.format(my_id=instance_id, my_az=az, now=now)

with open('/var/www/html/index.html', 'w') as fd:
    fd.write(page)