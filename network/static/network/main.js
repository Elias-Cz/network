document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.edit').forEach(edit => {
    edit.onclick = () => {
      let textArea = document.createElement('textarea');
      document.querySelector('.post-text').replaceWith(textArea);
      return false
    };
  });
});
