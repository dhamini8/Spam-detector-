function checkSpam() {
    const emailContent = document.getElementById('emailContent').value;
    const spamPhrases = document.getElementById('spamPhrases').value.split(',');

    fetch('/check_spam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email_content: emailContent, spam_phrases: spamPhrases }),
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.is_spam) {
            resultDiv.textContent = 'This email is spam.';
            resultDiv.style.color = 'red';
        } else {
            resultDiv.textContent = 'This email is not spam.';
            resultDiv.style.color = 'green';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
