package main

import (
	"fmt"
	"log"
  "io/ioutil"
	"net"
)

var hostnames = [4]string{
  "core",
  "thinkpad01",
  "oai-cu",
  "gnb-du",
}

var ipaddrs [4]string


/*
* Function get_ipaddr
* recv string hostname
* output string ipaddr
* 
* make a lookup in the network looking 
* for the first ip address of defined hostname
*/


func get_ipaddr(hostname string) string {
  ipaddr, err := net.LookupHost(hostname)
  if err != nil {
    log.Print(err)
    return "not found"
  }

  fmt.Printf("\n%s: %s",hostname,ipaddr[0])
  return ipaddr[0]
}


/*
* Function write_tofile
* recv: string regex, string filepath 
* output void
* 
* receives a regex and uses sed to modified 
* the desired file. 
*/

func write_tofile(regex string, filepath string) {
  
  content, err := ioutil.ReadFile(filepath)

  if err != nil {
    log.Println("Error reading file: ", err)
    return 
  }

  /*example of regex to be used 
  pattern := regexp.MustCompile('local_n_address\s*=\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')

  output := pattern.ReplaceAllString(input, 'local_n_address = {ipaddr[1]"

  */
  





}





func main(){


  idx := 0
  for _,hostname := range hostnames {

    ipaddrs[idx] = get_ipaddr(hostname)
    idx++

  }

  
}
