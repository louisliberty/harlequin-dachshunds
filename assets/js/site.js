// 1) Hide photos that haven't been uploaded yet instead of showing a broken image.
// 2) Clicking a linked photo opens it larger (like the old site's lightbox).
(function () {
  function hide(img) {
    var box = img.closest('.wp-caption') || img.closest('a') || img;
    box.style.display = 'none';
  }
  document.querySelectorAll('#main img, #secondary img').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) hide(img);
    else img.addEventListener('error', function () { hide(img); });
  });
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a || !/\.(jpe?g|png|gif)$/i.test(a.getAttribute('href') || '')) return;
    e.preventDefault();
    var o = document.createElement('div'); o.className = 'rl-overlay';
    var i = document.createElement('img'); i.src = a.href; o.appendChild(i);
    o.addEventListener('click', function () { o.remove(); });
    document.body.appendChild(o);
  });
})();
