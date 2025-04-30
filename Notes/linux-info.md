# Linux Cheat Sheet 

A concise reference for common Linux commands, keyboard shortcuts, and tasks. Perfect for quick look-ups in your terminal or GitHub.

---

## 📂 File & Directory Management

| Command                          | Description                                      | Example                                     |
|----------------------------------|--------------------------------------------------|---------------------------------------------|
| `ls -lah`                        | List files (all, human-readable sizes)           | `ls -lah /var/log`                          |
| `cd <dir>`                       | Change directory                                 | `cd /etc/netbox`                            |
| `pwd`                            | Print working directory                          | `pwd`                                       |
| `mkdir -p <path>`                | Create directory (with parents)                  | `mkdir -p ~/projects/scripts`               |
| `rm -rf <path>`                  | Remove files or directories recursively          | `rm -rf /tmp/test`                          |
| `cp -r <src> <dst>`              | Copy files/directories recursively               | `cp -r ~/scripts ~/backup/scripts`          |
| `mv <src> <dst>`                 | Move or rename files/directories                 | `mv old.conf new.conf`                      |
| `find <path> -name '<pattern>'`  | Find files by name                               | `find . -name '*.cfg'`                      |

---

## 📦 Package Management (Distro-Specific)

### Debian/Ubuntu (APT)

```bash
sudo apt update                    # Refresh package index
sudo apt upgrade                   # Upgrade installed packages
sudo apt install <pkg>             # Install package
sudo apt remove <pkg>              # Remove package
sudo apt autoremove                # Remove orphaned dependencies
```

### RHEL/CentOS (YUM/DNF)

```bash
sudo yum update                    # Update all packages
sudo yum install <pkg>             # Install package
sudo yum remove <pkg>              # Remove package
sudo dnf upgrade                   # DNF alternative to update
```

---

## 🖥️ System Monitoring & Processes

| Command                           | Description                                     | Example                                    |
|-----------------------------------|-------------------------------------------------|--------------------------------------------|
| `top`                             | Real-time process viewer                        | `top`                                      |
| `htop`                            | Enhanced process viewer (interactive)           | `htop`                                     |
| `ps aux | grep <pattern>`    | Search for running processes                    | `ps aux | grep sshd`                  |
| `kill <PID>` / `kill -9 <PID>`    | Terminate process (9=force)                    | `kill 1234`                                |
| `free -h`                         | Show memory usage (human-readable)              | `free -h`                                  |
| `df -h`                           | Show disk usage (human-readable)                | `df -h /`                                  |
| `du -sh <path>`                   | Show directory size summary                     | `du -sh /var/log`                          |
| `uptime`                          | System uptime and load averages                 | `uptime`                                   |

---

## 🌐 Networking & Connectivity

| Command                                 | Description                                   | Example                                     |
|-----------------------------------------|-----------------------------------------------|---------------------------------------------|
| `ip addr show` / `ifconfig`             | Display network interfaces                    | `ip addr show eth0`                         |
| `ip route` / `route -n`                 | Show routing table                            | `ip route`                                  |
| `ping <host>`                           | Send ICMP echo requests                       | `ping 8.8.8.8`                              |
| `traceroute <host>`                     | Trace network route                           | `traceroute github.com`                     |
| `ss -tuln` / `netstat -tuln`            | List listening ports and connections          | `ss -tuln`                                  |
| `curl -I <URL>`                         | Fetch HTTP headers                            | `curl -I https://example.com`               |
| `wget <URL>`                            | Download files                                | `wget https://example.com/file.tar.gz`      |
| `ssh user@host`                         | SSH into remote host                          | `ssh admin@192.168.1.100`                   |
| `scp src user@host:dst`                 | Secure copy to/from remote host               | `scp file.txt admin@host:/tmp/`             |
| `rsync -avz src/ dst/`                  | Sync files/directories efficiently            | `rsync -avz ~/scripts/ backup/scripts/`     |

---

## 🔒 Permissions & Ownership Explained

Linux permissions determine who can read, write, or execute files. There are three classes:

