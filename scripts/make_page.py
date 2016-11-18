from requests import get
from datetime import datetime

base_url = 'http://169.254.169.254/latest/meta-data/{}'

instance_id = get(base_url.format('instance-id')).content
az = get(base_url.format('placement/availability-zone')).content
now = str(datetime.now())

page = """\
<html>
    <head>
        <title>My instance info</title>
    </head>
    <body>
        <p>My instance id is: {id}</p>
        <p>I am in AZ: {az}</p>
        <p>File created at: {now}</p>
    </body>
</html>"""

page = page.format(id=instance_id, az=az, now=now)

with open('/var/www/html/index.html', 'w') as fd:
    fd.write(page)