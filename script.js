let lastScroll = 0;
const header = document.querySelector('header');
window.addEventListener('scroll', () => {
  const current = window.pageYOffset || document.documentElement.scrollTop;
  if (current > lastScroll) {
    header.classList.add('hide');
  } else {
    header.classList.remove('hide');
  }
  lastScroll = current <= 0 ? 0 : current;
});
