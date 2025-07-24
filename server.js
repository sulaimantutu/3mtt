// server.js
const express = require("express");
const fetch = require("node-fetch");
const cors = require("cors");
const cors = require("cors");
app.use(cors());


const app = express();
app.use(cors());
app.use(express.json());

app.post("/translate", async (req, res) => {
  const { text, target_lang } = req.body;

  try {
   const res = await fetch("https://libretranslate.de/translate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    q: text,
    source: "auto",
    target: target_lang,
    format: "text"
  })
});


    const data = await response.json();
    res.json({ translated_text: data.translatedText });
  } catch (err) {
    console.error("Translation error:", err);
    res.json({ error: "Translation failed. Please try again later." });
  }
});

app.listen(3000, () => console.log("✅ Server running at http://localhost:3000"));
