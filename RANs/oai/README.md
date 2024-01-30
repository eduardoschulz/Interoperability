# Configuration files for OPENAIRINTERFACE NR-5G

## gNB

```configfile

    amf_ip_address      = ( { ipv4       = "CHANGE for your ip addr to AMF";});

    NETWORK_INTERFACES :
    {
        GNB_INTERFACE_NAME_FOR_NG_AMF            = "CHANGE for your interface"; #eth0
        GNB_IPV4_ADDRESS_FOR_NG_AMF              = "CHANGE for your ip addr"; #191.4.205.128/23
        GNB_INTERFACE_NAME_FOR_NGU               = "CHANGE for your interface"; #eth0
        GNB_IPV4_ADDRESS_FOR_NGU                 = "CHANGE for your ip addr"; #191.4.205.128/23
        GNB_PORT_FOR_S1U                         = 2152; # Spec 2152
    };
```

## CU/DU Split

### CU

```configfile

    local_s_if_name = "CHANGE for your interface"; #lo
    local_s_address = "CHANGE for your ip addr of preference"; #127.0.0.4
    remote_s_address = "CHANGE for your DU ip addr"; #127.0.0.3

    amf_ip_address      = ( { ipv4       = "CHANGE for your ip addr to AMF";});

    NETWORK_INTERFACES :
    {
        GNB_INTERFACE_NAME_FOR_NG_AMF            = "CHANGE for your interface"; #eth0
        GNB_IPV4_ADDRESS_FOR_NG_AMF              = "CHANGE for your ip addr"; #191.4.205.128/23
        GNB_INTERFACE_NAME_FOR_NGU               = "CHANGE for your interface"; #eth0
        GNB_IPV4_ADDRESS_FOR_NGU                 = "CHANGE for your ip addr"; #191.4.205.128/23
        GNB_PORT_FOR_S1U                         = 2152; # Spec 2152
    };

```
### DU

```configfile

    local_s_if_name = "CHANGE for your interface"; #lo
    local_s_address = "CHANGE for your ip addr of preference"; #127.0.0.3
    remote_s_address = "CHANGE for your CU ip addr"; #127.0.0.4

```




