document.getElementById("sendButton").addEventListener("click", () => {
    const userText = document.getElementById("userInput").value;
    sendMessage(userText);
    document.getElementById("userInput").value = ''; // 清空输入框
});


function updateChatbox(message, sender) {
    const chatbox = document.getElementById("chatbox");
    const messageElement = document.createElement("p");
    messageElement.style.color = sender === 'You' ? 'blue' : 'black'; // Set color based on sender
    // Convert line breaks in message to <br> tags for HTML
    const formattedMessage = message.replace(/\n/g, '<br>');
    messageElement.innerHTML = `${sender}: ${formattedMessage}`;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the latest message
}


function sendMessage(message) {
    updateChatbox(message, 'You');
    fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender: "user", message: message })
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(response => {
            updateChatbox(response.text, 'Bot');
        });
    })
    .catch(error => console.error('Error sending message:', error));
}
