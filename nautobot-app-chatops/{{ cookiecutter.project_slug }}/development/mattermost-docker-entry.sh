#!/bin/bash
# Copyright (c) 2016 Mattermost, Inc. All Rights Reserved.
# See License.txt for license information.

echo "Starting MySQL"
/entrypoint.sh mysqld &

until mysqladmin -hlocalhost -P3306 -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" processlist &> /dev/null; do
	echo "MySQL still not ready, sleeping"
	sleep 5
done

echo "Updating CA certificates"
update-ca-certificates --fresh >/dev/null

if [ ! -e "/mm/mattermost-data/users" ]; then
    echo "-- Adding admin user --"
    mattermost user create --system_admin --email "admin@example.com" --username "admin" --password "Nautobot123!!" &> /dev/null
	echo "-- Adding ntcbot user --"
	mattermost user create --system_admin --email "nautobot-bot@exampe.com" --username "nautobot-bot" --password "Nautobot123!!" &> /dev/null
	echo "-- Converting user to bot --"
	mattermost user convert ntcbot --bot
	echo "-- Creating automationteam team --"
	mattermost team create --name automationteam --display_name "Automation Team"
	echo "-- Adding users to automationteam team"
	mattermost team add automationteam admin nautobot-bot
	echo "Starting platform"
	cd mattermost
	exec mattermost --config=config/config_docker.json
else
	echo "Starting platform"
	cd mattermost
	exec mattermost --config=config/config_docker.json
fi
