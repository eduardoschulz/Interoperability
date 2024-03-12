#!/bin/bash

BIND_IP=$(ip addr show br01 | grep -o 'inet [0-9\\.]*' | grep -o '[0-9\\.]*')
CORE_IP=$(ping -c 1 core.local | awk -F" |:" '/from/{print $5}' | grep -o '[0-9\\.]*')
RIC_IP=$(ping -c 1 thinkpad01 | awk -F" |:" '/from/{print $5}' | grep -o '[0-9\\.]*')


echo $CORE_IP
echo $BIND_IP
echo $RIC_IP

sed -Ei "s/    amf_ip_address      = \( \{ ipv4       = \"\S*\";/    amf_ip_address      = \( \{ ipv4       = \"$CORE_IP\";/"  gnb.conf
sed -Ei "s/        GNB_IPV4_ADDRESS_FOR_NG_AMF              = \"\S*\";/        GNB_IPV4_ADDRESS_FOR_NG_AMF              = \"$BIND_IP\";/" gnb.conf
sed -Ei "s/        GNB_IPV4_ADDRESS_FOR_NGU                 = \"\S*\";/        GNB_IPV4_ADDRESS_FOR_NGU                 = \"$BIND_IP\";/" gnb.conf

sed -Ei "s/  near_ric_ip_addr = \"\S*\";/  near_ric_ip_addr = \"$RIC_IP\";/" gnb.conf
