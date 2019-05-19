# Extraire les adresse d'une machine en cour d'execution
def ipaddr(name):
	domainName = name
	dom = conn.lookupByName(domainName)
	if dom == None:
		print('Failed to get the domain object')
	ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
	print("The interface IP addresses:")
	for (name, val) in ifaces.iteritems():
		if val['addrs']:
			print('----------')
			print(name+':')
			for ipaddr in val['addrs']:
				if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
					print("IPV4: "+ipaddr['addr'])
				elif ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV6:
					print("IPV6: "+ipaddr['addr'])
			print('----------')
	raw_input("Appuyer sur une touche pour revenir")


# lister tout les machine virtuelle et leurs etats

def lister_vm():

        clear()
        domainenames=conn.listDefinedDomains()
        for vm_name in domainenames:
                print('{{name:"{}",ID:"{}",state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(vm_name,"NONE","ShutDown","NONE","NONE"))
	for id in conn.listDomainsID():
		dom=conn.lookupByID(id)
		infos=dom.info()
                
                state, reason = dom.state()

		if state == libvirt.VIR_DOMAIN_NOSTATE:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"No State",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_RUNNING:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"Running",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_BLOCKED:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"Blocked",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_PAUSED:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"Pauded",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"ShutDown",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_SHUTOFF:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"ShutOff",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_CRASHED:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"Crached",infos[1],infos[3]))
		
		elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"Suspended",infos[1],infos[3]))
		
		else:
		    print('{{name:"{}",ID:"{}"   ,state:"{}",  max_mem:"{}",     nb_cpu:"{}"}}'.format(dom.name(),id,"UNKNOWN",infos[1],infos[3]))
		
		
	a0=raw_input("press enter")   





# Demarrer une machine virtuelle 
def demarrer_vm():

       clear()
       i=0
       domainenames=conn.listDefinedDomains()
       for vm_name in domainenames:
               print(str(i)+'. '+domainenames[i])
               i=i+1
       print(str(i)+'. QUITTER')
       if i==0:
               raw_input("Aucune Machine A Demarrer ")
      
       else:
	       start=input("choisissez une machine virtuelle :  ")	
               if start!=i:
		       vm_s=conn.lookupByName(domainenames[start])
		       vm_s.create()
	       	       a1=raw_input("Press Enter to Continue")
		     

# Arreter une machine virtuelle 
def arreter_vm():

       clear()
       i=0
       domainenames=conn.listDomainsID()
       for id in conn.listDomainsID():
		dom=conn.lookupByID(id)
	        print(str(i)+'. '+dom.name())
                i=i+1
       print(str(i)+'. QUITTER')
       if i==0:
               raw_input("Aucune Machine A Arreter")
      
       else:
	       start=input("choisissez une machine virtuelle :  ")	
               if start!=i: 
                       dom_arr=conn.lookupByID(domainenames[start])
		       vm_d=conn.lookupByName(dom_arr.name())
		       vm_d.destroy()
	       	       a1=raw_input("Press Enter to Continue")


#########################################################################
#########################################################################

import libvirt
import os
clear= lambda:os.system('clear')


conn=libvirt.open("qemu:///system")
boucler=1

while boucler !=6:
    clear()
    print'1. Nom de la machine hyperviseur'
    print'2. lister les machine virtuelle'
    print'3. demarrer une machine'
    print'4. arreter  une machine'
    print'5. L adresse IP d une machine'
    print'6. Quiter'
    boucler =input("Faite votre choix :")
    
    if boucler==1:
         clear()
         hp=conn.getHostname()
    	 print(hp)
         p=raw_input("press enter")
   
    if boucler==2:
         lister_vm()   
        
    if boucler==3:
         demarrer_vm()       

    if boucler==4:
         arreter_vm()

    if boucler==5:
       clear()
       i=0
       domainenames=conn.listDomainsID()
       for id in conn.listDomainsID():
		dom=conn.lookupByID(id)
	        print(str(i)+'. '+dom.name())
                i=i+1
       print(str(i)+'. QUITTER')
       if i==0:
               raw_input("Aucune machine n est en cour d execution")
      
       else:
	       start=input("choisissez une machine virtuelle :  ")	
               if start!=i: 
                   try:    
                       dom_arr=conn.lookupByID(domainenames[start])
		       ipaddr(dom_arr.name())
	       	       a1=raw_input("Press Enter to Continue")
                   except:
                       raw_input("  ")
conn.close()
exit()
