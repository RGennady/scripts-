#!/bin/bash
 dir=/home/backup_sql/
 count=$(find $dir -maxdepth 1 -name '*.gz' | wc -l)
 if [ "$count" -gt 40 ] ; then
    ssh root@127.0.0.1 mysqldump -u sql_user --password=user_password$ db_name | gzip > /home/backup_sql/backup-`date '+%d-%B-%Y-%T'`.gz
	find "$dir" -type f | xargs stat -c "%Y %n" | sort -n | head -1 | cut -d' ' -f2 | xargs rm -f
 else
 	ssh root@127.0.0.1 mysqldump -u sql_user --password=user_password$ db_name | gzip > /home/backup_sql/backup-`date '+%d-%B-%Y-%T'`.gz
 fi

