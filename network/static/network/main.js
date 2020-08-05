document.addEventListener('click', event => {
  const element = event.target;
  if (element.className === 'edit') {
    console.log('post edit')
    postId = element.id
    let textArea = document.createElement('textarea');

    textArea.value = element.parentNode.parentNode.textContent

    element.parentElement.parentElement.appendChild(textArea);
    const input = element.parentNode.children[1]
    input.setAttribute("type", "submit")
    element.setAttribute("type", "hidden")
    document.querySelector(".save").onclick = () => {
      text = textArea.value
      element.parentElement.parentElement.innerHTML = text

     fetch(`post/${postId}/${text}`)
     .then(response => response.json())
     .then(data => {
       console.log(data)
     })
   }
 } else if (element.className === 'likes') {
   console.log('post like')
   postId = element.id
   let count = parseInt(element.parentElement.textContent)
   console.log(count)
   fetch(`like/${postId}/${count}`)
   .then(response => response.json())
   .then(data => {
     console.log(data)
     element.parentElement.textContent = data.new_like_count + ' Likes'
   })
 }
});
