document.addEventListener('click', event => {
  const element = event.target;
  if (element.className === 'edit') {
    console.log('post edit')
    let textArea = document.createElement('textarea');
    const input = document.createElement('button')
    textArea.value = element.parentNode.textContent
    input.setAttribute("type", "submit")
    input.setAttribute("value", "save_entry")
    input.setAttribute("class", "save")
    input.innerHTML = "Save"
    element.parentElement.append(textArea);
    element.parentNode.appendChild(input)
    document.querySelector(".save").onclick = () => {
     element.parentElement.innerHTML = textArea.value
    }
  }
});

//document.addEventListener('click', event => {
// const element = event.target;
//  if (element.className === 'edit') {
//    console.log('Post edit')
//    let form = document.createElement('form')
  //  form.setAttribute('id', 'edit_form')
//    form.setAttribute('method', 'post')
//    form.setAttribute('data', '{% csrf_token %}')
//    element.parentElement.append(form)
//    let formInput = document.getElementById('edit_form')
//    let input = document.createElement('textArea')
//    let save = document.createElement('button')
//    input.value = element.parentNode.textContent;
//    save.setAttribute('type', 'submit')
//    save.setAttribute('value', 'save_entry')
//    save.setAttribute('name', 'save_entry')
//    save.setAttribute("class", "save")
//    save.innerHTML = 'Save'
//    formInput.appendChild(input)
//    formInput.appendChild(save)
  //  document.querySelector(".save").onclick = () => {
//         element.parentElement.innerHTML = textArea.value
//        }
//    return false
//  }
//})
