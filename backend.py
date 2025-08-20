# backend.py
# Flask backend for FactCheck AI using google-genai
# Copy this file, install deps, set GEMINI_API_KEY, then run: python backend.py

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

# Config
GEMINI_API_KEY ="YOUR_GEMINI_API_KEY_HERE"
MODEL_NAME = "gemini-2.5-flash-lite"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/fact-check", methods=["POST"])
def fact_check():
    if not GEMINI_API_KEY:
        return jsonify({"error": "GEMINI_API_KEY env var not set"}), 500

    payload = request.get_json(silent=True) or {}
    claim = (payload.get("claim") or "").strip()
    if not claim:
        return jsonify({"error": "No claim provided"}), 400

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        contents = [
            types.Content(role="user", parts=[types.Part.from_text(text=claim)])
        ]

        # We keep GoogleSearch tool so model can use the web -- remove if you don't want it
        tools = [types.Tool(googleSearch=types.GoogleSearch())]

        # IMPORTANT: do NOT include thinking_config with an unsupported field
        generate_content_config = types.GenerateContentConfig(
            tools=tools,
                    temperature=0,
            system_instruction=[
                types.Part.from_text(
                    text=(
                        "You are a Fact-Checker AI. Analyze the given claim and provide a clear, "
                        "concise explanation of whether it is true, false, partially true/misleading, "
                        "or unverifiable. Always justify with brief reasoning and, when possible, "
                        "mention credible context or evidence. Avoid opinions."
                        "dont use asterics symbol(*) in your response and give a proper framed response"
                        "dont repond withiut srching even if you know the answer, srch and fact check it "
                    )
                )
            ],
        )

        # Non-streaming call (simpler for frontend)
        result = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=generate_content_config,
        )

        # The SDK may put output in different attributes depending on version; try common ones
        explanation = ""
        if hasattr(result, "text") and result.text:
            explanation = result.text
        elif hasattr(result, "content") and result.content:
            # sometimes response object differs; try to join parts if present
            explanation = getattr(result, "content", "")
        else:
            # fallback: str(result)
            explanation = str(result)

        explanation = explanation.strip() if isinstance(explanation, str) else str(explanation)

        return jsonify({"explanation": explanation}), 200

    except Exception as e:
        # Return the exact error so frontend can show it (useful for debugging)
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Starting backend on http://0.0.0.0:{port} (GEMINI_API_KEY set: {'yes' if GEMINI_API_KEY else 'no'})")
    app.run(host="0.0.0.0", port=port, debug=True)
