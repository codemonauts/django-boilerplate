#! /bin/bash
set -eu

OLDNAME=$1
NEWNAME=$2

sed -i "s/$OLDNAME/$NEWNAME/" manage.py
sed -i "s/$OLDNAME/$NEWNAME/" $OLDNAME/wsgi.py
sed -i "s/$OLDNAME/$NEWNAME/" $OLDNAME/settings/common.py
sed -i "s/$OLDNAME/$NEWNAME/" $OLDNAME/urls.py
sed -i "s/$OLDNAME/$NEWNAME/" docker-compose.yml

mv $OLDNAME $NEWNAME

echo "Done"
