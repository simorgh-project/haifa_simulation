#install gateway wireless driver
#if (( opkg list_installed | grep -q 'snort'))
#	then
#		echo "found"
#	else
#		opkg update 
#		opkg install snort --force-maintainer 
#		opkg install python python-pip
#		python -m pip install -U --force-reinstall wget
#		cp snort.conf /etc/snort/snort.conf
#		mv rules /etc/snort/rules/
#		mv logs /etc/snort/logs
#		mv preproc_rules /etc/snort/preproc_rules/
#		mv so_rules /etc/snort/so_rules/
#		echo "snort installed & running"
#fi



/etc/init.d/snort stop
killall snort
snort -c "/etc/snort/snort.conf" -Q -i eth0:eth1 --daq-dir /usr/lib/daq
