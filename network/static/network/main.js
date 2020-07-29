function editPost() {
  let textArea = document.createElement('textarea')
  textArea.value = document.querySelector('#post-text').innerHTML
  document.querySelector('.post').appendChild(textArea)
}
