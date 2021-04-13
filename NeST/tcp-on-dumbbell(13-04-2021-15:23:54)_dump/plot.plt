set terminal png size  600, 400
set output "NeST_H3_cwnd.png"
set xlabel "seconds"
set ylabel "cwnd"
plot "cwnd_data_node_2.txt" using 1:2 with lines title "NeST" 