- **Owner (u):** The user who owns the file.
- **Group (g):** The group assigned to the file.
- **Others (o):** Everyone else.

Permissions are represented symbolically (`rwx`) or numerically (0-7):

| Symbolic | Numeric | Meaning                            |
|----------|---------|------------------------------------|
| `rwx`    | `7`     | Read, write, execute               |
| `rw-`    | `6`     | Read, write                        |
| `r-x`    | `5`     | Read, execute                      |
| `r--`    | `4`     | Read-only                          |
| `--x`    | `1`     | Execute-only                       |
| `---`    | `0`     | No permissions                     |

### Common Commands
```bash
chmod 755 <file>          # rwxr-xr-x
chmod 644 <file>          # rw-r--r--
chmod -R 700 <dir>        # rwx------ recursively
chown user:group <file>   # Change owner and group
chown -R user:group <dir> # Recursively change ownership
```

### Special Bits
- **Setuid (s):** Runs executable as file owner.
- **Setgid (s):** Runs executable as file group or new files inherit group.
- **Sticky (t):** On directories, only file owners can delete their files (e.g., `/tmp`).

```bash
chmod u+s <file>          # Setuid bit
chmod g+s <dir>           # Setgid directory
chmod +t <dir>            # Sticky bit
``` 

---

## ⌨️ Keyboard Shortcuts (Bash)

| Shortcut            | Action                                                                 |
|---------------------|------------------------------------------------------------------------|
| `Ctrl + A`          | Move cursor to beginning of line                                       |
| `Ctrl + E`          | Move cursor to end of line                                             |
| `Alt + B`           | Move cursor backward one word                                          |
| `Alt + F`           | Move cursor forward one word                                           |
| `Ctrl + U`          | Delete from cursor to line start                                       |
| `Ctrl + K`          | Delete from cursor to line end                                         |
| `Ctrl + W`          | Delete the word before the cursor                                      |
| `Ctrl + Y`          | Paste text from clipboard (yank)                                        |
| `Ctrl + R`          | Reverse search command history                                         |
| `!!`                | Repeat last command                                                    |
| `!$`                | Last argument of previous command                                      |
| `Tab`               | Autocomplete file/command names                                        |

---

## 📝 Text Processing & Logs

| Command                             | Description                                 | Example                                     |
|-------------------------------------|---------------------------------------------|---------------------------------------------|
| `grep '<pattern>' <file>`           | Search text in files                        | `grep 'ERROR' /var/log/syslog`             |
| `grep -R '<pattern>' <dir>`         | Recursive grep                              | `grep -R 'access denied' /etc/`            |
| `awk '{print $1,$5}' <file>`        | Pattern scanning and processing             | `awk '{print $1,$5}' /var/log/auth.log`     |
| `sed 's/old/new/g' <file>`          | Stream editor (find & replace)              | `sed 's/foo/bar/g' config.yml`              |
| `tail -f <file>`                    | Follow file (real-time)                     | `tail -f /var/log/nginx/access.log`         |
| `less <file>`                       | View file (scrollable)                      | `less /etc/passwd`                          |

---

## ⏱️ Scheduling & Job Control

```bash
crontab -l                           # List cron jobs
crontab -e                           # Edit cron jobs
systemctl restart <service>          # Restart a systemd service
systemctl status <service>           # Check service status
service <name> start|stop|status     # SysV init alternative
```

---

## 📚 Tips & Best Practices

- **Use aliases** for frequent commands in `~/.bashrc`:
  ```bash
  alias ll='ls -lah'
  alias gs='git status'
  ```
- **Protect critical files** by setting immutable bit:
  ```bash
  sudo chattr +i /etc/passwd
  ```
- **Enable bash-completion** for faster navigation:
  ```bash
  sudo apt install bash-completion
  source /etc/bash_completion
  ```
- **Secure SSH** by disabling root login and using key-based auth:
  ```bash
  PermitRootLogin no
  PasswordAuthentication no
  ```

---

*Enjoy this cheat sheet? Star ⭐ it on GitHub and send feedback!*

