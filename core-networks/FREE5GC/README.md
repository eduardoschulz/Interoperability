# Free5GC

For our test we chose version *v3.3.0* given that it was the latest available when we were testing.
https://github.com/free5gc/free5gc-compose.git

We have tested two COTS UE during the experiment, a Samsung Galaxy A33 and a Oneplus Nord N10. The samsung device was unable to connect to our network because of a limitation imposed by samsung, by default the device has a list of blocked PLMNS which we were not able to modify. Because of that we could not use 90170 as our PLMN and we were not able to get free5gc to work under roaming. 

Using the test PLMN(00101) we were able to connect both devices but with a caviat, the A33 was much more unstable compared to the oneplus using openairinterface. This problem persisted during our test with others core networks.
