# 🧪 Cisco DNA Center API Cheat Sheet

A fast-start guide for interacting with Cisco DNA Center’s RESTful API — from token generation to practical data pulls.

---

## 🔐 1. Authenticate: Get Your Auth Token

**Endpoint:**
POST /dna/system/api/v1/auth/token

**Full URL:**
https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token

**Headers:**
Content-Type: application/json
Authorization: Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=

> The Authorization value is the base64 encoding of `devnetuser:Cisco123!`.

**Sample Response:**
```json
{
  "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 📡 2. Make Your First API Call

Use the token from Step 1 in your headers:

**Header:**
X-Auth-Token: <your token here>

Example:
```bash
curl -X GET \
  https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device \
  -H "X-Auth-Token: <your token here>"
```

---

## 🧠 3. Common DNAC API Endpoints

### ✅ Get All Network Devices
GET /dna/intent/api/v1/network-device

### 🗺️ Get Site Topology
GET /dna/intent/api/v1/site

### 📋 Get Client Health
GET /dna/intent/api/v1/client-health

### 🔧 Get Interface Info
GET /dna/intent/api/v1/interface

---

## 🧪 4. Example curl Commands

### 🔐 Get Auth Token
```bash
curl -X POST \
  https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="
```

### 📡 Get Network Devices
```bash
curl -X GET \
  https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device \
  -H "X-Auth-Token: <your token here>"
```

---

## 🛠 Sandbox Info

| Field       | Value                       |
|-------------|-----------------------------|
| Base URL    | https://sandboxdnac2.cisco.com |
| Username    | devnetuser                  |
| Password    | Cisco123!                   |

---

## 🧭 Tips

- Tokens expire after ~1 hour — re-auth frequently
- DNAC APIs use `X-Auth-Token` (no "Bearer" prefix)
- DNAC sandboxes reset often — your data is ephemeral
- Use Postman or Python scripts for more advanced flows

---

## 🐍 Optional: Python Script Starter (Auth + Device Pull)

```python
import requests

BASE_URL = "https://sandboxdnac2.cisco.com"
AUTH_ENDPOINT = "/dna/system/api/v1/auth/token"
DEVICE_ENDPOINT = "/dna/intent/api/v1/network-device"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

# Get Token
auth_response = requests.post(
    f"{BASE_URL}{AUTH_ENDPOINT}",
    auth=(USERNAME, PASSWORD),
    headers={"Content-Type": "application/json"},
    verify=False  # For sandbox only
)
token = auth_response.json()["Token"]

# Make API Call
device_response = requests.get(
    f"{BASE_URL}{DEVICE_ENDPOINT}",
    headers={"X-Auth-Token": token},
    verify=False
)
devices = device_response.json()["response"]

# Print Hostnames
for d in devices:
    print(f"{d['hostname']} ({d['managementIpAddress']}) - {d['softwareVersion']}")
```

---

