document.addEventListener('DOMContentLoaded', function () {
  var input = document.querySelector('input[name="pregunta"]');
  var initialSize = input.size;

  input.addEventListener('input', function () {
    var inputValue = this.value;
    var width = inputValue.length > initialSize ? inputValue.length : initialSize;
    this.style.width = Math.max(width, initialSize) + 'ch';
  });
});

const progressBar = document.querySelector(".progress-bar"),
  progressText = document.querySelector(".progress-text"),
  selectTime = document.getElementById("time"),
  submitButton = document.querySelector(".btn-quiz-election"),
  hiddenInput = document.querySelector('input[name="opcion_escogida"][value="sin_tiempo"]');

let time = parseInt(selectTime.dataset.valor);
let intervalId;

const startQuestion = () => {
  progress(0);
  intervalId = setInterval(() => {
    progress(time);
    time--;

    if (time === -1) {
      clearInterval(intervalId);
      hiddenInput.checked = true;
      submitButton.click();
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

document.addEventListener("DOMContentLoaded", function() {
  var answerButtons = document.querySelectorAll('.answer.selected');

  answerButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();

      var radioInput = button.querySelector('input[type="radio"]');
      radioInput.checked = true;
    });
  });
});

document.getElementById('enviarBtn').addEventListener('click', function () {
  clearInterval(intervalId);

  var selectedOption = document.querySelector('input[name="opcion_escogida"]:checked');

  if (!selectedOption) {
    document.querySelector('input[name="opcion_escogida"][value="sin_tiempo"]').checked = true;
  }

  var showOptions = document.getElementsByClassName('show-options');
  for (var i = 0; i < showOptions.length; i++) {
    showOptions[i].style.display = 'inline-block';
  }

  var showSubmitButton = document.querySelector('.show-submit-button');
  showSubmitButton.style.display = 'none';

  var submitButton = document.querySelector('.submit-button');
  submitButton.style.display = 'inline-block';

  var optionsToHide = document.getElementsByClassName('options-to-hide');
  for (var i = 0; i < optionsToHide.length; i++) {
    optionsToHide[i].style.display = 'none';
  }
});
