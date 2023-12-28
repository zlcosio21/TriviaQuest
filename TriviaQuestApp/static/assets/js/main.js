document.addEventListener('DOMContentLoaded', function () {
  var input = document.querySelector('input[name="pregunta"]');
  var initialSize = input.size;

  input.addEventListener('input', function () {
    var inputValue = this.value;
    var width = inputValue.length > initialSize ? inputValue.length : initialSize;
    this.style.width = Math.max(width, initialSize) + 'ch';
  });
});

const playAudio = (src) => {
  const audio = new Audio(src);
  audio.play();
};

const progressBar = document.querySelector(".progress-bar"),
  progressText = document.querySelector(".progress-text"),
  selectTime = document.getElementById("time");

let time = parseInt(selectTime.dataset.valor);
let intervalId;

const startQuestion = () => {
  progress(0);
  intervalId = setInterval(() => {
    progress(time);
    time--;

    if (time < 0) {
      clearInterval(intervalId);
    }
  }, 1000);
};

const progress = (value) => {
  const percentage = (value / parseInt(selectTime.dataset.valor)) * 100;
  progressBar.style.width = `${percentage}%`;
  progressText.innerHTML = `${value}s`;
};

startQuestion();

selectTime.addEventListener("change", () => {
  time = parseInt(selectTime.dataset.valor);
  startQuestion();
});