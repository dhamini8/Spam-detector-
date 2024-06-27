from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def rabin_karp_search(pattern, text, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    result = []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return result

def is_spam(email_content, spam_phrases):
    for phrase in spam_phrases:
        if rabin_karp_search(phrase, email_content):
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_spam', methods=['POST'])
def check_spam():
    data = request.json
    email_content = data['email_content']
    spam_phrases = data['spam_phrases']
    is_spam_result = is_spam(email_content, spam_phrases)
    return jsonify({"is_spam": is_spam_result})

if __name__ == '__main__':
    app.run(debug=True)
