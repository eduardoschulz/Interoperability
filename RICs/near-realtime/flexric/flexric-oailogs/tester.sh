#!/bin/bash

for i in {0..100}
do
	./xapp_* -c flexric.conf | tee "logs/oai-$i.log"
done
