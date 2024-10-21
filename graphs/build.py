import ram_core_mono
import ram_core_split
import ram_mono
import ram_split_cu
import ram_split_du
import cpu_core_mono
import cpu_core_split
import cpu_mono
import cpu_split_cu
import cpu_split_du
import iperf_split
import iperf_mono
import retransmissions_split
import retransmissions_mono

ram_core_mono.build()
ram_core_split.build()
ram_mono.build()
ram_split_cu.build()
ram_split_du.build()
cpu_core_mono.build()
cpu_core_split.build()
cpu_mono.build()
cpu_split_cu.build()
cpu_split_du.build()
iperf_split.build()
iperf_mono.build()
retransmissions_split.build()
retransmissions_mono.build()
