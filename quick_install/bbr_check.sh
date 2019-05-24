echo 'bbr cubic reno or reno cubic bbr'
sysctl net.ipv4.tcp_available_congestion_control
echo 'bbr'
sysctl net.ipv4.tcp_congestion_control
echo 'fq'
sysctl net.core.default_qdisc
