document.addEventListener('DOMContentLoaded', () => {
    const newsInput = document.getElementById('newsInput');
    const predictBtn = document.getElementById('predictBtn');
    const loading = document.getElementById('loading');
    const resultSection = document.getElementById('resultSection');
    const statusBadge = document.getElementById('statusBadge');
    const confidenceValue = document.getElementById('confidenceValue');
    const progressBarFill = document.getElementById('progressBarFill');

    predictBtn.addEventListener('click', async () => {
        const text = newsInput.value.trim();
        if (!text) {
            alert('Please enter some news text to analyze.');
            return;
        }

        // Reset and show loading
        loading.classList.remove('hidden');
        resultSection.classList.add('hidden');
        predictBtn.disabled = true;

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Prediction failed');
            }

            const data = await response.json();
            displayResult(data);
        } catch (error) {
            console.error('Error:', error);
            alert('Error analyzing news: ' + error.message);
        } finally {
            loading.classList.add('hidden');
            predictBtn.disabled = false;
        }
    });

    function displayResult(data) {
        resultSection.classList.remove('hidden');
        
        // Update badge
        statusBadge.textContent = (data.result || "N/A").toUpperCase();
        statusBadge.className = 'badge ' + (data.result === 'Real News' ? 'real' : 'fake');
        
        // Update justification
        const justificationText = document.getElementById('justificationText');
        if (justificationText) {
            justificationText.textContent = data.justification || "No justification provided.";
        }
        
        // Update confidence
        let confidencePercent = Math.min(Math.round((data.confidence || 0) * 100), 99);
        if (confidencePercent === 0 && data.confidence !== 0) confidencePercent = Math.round(data.confidence * 100);
        
        confidenceValue.textContent = confidencePercent + '%';
        progressBarFill.style.width = '0%';
        
        setTimeout(() => {
            progressBarFill.style.width = confidencePercent + '%';
        }, 50);

        // Smooth scroll to result
        resultSection.scrollIntoView({ behavior: 'smooth' });
    }
});
