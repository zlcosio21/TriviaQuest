document.addEventListener('DOMContentLoaded', function () {
  var input = document.querySelector('input[name="pregunta"]');
  var initialSize = input.size;

  input.addEventListener('input', function () {
    var inputValue = this.value;
    var width = inputValue.length > initialSize ? inputValue.length : initialSize;
    this.style.width = Math.max(width, initialSize) + 'ch';
  });
});