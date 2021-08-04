// custom javascript
document.addEventListener('DOMContentLoaded', (evt) => {
  const checkboxes = document.querySelectorAll('.checkbox');

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', (evt) => {
      const wrapper = checkbox.parentNode;
      const bindedInput = wrapper.previousElementSibling.querySelector('input');

      if (checkbox.checked){
        bindedInput.setAttribute('readonly', true);
      } else {
        bindedInput.removeAttribute('readonly');
      }
    });
  })
});


function reloadStatus() {
  const response = await fetch('/get_status')

  return response.json()
  .then(data => console.log(data))
}