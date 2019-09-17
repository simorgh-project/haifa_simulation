wget https://snort.org/downloads/archive/snort/snort-2.9.9.0.tar.gz
tar -xvzf snort-2.9.9.0.tar.gz
cd snort-2.9.9.0
./configure --enable-sourcefire
make
sudo make install
ldconfig

snort -v --daq-list | grep nfq 
