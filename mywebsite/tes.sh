
#!/bin/bash

# Menampilkan interface jaringan yang digunakan
echo "Interface jaringan: $(ip route show | awk '/default/ {print $5}')"

# Menampilkan jumlah data yang diterima dan dikirim
rx_bytes=$(cat /sys/class/net/$(ip route show | awk '/default/ {print $5}')/statistics/rx_bytes)
tx_bytes=$(cat /sys/class/net/$(ip route show | awk '/default/ {print $5}')/statistics/tx_bytes)

# Mengkonversi jumlah data dari bytes ke MB atau GB
rx_mb=$(echo $rx_bytes | awk '{printf "%.2f", $1 / 1024 / 1024}')
tx_mb=$(echo $tx_bytes | awk '{printf "%.2f", $1 / 1024 / 1024}')
rx_gb=$(echo $rx_bytes | awk '{printf "%.2f", $1 / 1024 / 1024 / 1024}')
tx_gb=$(echo $tx_bytes | awk '{printf "%.2f", $1 / 1024 / 1024 / 1024}')

# Menampilkan jumlah data yang diterima dan dikirim dalam MB atau GB
echo "Total data yang diterima: $rx_mb MB ($rx_gb GB)"
echo "Total data yang dikirim: $tx_mb MB ($tx_gb GB)"

