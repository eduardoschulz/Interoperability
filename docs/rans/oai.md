# OpenAirInterface

[OpenAirInteface](oai/README.md)
For our testing we used the 2.1 release of the project.
### How to Build

+ [UHD - Build Instructions](https://files.ettus.com/manual/page_build_guide.html)
+ [OAI - Build Instructions(No E2Agent)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/BUILD.md)
+ [OAI - Build Instructions(Flexric)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/openair2/E2AP/README.md)

#### Build with Flexric
In this setup we have used **OpenAirInterface** built with the _--build-e2_ flag.

## 0. Required dependencies

### 0.1 Building Swig

```shell
$ git clone https://github.com/swig/swig.git && cd swig
$ git checkout release-4.2
$ ./autogen.sh
$ ./configure --prefix=/usr/
$ make -j$(nproc)
$ sudo make install
```

### 0.2 Installing other dependencies

```shell
$ sudo apt install libsctp-dev python3 cmake-curses-gui libpcre2-dev

```
## 1. Building **OpenAirInterface**

```shell
$ git clone https://gitlab.eurecom.fr/oai/openairinterface5g oai
$ cd oai
$ git checkout v2.1.0
$ ./build_oai -w USRP --gNB --nrUE --build-e2 
```

## 2. Building Flexric

```shell
$ cd oai/openair2/E2AP/flexric
$ mkdir build && cd build
$ cmake -DSWIG_DIR=/usr/share/swig/4.2.0/ -DSWIG_EXECUTABLE=/usr/bin/swig -DCMAKE_C_COMPILER=gcc-10 -DCMAKE_CXX_COMPILER=g++-10 ..
$ make -j$(nproc)
$ sudo make install 
```

## 3. Launching gNB

### 3.1 gNB configuration

First some modifications on the configuration file are required to make the gNB work properly. Some of the configurations bellow are optional depending on your setup.

```shell
$ cd /path-to/openairinterface5g/targets/PROJECTS/GENERIC-NR-5GC/CONF
$ vi gnb.sa.band78.fr1.106PRB.usrpb210.conf #in this case we're using the usrp b210.
```

```config
tracking_area_code  =  1;
plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ({ sst = 1; }) }); #in this case we are using the test plmn 00101
...
min_rxtxtime = 6;
...
amf_ip_address      = ( { ipv4       = "191.4.205.169"; #change this to our amf ip; default for oai cn: 192.168.70.132
                          ipv6       = "192:168:30::17";
                          active     = "yes";
                          preference = "ipv4";
                        }
                      );


NETWORK_INTERFACES :
    {
        GNB_INTERFACE_NAME_FOR_NG_AMF            = "br01"; #change to our host machine network interface of choice
        GNB_IPV4_ADDRESS_FOR_NG_AMF              = "191.4.204.211"; #change to the ip addr of the interface selected 
        GNB_INTERFACE_NAME_FOR_NGU               = "br01"; #change to our host machine network interface of choice
        GNB_IPV4_ADDRESS_FOR_NGU                 = "191.4.204.211"; #change to the ip addr of the interface selected 
        GNB_PORT_FOR_S1U                         = 2152;
    };
...

e2_agent = {
    near_ric_ip_addr = "191.4.204.161" #change to to the ip addr of the ric. If you are running flexric locally --> 127.0.0.1
    sm_dir = "/usr/local/lib/flexric/"
};
```
### 3.2 Running nr-softmodem

```shell
$ sudo ./nr-softmodem -O /path-to/gnb.conf --sa -E --continuous-tx | tee oai.logs
```
