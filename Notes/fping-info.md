# fping Cheat Sheet

A concise reference for using **fping** in your network scripts and repos.

---

## 📥 Installation

- **Debian/Ubuntu:**
  ```bash
  sudo apt-get update && sudo apt-get install fping
  ```
- **RedHat/CentOS:**
  ```bash
  sudo yum install fping
  ```
- **macOS (Homebrew):**
  ```bash
  brew install fping
  ```

---

## ⚙️ Basic Syntax

```bash
fping [options] <hosts>...
```

- **Hosts** can be:
  - Single IP/FQDN: `192.168.1.1` or `example.com`
  - Range: `192.168.1.1 192.168.1.254`
  - CIDR: `-g 192.168.1.0/24`
  - Hostfile: `-f hosts.txt`

---

## 🔑 Common Options

| Option      | Description                                   |
|-------------|-----------------------------------------------|
| `-a`        | Show only **alive** hosts                     |
| `-u`        | Show only **unreachable** hosts               |
| `-g <net>`  | Generate ping targets from CIDR (e.g. /24)    |
| `-f <file>` | Read hosts from a file (newline-separated)    |
| `-c <num>`  | Send `<num>` pings per host (default: 1)      |
| `-i <ms>`   | Interval between pings in milliseconds        |
| `-t <ms>`   | Timeout for each ping in milliseconds         |
| `-r <num>`  | Retry `<num>` times before giving up          |
| `-q`        | Quiet output (just summary)                   |
| `-l`        | Loop continuously until interrupted           |
| `-p <ms>`   | Wait `<ms>` between ping packets (interval)   |
| `-b <bytes>`| Send packets of `<bytes>` size                |

---

## 💡 Examples

- **Ping a single host:**
  ```bash
  fping 10.0.0.1
  ```

- **Ping a /24 network:**
  ```bash
  fping -g 192.168.1.0/24
  ```

- **Use a host list file:**
  ```bash
  fping -f hosts.txt
  ```

- **Show only alive hosts:**
  ```bash
  fping -a -g 10.0.0.0/24
  ```

- **Retry and timeout settings:**
  ```bash
  fping -c 3 -i 200 -t 500 10.0.0.1
  ```

- **Continuous monitoring:**
  ```bash
  fping -l -i 1000 10.0.0.1 10.0.0.2
  ```

---

## 📋 Parsing & Scripting Tips

- **Batch Scripts:** Redirect output to parse alive/unreachable.
  ```bash
  fping -a -g 10.0.0.0/24 > up.txt
  fping -u -g 10.0.0.0/24 > down.txt
  ```
- **CSV Output:** Combine with `awk` or `sed`:
  ```bash
  fping -g 10.0.0.0/24 | awk '{print $1","$2}' > status.csv
  ```
- **Cron Jobs:** Use `-q` for summary emails.
  ```bash
  0 * * * * /usr/bin/fping -a -g 10.0.0.0/24 | mail -s "Up hosts" you@domain.com
  ```
