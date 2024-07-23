document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    
    const data = {
        id_number: formData.get('number'),
        first_name: formData.get('firstName'),
        last_name: formData.get('lastName'),
        specialty: formData.get('specialty'),
        contact_number: formData.get('contactNumber'),
        password: formData.get('pswd')
    };
    
    console.log(data);
    
    fetch('https://medsync-production.up.railway.app/signup/doctor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(result => console.log(result))
    .catch(error => console.error('Error:', error));
});
