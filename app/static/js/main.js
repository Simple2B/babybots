// custom javascript
document.addEventListener('DOMContentLoaded', (evt) => {
  const checkboxes = document.querySelectorAll('.checkbox');

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', (evt) => {
      const wrapper = checkbox.parentNode;
      const bindedInput = wrapper.previousElementSibling.querySelector('input');

      if (checkbox.checked) {
        bindedInput.setAttribute('readonly', true);
      } else {
        bindedInput.removeAttribute('readonly');
      }
    });
  })

  async function reloadStatus() {
    const response = await fetch('/get_status')
    const divStatus = document.querySelector('.timer_status-text')

    const data = await response.json();
    // console.log(data);

    if (data) {
      return divStatus.innerText = 'Running'
    } else {
      return divStatus.innerText = 'Down'
    }
  }

  setInterval(reloadStatus, 3000);


  function sendTimeToServer() {
    const time = new Date();
    const hours = time.getHours();
    console.log(hours)
    const hiddenTagValue = document.getElementById('hidden_tag').value = hours;
    console.log(hiddenTagValue);
    return hiddenTagValue;
  };

  sendTimeToServer();
});