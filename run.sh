sudo cat << EOF > /etc/systemd/system/r4spi-fan-single.service
[Unit]
Description=r4spi-fan-single
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=python /workspace/r4spi-fan-single/src/main.py

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable r4spy-fan-single.service
sudo systemctl start r4spy-fan-single.service
