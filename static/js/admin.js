// Admin Panel JavaScript

// Sidebar Toggle
const sidebarToggle = document.getElementById('sidebarToggle');
const adminBody = document.body;

if (sidebarToggle) {
 sidebarToggle.addEventListener('click', () => {
  adminBody.classList.toggle('sidebar-collapsed');

  // Save state to localStorage
  const isCollapsed = adminBody.classList.contains('sidebar-collapsed');
  localStorage.setItem('sidebarCollapsed', isCollapsed);
 });
}

// Load sidebar state from localStorage
document.addEventListener('DOMContentLoaded', () => {
 const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
 if (isCollapsed) {
  adminBody.classList.add('sidebar-collapsed');
 }
});

// Delete Confirmation Modal
function confirmDelete(url, itemName) {
 const modal = document.getElementById('deleteModal');
 const form = document.getElementById('deleteForm');
 const itemNameSpan = document.getElementById('deleteItemName');

 itemNameSpan.textContent = itemName;
 form.action = url;
 modal.style.display = 'block';
}

function closeModal() {
 const modal = document.getElementById('deleteModal');
 modal.style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function (event) {
 const modal = document.getElementById('deleteModal');
 if (event.target === modal) {
  closeModal();
 }
}

// Toggle Booking Status
function toggleBookingStatus(bookingId, currentStatus) {
 const newStatus = !currentStatus;
 const url = `/admin/bookings/update/${bookingId}/`;

 fetch(url, {
  method: 'POST',
  headers: {
   'Content-Type': 'application/x-www-form-urlencoded',
   'X-CSRFToken': getCookie('csrftoken')
  },
  body: `is_confirmed=${newStatus}`
 })
  .then(response => response.json())
  .then(data => {
   if (data.success) {
    location.reload();
   }
  })
  .catch(error => {
   console.error('Error:', error);
   alert('Error updating booking status');
  });
}

// Get CSRF token
function getCookie(name) {
 let cookieValue = null;
 if (document.cookie && document.cookie !== '') {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
   const cookie = cookies[i].trim();
   if (cookie.substring(0, name.length + 1) === (name + '=')) {
    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    break;
   }
  }
 }
 return cookieValue;
}

// Image Preview for Forms
function previewImage(input, previewId) {
 const preview = document.getElementById(previewId);
 const file = input.files[0];

 if (file) {
  const reader = new FileReader();

  reader.onload = function (e) {
   preview.src = e.target.result;
   preview.style.display = 'block';
  }

  reader.readAsDataURL(file);
 }
}

// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', function () {
 // Auto-dismiss alerts after 5 seconds
 const alerts = document.querySelectorAll('.alert');
 alerts.forEach(alert => {
  setTimeout(() => {
   alert.style.opacity = '0';
   setTimeout(() => {
    if (alert.parentElement) {
     alert.parentElement.removeChild(alert);
    }
   }, 300);
  }, 5000);
 });

 // Add fade-in animation to elements
 const animatedElements = document.querySelectorAll('.stat-card, .dashboard-section');
 animatedElements.forEach((el, index) => {
  el.style.animationDelay = `${index * 0.1}s`;
  el.classList.add('fade-in');
 });
});

// Add some CSS animations
const style = document.createElement('style');
style.textContent = `
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);