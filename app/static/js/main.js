// Main JavaScript for Email Management System

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    console.log('Email Management System initialized');
    
    // Setup event listeners
    setupFilterButtons();
    setupSearchForm();
}

function setupFilterButtons() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterEmails(this.dataset.filter);
        });
    });
}

function setupSearchForm() {
    const searchForms = document.querySelectorAll('.search-form');
    searchForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Allow default form submission
        });
    });
}

function filterEmails(filterType) {
    const emailItems = document.querySelectorAll('.email-item');
    console.log(`Filtering emails by: ${filterType}`);
    
    // This can be extended to filter emails on the client side
}

function selectAllEmails() {
    const checkboxes = document.querySelectorAll('.email-select');
    const selectAllCheckbox = document.querySelector('.select-all');
    
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });
}

function deleteSelectedEmails() {
    const selectedEmails = document.querySelectorAll('.email-select:checked');
    if (selectedEmails.length === 0) {
        alert('Please select emails to delete');
        return;
    }
    
    if (confirm(`Delete ${selectedEmails.length} email(s)?`)) {
        // Call delete API
        console.log('Deleting emails...');
    }
}

function markAsRead(emailId) {
    console.log(`Marking email ${emailId} as read`);
}

function markAsUnread(emailId) {
    console.log(`Marking email ${emailId} as unread`);
}

function starEmail(emailId) {
    console.log(`Starring email ${emailId}`);
}

function unstarEmail(emailId) {
    console.log(`Unstarring email ${emailId}`);
}

// Toast notification utility
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// API calls
async function apiCall(endpoint, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            }
        };
        
        if (data) {
            options.body = JSON.stringify(data);
        }
        
        const response = await fetch(endpoint, options);
        return await response.json();
    } catch (error) {
        console.error('API call error:', error);
        showNotification('Error: ' + error.message, 'danger');
    }
}
