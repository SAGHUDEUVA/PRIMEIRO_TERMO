# 🌐 Arquitetura de Redes e Internet das Coisas (IoT)

## 📅 Conteúdo das Aulas

### 🔹 Aula 01: Fundamentos de Redes e Ativos/Passivos
*   **Ativos de Rede:** Switches, roteadores, gateways e access points.
*   **Passivos de Rede:** Cabos estruturados, racks e conectores.

### 🔹 Aula 02: Internet e Suas Derivações na IoT
*   **Arquitetura de Conectividade:** Dispositivos finais, redes de borda (Edge) e nuvem (Cloud).

### 🔹 Aula 03: Controladores e Drivers - O Ecossistema ESP32
*   **Hardware para IoT:** Introdução à plataforma ESP32 e instalação de drivers de comunicação serial.

### 🔹 Aula 04: Protocolos de Comunicação - Foco em MQTT
*   **O Protocolo MQTT:** Conceitos de Publish/Subscribe, Broker, Tópicos e Payload.

## 💻 Código Prático: ESP32 + MicroPython + MQTT
```python
# Script para conectar o ESP32 ao Wi-Fi e enviar dados de sensores para o Broker
import time
import network
from umqtt.simple import MQTTClient

# Configurações de rede e broker omitidas para segurança
```