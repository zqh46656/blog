document.addEventListener('DOMContentLoaded', function () {
  var overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.innerHTML = '<span class="lightbox-close">&times;</span><img class="lightbox-img" src="" alt="">';
  document.body.appendChild(overlay);

  var overlayImg = overlay.querySelector('.lightbox-img');
  var closeBtn = overlay.querySelector('.lightbox-close');

  var scale = 1;
  var posX = 0, posY = 0;
  var isDragging = false;
  var startX = 0, startY = 0;

  function applyTransform() {
    overlayImg.style.transform =
      'translate(' + posX + 'px, ' + posY + 'px) scale(' + scale + ')';
  }

  function resetLightbox() {
    overlay.classList.remove('active');
    overlayImg.src = '';
    scale = 1;
    posX = 0;
    posY = 0;
    applyTransform();
  }

  document.querySelectorAll('article img').forEach(function (img) {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', function (e) {
      e.preventDefault();
      overlayImg.src = img.src;
      overlayImg.alt = img.alt;
      scale = 1;
      posX = 0;
      posY = 0;
      applyTransform();
      overlay.classList.add('active');
    });
  });

  // 滚轮缩放
  overlay.addEventListener('wheel', function (e) {
    e.preventDefault();
    if (e.deltaY < 0) {
      scale += 0.1;
    } else {
      scale -= 0.1;
    }
    if (scale < 0.2) scale = 0.2;
    if (scale > 8) scale = 8;
    applyTransform();
  }, { passive: false });

  // 拖动
  overlayImg.addEventListener('mousedown', function (e) {
    e.preventDefault();
    isDragging = true;
    startX = e.clientX - posX;
    startY = e.clientY - posY;
    overlayImg.style.cursor = 'grabbing';
  });

  document.addEventListener('mousemove', function (e) {
    if (!isDragging) return;
    posX = e.clientX - startX;
    posY = e.clientY - startY;
    applyTransform();
  });

  document.addEventListener('mouseup', function () {
    isDragging = false;
    overlayImg.style.cursor = 'grab';
  });

  // 点击背景或关闭按钮
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay || e.target === closeBtn) {
      resetLightbox();
    }
  });

  // ESC 关闭
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('active')) {
      resetLightbox();
    }
  });
});



// 目录跳转：按链接文字匹配 h2
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('article a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var linkText = this.textContent.trim();
      var headings = document.querySelectorAll('article h2');
      for (var i = 0; i < headings.length; i++) {
        var h = headings[i];
        var hClone = h.cloneNode(true);
        hClone.querySelectorAll('a.anchor').forEach(function (a) { a.remove(); });
        var hText = hClone.textContent.trim();
        if (hText === linkText || hText.indexOf(linkText) === 0) {
          e.preventDefault();
          h.scrollIntoView({ behavior: 'smooth', block: 'start' });
          return;
        }
      }
    });
  });
});