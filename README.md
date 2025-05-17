
<p align="center">
  <img src="logo.png" alt="Base42-Persian logo" width="300"/>
</p>


## 🚀 Features

✅ Persian letters + Persian digits as alphabet  
✅ Clean and readable output (for Persian users)  
✅ Simple API with `encode` / `decode`  
✅ UTF-8 friendly  
✅ Zero dependencies

---

## 🔤 Alphabet
```

ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی۰۱۲۳۴۵۶۷۸۹

````

---

## 🛠️ Usage

```python
from base42 import base42_encode, base42_decode

msg = "Hey, this is sample text 😅"
encoded = base42_encode(msg)
print(encoded)
decoded = base42_decode(encoded).decode("utf-8")
print(decoded)
````

---

## 📦 Functions

### `base42_encode(data)`

🔹 Accepts string (`str`) or raw `bytes`
🔹 Returns a Base42-encoded Persian string

### `base42_decode(text)`

🔹 Accepts Persian Base42 string
🔹 Returns raw `bytes` (can be `.decode("utf-8")`)

---

## 🤔 Why?

Sometimes you just want your encoded data to **look Persian** —  
for fun, CTF challenges, localized projects, or just to vibe differently 😎

Also, many developers prefer not to use Base64 due to how common and easily recognizable it is.  
**Base42-Persian** can help you obscure your data in a more unique, culturally styled way.

---

## 👨‍💻 Contribute

Pull Requests are welcome 💥
Ideas? Bugs? Open an issue 🎯

---

## 📄 License

MIT — Use it, break it, fix it, improve it ❤️
