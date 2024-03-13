# RANs

## Open Air Interface 
[OpenAirInteface](oai/README.md)
For our testing we used the 2.1 release of the project.
### How to Build

+ [UHD - Build Instructions](https://files.ettus.com/manual/page_build_guide.html)
+ [OAI - Build Instructions(No E2Agent)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/BUILD.md)
+ [OAI - Build Instructions(Flexric)](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/openair2/E2AP/README.md)

#### Build with Flexric
In this setup we have used OpenAirInterface built with the _--build-e2_ flag.
```shell

## 0. Required dependencies

### 0.1 Building Swig

$ git clone https://github.com/swig/swig.git && cd swig
$ git checkout release-4.2
$ ./autogen.sh
$ ./configure --prefix=/usr/
$ make -$(nproc)
$ sudo make install

### 0.2 Installing other dependecies

$ sudo apt install libsctp-dev python3 cmake-curses-gui libpcre2-dev

## 1. Building OAI

$ git clone https://gitlab.eurecom.fr/oai/openairinterface5g oai
$ cd oai
$ git checkout v2.1.0
$ ./build_oai -w USRP --gNB --nrUE --build-e2 

## 2. Building Flexric

$ cd oai/openair2/E2AP/flexric
$ cmake -DSWIG_DIR=/usr/share/swig/4.2.0/ -DSWIG_EXECUTABLE=/usr/bin/swig -DCMAKE_C_COMPILER=gcc-10 -DCMAKE_CXX_COMPILER=g++-10 ..
$ make -j20
$ sudo make install 

```
