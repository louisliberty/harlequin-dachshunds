// Harlequin Dachshunds site script
// 1) Phone menu: the "Menu" button opens/closes the navigation.
// 2) Photos that fail to load are hidden instead of showing a broken image.
// 3) Clicking a linked photo opens it larger (like the old site's lightbox).
(function () {
  var nav = document.getElementById('site-navigation');
  var button = nav && nav.querySelector('.menu-toggle');
  var menu = nav && nav.querySelector('ul');
  if (button && menu) {
    if (menu.className.indexOf('nav-menu') === -1) menu.className += ' nav-menu';
    button.addEventListener('click', function (e) {
      e.preventDefault();
      nav.classList.toggle('toggled');
    });
  } else if (button) {
    button.style.display = 'none';
  }

  function hide(img) {
    var box = img.closest('.wp-caption') || img.closest('picture') || img;
    if (box.parentElement && box.parentElement.tagName === 'A') box = box.parentElement;
    box.style.display = 'none';
  }
  document.querySelectorAll('#main img, #secondary img').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0 && img.getAttribute('loading') !== 'lazy') hide(img);
    else img.addEventListener('error', function () { hide(img); });
  });

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a || !/\.(jpe?g|png|gif|webp)$/i.test(a.getAttribute('href') || '')) return;
    e.preventDefault();
    var o = document.createElement('div'); o.className = 'rl-overlay';
    var i = document.createElement('img'); i.src = a.href; i.alt = '';
    o.appendChild(i);
    o.addEventListener('click', function () { o.remove(); });
    document.body.appendChild(o);
  });
})();
