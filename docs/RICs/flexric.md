# Flexric

## 0. Required dependencies

### 0.1 Prerequisites

* CMake (v >= v3.22)
* Swig (v >= v.4.1)

#### 0.1.1 Building Swig

```shell
$ git clone https://github.com/swig/swig.git && cd swig
$ git checkout release-4.1
$ ./autogen.sh
$ ./configure --prefix=/usr/
$ make -j$(nproc)
$ sudo make install
```
### 0.2 Other dependencies

```shell
$ sudo apt install libsctp-dev python3 cmake-curses-gui libpcre2-dev python3-dev
``` 

## 1.0 Building Flexric
```
$ git clone https://gitlab.eurecom.fr/mosaic5g/flexric.git
$ git checkout <*version>
```

\*For an oai install refer back to [oai-flexric](/docs/RANs/oai.md). More information can be found [at](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/openair2/E2AP/README.md).

```shell
$ cd flexric
$ mkdir build && cd build
$ cmake -DSWIG_DIR=/usr/share/swig/4.1.0/ -DSWIG_EXECUTABLE=/usr/bin/swig -DCMAKE_C_COMPILER=gcc-10 -DCMAKE_CXX_COMPILE=g++-10 ..
$ make -j$(nproc)
$ sudo make install
```

## 2.0 Running Flexric
### 2.1 NearRT-RIC
``` 
$ cd build/examples/ric/
$ ./nearRT-RIC # you can use -c to specify a config file
```
### 2.2 Running a xApp
```
$ cd build/examples/c/monitor/
$ ./xapp_kpm_moni

```
