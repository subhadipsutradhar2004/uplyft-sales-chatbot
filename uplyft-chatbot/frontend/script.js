async function sendMessage() {
  const input = document.getElementById('user-input');
  const message = input.value;
  appendChat('User', message);

  const response = await fetch('http://localhost:5000/query', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  appendChat('Bot', data.response);
  input.value = '';
}

function appendChat(sender, message) {
  const box = document.getElementById('chat-box');
  const p = document.createElement('p');
  p.textContent = `${sender}: ${message}`;
  box.appendChild(p);
  box.scrollTop = box.scrollHeight;
}

function resetChat() {
  document.getElementById('chat-box').innerHTML = '';
}
