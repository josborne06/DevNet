# 🔥 Cisco Live 2025 – Firewall Deep Dive Session

**Speaker**: Key (Cisco Product Manager, Secure Firewall)  
**Transcript**: [Otter.ai Full Transcript](https://otter.ai/u/vVZKJfWwGHjk7K1fyKnUP326kj4)  
**Focus**: Cisco Secure Firewall portfolio, lifecycle, design, performance, clustering, and multi-tenancy

---

## 🎯 Session Summary

This session covered the evolution and architecture of Cisco's Secure Firewalls — from PIX to ASA to FTD — and detailed Cisco’s newest platforms (220, 3100, 4200, 6100 series). Key design topics included clustering, performance tuning, multi-tenancy, and high availability.

---

## 🚀 Action Items

- [ ] Explore **Elephant Flow Offload** to improve high-throughput performance
- [ ] Review policy scale limits by platform to stay within **supported thresholds**
- [ ] Understand **L3 Clustering** design for scalable and HA environments
- [ ] Evaluate **multi-tenancy models**: multi-instance, domains, VRFs, virtual firewalls

---

## 🔧 Firewall Portfolio Evolution

| Legacy | Modern |
|--------|--------|
| PIX → ASA → FTD OS | FTD across physical & virtual platforms |

- End-of-sale: 2100, 4100, 9300 series (plan migration or extended support)
- New hardware:  
  - 🧱 **220 Series** – Low-power branch firewall  
  - 🚀 **6100 Series** – Flagship powerhouse (up to 256 physical cores)

---

## 🖥️ Hardware Breakdown

### 🔹 Cisco 6100 Series
- Up to **256 physical cores**
- 16 ports: **10/25/50G** supported
- FPGAs + crypto acceleration
- Future-proof for **hyper-scale edge or core**

### 🔹 Cisco 4200 Series
- Up to **120 cores**, 8 ports
- Up to **145 Gbps** throughput
- Built-in hardware bypass, ideal for **large enterprises**

### 🔹 Cisco 3100 Series
- High-performance for **data centers**
- Models like 3130/3140 support **100G interfaces**

### 🔹 Cisco 1200 Compact / Threat Mount
- ARM-based SoC
- Compact models support up to **9 Gbps**
- Threat Mount adds more cores & capabilities

---

## 🧪 Testing & Benchmarking

- Testing standards: **NetSecOpen**, **RFC 9411**
- Use the [NGFW Performance Estimator](https://www.cisco.com/go/ngfw-performance)  
- Best practice: Validate based on **your traffic mix**, not raw numbers

---

## 🛡️ High Availability & Clustering

- **HA Active-Standby** and **Clustering (16 nodes)**
- Load-balanced traffic via Flow Owner model
- Scalability + Resiliency = Key goals

---

## 🧩 Multi-Tenancy Best Practices

| Feature | Description |
|--------|-------------|
| **Domains** | Logical separation of admins/policies |
| **Multi-Instance** | Run multiple logical firewalls on one physical box |
| **VRFs + BGP leaking** | Route segmentation for tenants |
| **Virtual Firewalls** | Separate policies and zones per tenant |

- Supported on: **4100, 1000, 9300 series**
- Map physical IFs → zones → assign policies per tenant

---

## 🗓️ Lifecycle & Support

- 🔚 End-of-Sale reminders for older models
- 🔐 Security fixes continue **post-EOL** (limited support)
- 🔄 Plan transitions to **3100+, 4200+, 6100 series**

---

## 🧠 Key Takeaways

- Firewall sizing is **mission-critical** — use estimators
- Always architect for **redundancy (HA, clustering)**
- Embrace **VRFs and virtualization** for multi-tenant security
- Use **hardware acceleration** (FPGA, crypto offload) to optimize performance

---

## 📚 Related Resources

- [Cisco Secure Firewall Portfolio](https://www.cisco.com/site/us/en/products/security/firewalls/index.html)
- [FTD Release Notes](https://www.cisco.com/c/en/us/support/security/firepower-ngfw/products-release-notes-list.html)
- [Cisco Firepower Compatibility Guide](https://www.cisco.com/c/en/us/support/security/firepower-ngfw/products-device-support-tables-list.html)
- [NGFW Estimator Tool](https://www.cisco.com/go/ngfw-performance)

---

> “Design for performance. Plan for growth. Build for segmentation.” – Cisco Secure Firewall Team
```