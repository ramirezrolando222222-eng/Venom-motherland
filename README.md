# Venom-motherland
VENOM MOTHERLAND SYSTEM Cloud 
venom-motherland/
│
├── backend/
│   ├── venom_core.py              # Core brain + state engine + workers
│   ├── gateway.py                 # WebSocket + event gateway
│   ├── timex.py                   # Time validation engine
│   ├── memory.py                  # State history + audit log
│   ├── state_engine.py           # Single source of truth (workers/vaults)
│   ├── execution.py              # Worker simulation + task runner
│   ├── broadcast.py              # WebSocket fanout system
│   └── config.py                 # System configuration
│
├── frontend/
│   ├── index.html                # Motherland UI (3D canvas)
│   ├── app.js                    # WebSocket client + renderer logic
│   ├── styles.css                # HUD + matrix UI styling
│   └── renderer.js               # 3D world simulation layer
│
├── shared/
│   ├── protocol.py               # Event schema (JSON structure rules)
│   └── models.py                 # Worker / Vault / State definitions
│
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml       # Full system orchestration
│
├── scripts/
│   ├── start.sh                 # Local startup script
│   ├── build.sh                 # Docker build automation
│   └── deploy.sh                # Production deploy script
│
├── logs/
│   └── system.log               # Runtime logs (optional persistence)
│
├── LICENSE
├── NOTICE
├── README.md
└── requirements.txt
version: "3.9"

services:

  venom-backend:
    build:
      context: .
      dockerfile: docker/Dockerfile.backend
    ports:
      - "8765:8765"
    restart: always

  venom-frontend:
    build:
      context: .
      dockerfile: docker/Dockerfile.frontend
    ports:
      - "8080:80"
    restart: always
    FROM python:3.11

WORKDIR /app

COPY backend/ backend/
COPY shared/ shared/
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8765

CMD ["python", "backend/venom_core.py"]
FROM nginx:alpine

COPY frontend/ /usr/share/nginx/html

EXPOSE 80
VENOM MOTHERLAND SYSTEM

Copyright (c) 2026 Rolando H Ramirez Jr

All rights reserved.

This software and associated documentation files (the "Software") are proprietary and confidential.
Unauthorized copying, modification, distribution, or use of the Software, in whole or in part,
without the prior written permission of the copyright holder is strictly prohibited.
