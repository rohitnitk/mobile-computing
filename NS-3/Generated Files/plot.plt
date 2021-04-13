set terminal png size  600, 400
set output "ns3_H3_cwnd.png"
set xlabel "seconds"
set ylabel "cwnd"
plot "application_6_h3_h6_a.cwnd" using 1:2 with lines title "ns-3", 

