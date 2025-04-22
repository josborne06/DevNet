# 📬 Postman Cheat Sheet – DevNet Lab Edition

## 🧰 Recommended Postman Packages & Add-ons

### 🔌 Postman Packages (Add-ons/Integrations)
- **Newman** – CLI runner for Postman collections (automate tests)
- **Mock Servers** – Simulate endpoints before back-end exists
- **Monitor** – Schedule requests to run and alert on failure
- **Postman Interceptor** – Capture requests from browser
- **GitHub Integration** – Sync collections with repo
- **Slack Integration** – Get alerts on test results

> 📥 Most are available under *Integrations* in the Postman workspace tab

---

## 🛠️ Postman Basics

### 🔧 Use Cases
- Test REST APIs (GET, POST, PUT, DELETE)
- Simulate network automation workflows
- Save and share collections for collaboration

### ✨ Key Features
- **Collections** – Organize API calls by project
- **Environments** – Store variables like base URLs
- **Pre-request Scripts** – Logic before a call
- **Test Scripts** – Validate response codes & bodies

### 🔁 Sample GET Request
```http
GET https://api.publicapis.org/entries
```

### ✅ Basic Test Example
```js
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});
```

### ⌨️ Shortcuts
- Cmd + Enter: Send request
- Cmd + S: Save
- Cmd + E: Environment manager

---

## 🧠 Pro Tips
- Use variables (`{{url}}`, `{{token}}`) in your requests
- Export collections and commit them to GitHub
- Use Monitor + Slack for passive API testing alerts

---

## 📝 Personal Notes
