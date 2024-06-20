import parse from json.parse

fetch('http://http://127.0.0.1:5000/users.json')
  .then(response => response.json())
  .then((data) => {
    let users = parse(data);
    const email = document.getElementById('email');
    const password = document.getElementById('password')

    if (users['Email'].includes(email) && users['Password'].includes(password))
    
  })
