var chatbox = document.getElementById("chatbox");
var message = document.getElementById("message");
var send = document.getElementById("send");
send.addEventListener("click", function() {
    sendMessage();
});
message.addEventListener("keydown", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        send.click();
    }
});
function sendMessage() {
    var userMessage = message.value;
    var userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerHTML = "<strong>You:</strong> " + userMessage;
    chatbox.appendChild(userDiv);
    message.value = "";
    fetch("/get_response?message=" + encodeURIComponent(userMessage))
    .then(function(response) { return response.text(); })
    .then(function(botMessage) {
        var botDiv = document.createElement("div");
        botDiv.className = "message bot";
        botDiv.innerHTML = "<strong>Assistant:</strong> " + botMessage;
        chatbox.appendChild(botDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}