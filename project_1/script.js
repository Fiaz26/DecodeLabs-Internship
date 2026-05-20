document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.querySelector('.submit-btn');
    const blueprintBtn = document.getElementById('blueprint-mode');
    const projectWrapper = document.querySelector('.decode-final-project');

    if(submitBtn) {
        submitBtn.addEventListener('click', () => {
            alert('🚀 Project 01: Deployment Successful!');
        });
    }

    if(blueprintBtn) {
        blueprintBtn.addEventListener('click', () => {
            if (projectWrapper.style.filter === 'grayscale(100%)') {
                projectWrapper.style.filter = 'none';
                blueprintBtn.innerText = 'Toggle Blueprint Mode (Grayscale)';
                blueprintBtn.style.background = 'transparent';
                blueprintBtn.style.color = 'var(--mocha)';
            } else {
                projectWrapper.style.filter = 'grayscale(100%)';
                blueprintBtn.innerText = 'Back to 2025 Aesthetics';
                blueprintBtn.style.background = 'var(--mocha)';
                blueprintBtn.style.color = 'white';
            }
        });
    }
});
