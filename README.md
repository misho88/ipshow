# ipshow - Nicely-Formatted IP Information

`ip address show` (`ip a`) and `ip route show` (`ip r`) more or less give all
the information a user could want about a network's setup. Usually, they just
want to know about IP addresses, MAC addresses and maybe the default gateway,
so I just threw all that together in one place:

```
$ ipshow
IP
Interface  Address        Netmask  Broadcast        Gateway
       lo  127.0.0.1      /8       ---              ---
   wlp4s0  10.0.0.109     /24      10.0.0.255       10.0.0.1
           192.168.77.3   /24      192.168.0.0      ---
   virbr0  192.168.122.1  /24      192.168.122.255  ---
     vpn0  XXX.XXX.XX.XX  /16      ---              ---
     tun0  XXX.XXX.XXX.X  /24      ---              XXX.XXX.XXX.X*

IPv6
Interface  Address                    Netmask  Gateway
       lo  ::1                        /128     ---
   wlp4s0  fe80::a1e8:aecc:401b:e4a0  /64      ---
     vpn0  XXXX::XXXX:XXXX:XXXX:XXXX  /64      ---
     tun0  XXXX::XXXX:XXXX:XXXX:XXXX  /64      ---

MAC
 Interface  Address
        lo  00:00:00:00:00:00
 enp0s31f6  XX:XX:XX:XX:XX:XX
    wlp4s0  XX:XX:XX:XX:XX:XX
    virbr0  52:54:00:87:55:eb
virbr0-nic  52:54:00:87:55:eb
```

## Requirements

`pysh` which in turn needs `funcpipes`:

https://github.com/misho88/pysh
https://github.com/misho88/funcpipes
