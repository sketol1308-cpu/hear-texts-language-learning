from flask import Flask, render_template, jsonify, request, Response
from text_generator import TextGenerator
import asyncio
import re
import requests
import json
import os

app = Flask(__name__)
text_generator = TextGenerator()

# AI API configuration (Groq - FREE!)
AI_API_KEY = os.environ.get("GROQ_API_KEY", "")
AI_API_URL = "https://api.groq.com/openai/v1/chat/completions"
AI_MODEL = "llama-3.3-70b-versatile"  # Free and fast!

# Voice options for each language
VOICES = {
    "en": {
        "female": "en-US-JennyNeural",
        "male": "en-US-GuyNeural",
        "teen": "en-US-AnaNeural",
        "british_female": "en-GB-SoniaNeural",
        "british_male": "en-GB-RyanNeural",
        "australian": "en-AU-NatashaNeural",
        "indian": "en-IN-NeerjaNeural",
        "cheerful": "en-US-AriaNeural"
    },
    "fr": {
        "female": "fr-FR-DeniseNeural",
        "male": "fr-FR-HenriNeural",
        "teen": "fr-FR-EloiseNeural",
        "canadian": "fr-CA-SylvieNeural",
        "belgian": "fr-BE-CharlineNeural"
    },
    "de": {
        "female": "de-DE-KatjaNeural",
        "male": "de-DE-ConradNeural",
        "teen": "de-DE-GiselaNeural",
        "austrian": "de-AT-IngridNeural",
        "swiss": "de-CH-LeniNeural"
    }
}

