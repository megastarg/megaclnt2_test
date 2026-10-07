document.addEventListener('DOMContentLoaded', () => {
    
    // Fetch and populate categories on load
    fetch('/api/categories')
        .then(response => response.json())
        .then(categories => {
            const dataList = document.getElementById('category-options');
            categories.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat;
                dataList.appendChild(option);
            });
        })
        .catch(err => console.error("Error loading categories", err));

    // Form Submission
    const form = document.getElementById('add-link-form');
    const submitBtn = document.getElementById('submit-btn');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // UI loading state
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        const payload = {
            category: document.getElementById('category').value,
            filename: document.getElementById('filename').value,
            url: document.getElementById('url').value,
            force: document.getElementById('force').checked,
            notassured: document.getElementById('notassured').checked
        };

        fetch('/api/add-link', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(data => {
            if(data.success) {
                showToast(data.message, 'success');
                // Clear URL and filename inputs but keep category and switches for rapid entry
                document.getElementById('filename').value = '';
                document.getElementById('url').value = '';
                document.getElementById('filename').focus();
            } else {
                showToast(data.error || "An error occurred", 'error');
            }
        })
        .catch(err => {
            showToast("Failed to connect to the server.", 'error');
        })
        .finally(() => {
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        });
    });

    // Toast logic
    function showToast(message, type = 'success') {
        const container = document.getElementById('toast-container');
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        // Icon based on type
        const icon = type === 'success' 
            ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`
            : `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>`;

        toast.innerHTML = `${icon} <span>${message}</span>`;
        container.appendChild(toast);

        // Animate in
        setTimeout(() => toast.classList.add('show'), 10);

        // Animate out and remove
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 4000);
    }
});
