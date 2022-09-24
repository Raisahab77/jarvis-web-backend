// console.log("Enter in javascript")
const btn = document.querySelector('.talk');
const content = document.querySelector('.content');


const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.onstart = function(){
    console.log('Voice is activated')
};


recognition.onresult = function(event){
    const current = event.resultIndex;
    const transcript = event.results[current][0].transcript;
    // content.textContent = transcript;
    console.log(transcript);

};
btn.addEventListener('click',()=>{
    console.log("Button clicked");
    recognition.start();
});
console.log("before ajax")
$.ajax({
    url: '{{ url_for('/') }}',
    type: 'POST',
    data: {
        message: transcript
    },
    success: function (response) {
    },
    error: function (response) {
    }
});
console.log("After ajax")

function readOutLoud(message){
    const speech = new SpeechSynthesisUtterance();
    speech.text = message; 
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
}
// no changes