# Expected answers for texts (extracted key information)
ANSWER_KEYS = {
    "English": {
        "beginner": {
            "daily_life": [
                ["anna", "marie", "the girl"],
                ["seven", "7", "seven o'clock"],
                ["toast", "orange juice", "croissants"],
                ["walk", "walks", "on foot"],
                ["max", "dog"]
            ]
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

def generate_with_ai(theme, language, level, word_count):
    """Generate text using Groq AI (FREE!)"""
    if not AI_API_KEY:
        print("No API key set")
        return {"error": "No API key set. Please enter your Groq API key (it's FREE!)."}

    level_styles = {
        "beginner": "Use simple vocabulary and short sentences. Use present tense mostly.",
        "intermediate": "Use varied vocabulary and compound sentences. Mix different tenses.",
        "advanced": "Use sophisticated vocabulary and complex sentences. Use all tenses and idioms."
    }

    # Word count based on level
    level_word_counts = {
        "beginner": 80,
        "intermediate": 150,
        "advanced": 250
    }
    target_words = word_count or level_word_counts.get(level, 100)

    prompt = f"""Generate a {level} level text in {language} about the topic: "{theme}"

REQUIREMENTS:
- Write approximately {target_words} words
- {level_styles.get(level, level_styles['beginner'])}
- Make it interesting and educational
- The text should be a coherent story or description

After the text, provide exactly 5 comprehension questions about the text in {language}.

Format your response exactly like this:
TEXT:
[Your generated text here]

QUESTIONS:
1. [First question]
2. [Second question]
3. [Third question]
4. [Fourth question]
5. [Fifth question]"""

    try:
        headers = {
            "Authorization": f"Bearer {AI_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a language learning assistant that creates educational texts in {language}."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        print(f"Calling Groq API...")
        response = requests.post(AI_API_URL, headers=headers, json=payload, timeout=60)
        print(f"Response status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            print(f"Got content, length: {len(content)}")

            # Parse the response - try multiple formats
            text = ""
            questions = []

            # Try format with TEXT: and QUESTIONS:
            if "TEXT:" in content and "QUESTIONS:" in content:
                parts = content.split("QUESTIONS:")
                text_part = parts[0].replace("TEXT:", "").strip()
                questions_part = parts[1].strip()
                text = text_part
            elif "QUESTIONS:" in content:
                # Sometimes there's no TEXT: label
                parts = content.split("QUESTIONS:")
                text = parts[0].strip()
                questions_part = parts[1].strip()
            else:
                # Try to split by numbered questions
                lines = content.split("\n")
                text_lines = []
                questions_part = ""
                in_questions = False
                for line in lines:
                    if re.match(r'^\d+[\.\)]', line.strip()):
                        in_questions = True
                    if in_questions:
                        questions_part += line + "\n"
                    else:
                        text_lines.append(line)
                text = "\n".join(text_lines).strip()

            # Extract questions
            if questions_part:
                lines = questions_part.split("\n")
                for line in lines:
                    line = line.strip()
                    if line and len(line) > 5:
                        # Remove numbering
                        q = re.sub(r'^[\d]+[\.\)]\s*', '', line)
                        q = q.lstrip('- ')
                        if q and '?' in q:
                            questions.append(q)

            if text and len(questions) >= 1:
                print(f"Success: {len(text.split())} words, {len(questions)} questions")
                return {"text": text, "questions": questions[:5]}
            else:
                print(f"Parse issue, returning raw content")
                # Return raw content as fallback
                return {
                    "text": content,
                    "questions": ["What is the main topic of this text?",
                                  "Can you summarize the key points?",
                                  "What did you learn from this text?"]
                }
        else:
            error_msg = response.text
            print(f"API error: {response.status_code} - {error_msg}")
            return {"error": f"API error: {response.status_code}"}

    except requests.exceptions.Timeout:
        print("API timeout")
        return {"error": "Request timed out. Please try again."}
    except Exception as e:
        print(f"DeepSeek API error: {e}")
        return {"error": str(e)}

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    language = data.get('language', 'English')
    level = data.get('level', 'beginner')
    topic = data.get('topic', '')
    word_count = data.get('word_count', 100)
    use_ai = data.get('use_ai', False)

    # Try AI generation if custom theme is provided
    if use_ai and topic:
        ai_result = generate_with_ai(topic, language, level, word_count)
        if ai_result:
            if "error" in ai_result:
                return jsonify({
                    "text": f"Error: {ai_result['error']}\n\nGet your FREE Groq API key at: https://console.groq.com/keys",
                    "questions": ["Did you enter your API key?", "Is your API key valid?", "Try again?"]
                })
            return jsonify(ai_result)

    # Fallback to predefined texts
    result = text_generator.generate(language, level, topic if topic else 'daily_life', word_count)
    return jsonify(result)

@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    global AI_API_KEY
    data = request.json
    key = data.get('api_key', '')
    # Accept Groq keys (gsk_) or other keys
    if key and '•' not in key and len(key) > 20:
        AI_API_KEY = key.strip()
        print(f"API key set: {key[:10]}...")
        return jsonify({"success": True, "has_key": True})
    elif AI_API_KEY:
        # Key already set, don't overwrite with masked version
        return jsonify({"success": True, "has_key": True})
    return jsonify({"success": False, "has_key": False})

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'en')
    voice_type = data.get('voice_type', 'female')

    if not text:
        return Response(status=400)

    try:
        import edge_tts

        # Get voice for language and type
        voice = VOICES.get(language, VOICES["en"]).get(voice_type, "en-US-JennyNeural")

        async def generate_speech():
            communicate = edge_tts.Communicate(text, voice)
            audio_data = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_data += chunk["data"]
            return audio_data

        audio_data = asyncio.run(generate_speech())

        return Response(
            audio_data,
            mimetype='audio/mpeg',
            headers={'Content-Disposition': 'inline'}
        )
    except Exception as e:
        print(f"TTS error: {e}")
        return Response(status=500)

def extract_answer_from_text(text, question):
    """Extract likely answer from text based on question keywords"""
    text_lower = text.lower()
    question_lower = question.lower()

    # Common question patterns and how to find answers
    patterns = {
        # Name questions
        r"(what is|what's|wie heißt|comment s'appelle|quel est le nom).*(name|nom|name)":
            r"(?:name is|s'appelle|heißt|ich bin|je suis|my name is|called)\s+(\w+)",
        r"(name|nom).*\?":
            r"(?:name is|s'appelle|heißt|ich bin|je suis|my name is|called)\s+(\w+)",

        # Age questions
        r"(how old|quel âge|wie alt)":
            r"(\d+)\s*(?:years? old|ans|jahre)",

        # Time questions
        r"(what time|à quelle heure|um wie viel uhr|when).*(?:wake|lever|aufstehen|get up)":
            r"(?:at|à|um)\s*(\d+(?::\d+)?)\s*(?:o'clock|heures|uhr)?",

        # Food questions
        r"(what|que|was).*(?:eat|mange|isst|breakfast|petit déjeuner|frühstück)":
            r"(?:eat|mange|isst|eating)\s+([\w\s,]+?)(?:\.|,|and|et|und)",

        # Location questions
        r"(where|où|wo).*(?:is|are|est|sont|ist|sind)":
            r"(?:at the|in|à|im|am|dans)\s+([\w\s]+?)(?:\.|,|with)",

        # How questions (transport)
        r"(how|comment|wie).*(?:go|get|va|kommt|travel)":
            r"(?:by|en|mit|walk|marche|zu fuß|on foot)\s*([\w\s]+?)(?:\.|,|because)",

        # What does X do
        r"(what|que|was).*(?:do|does|fait|macht)":
            r"(?:he|she|il|elle|er|sie)\s+([\w\s]+?)(?:\.|,)",
    }

    for q_pattern, a_pattern in patterns.items():
        if re.search(q_pattern, question_lower):
            match = re.search(a_pattern, text_lower)
            if match:
                return match.group(1).strip()

    return None

def check_answer_similarity(user_answer, text, question):
    """Check if user's answer matches information in the text"""
    if not user_answer.strip():
        return {
            "correct": False,
            "feedback": "Please provide an answer.",
            "hint": ""
        }

    user_lower = user_answer.lower().strip()
    text_lower = text.lower()

    # Extract key words from user answer (remove common words)
    stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'it', 'he', 'she', 'they',
                  'le', 'la', 'les', 'un', 'une', 'des', 'est', 'sont', 'il', 'elle',
                  'der', 'die', 'das', 'ein', 'eine', 'ist', 'sind', 'er', 'sie'}

    user_words = [w for w in re.findall(r'\w+', user_lower) if w not in stop_words and len(w) > 2]

    # Check how many key words from the answer appear in the text
    matches = sum(1 for word in user_words if word in text_lower)

    # Try to extract the expected answer from text
    expected = extract_answer_from_text(text, question)

    if len(user_words) == 0:
        return {
            "correct": False,
            "feedback": "Your answer is too short. Please provide more detail.",
            "hint": f"Look for information about: {question}"
        }

    match_ratio = matches / len(user_words) if user_words else 0

    # Check if expected answer words are in user answer
    if expected:
        expected_words = [w for w in re.findall(r'\w+', expected.lower()) if len(w) > 2]
        expected_matches = sum(1 for w in expected_words if w in user_lower)
        expected_ratio = expected_matches / len(expected_words) if expected_words else 0

        if expected_ratio >= 0.5 or match_ratio >= 0.7:
            return {
                "correct": True,
                "feedback": f"Correct! Good job! The answer '{expected}' is found in the text.",
                "hint": ""
            }
        elif expected_ratio > 0 or match_ratio > 0.3:
            return {
                "correct": False,
                "feedback": f"Partially correct. You're on the right track!",
                "hint": f"The text mentions: '{expected}'. Check if this matches your answer."
            }
        else:
            return {
                "correct": False,
                "feedback": "Not quite right. Re-read the text carefully.",
                "hint": f"Hint: Look for '{expected}' in the text."
            }

    # Fallback: check if answer words appear in text
    if match_ratio >= 0.7:
        return {
            "correct": True,
            "feedback": "Your answer contains correct information from the text!",
            "hint": ""
        }
    elif match_ratio >= 0.3:
        return {
            "correct": False,
            "feedback": "Partially correct, but some details may be wrong or missing.",
            "hint": "Read the relevant part of the text again."
        }
    else:
        return {
            "correct": False,
            "feedback": "This doesn't seem to match the text. Try reading it again.",
            "hint": "Focus on finding keywords from the question in the text."
        }

@app.route('/check_answers', methods=['POST'])
def check_answers():
    data = request.json
    user_answers = data.get('answers', [])
    questions = data.get('questions', [])
    text = data.get('text', '')

    results = []
    for i, answer in enumerate(user_answers):
        question = questions[i] if i < len(questions) else ""
        result = check_answer_similarity(answer, text, question)
        results.append({
            "question": question,
            "answer": answer,
            "correct": result["correct"],
            "feedback": result["feedback"],
            "hint": result["hint"]
        })

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
