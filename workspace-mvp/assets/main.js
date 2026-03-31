/* ==========================================================================
   Agent Prime — Landing Page JavaScript
   Vanilla JS, no dependencies. IIFE-wrapped to avoid global scope pollution.
   ========================================================================== */

(function () {
  'use strict';

  /* --------------------------------------------------------------------------
     1. DARK MODE TOGGLE
     -------------------------------------------------------------------------- */
  (function initDarkMode() {
    var STORAGE_KEY = 'agent-prime-theme';
    var toggle = document.querySelector('.theme-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', function () {
      var html = document.documentElement;
      var current = html.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      try {
        localStorage.setItem(STORAGE_KEY, next);
      } catch (e) {
        // localStorage may be unavailable
      }
      toggle.setAttribute('aria-label',
        next === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
      );
    });
  })();

  /* --------------------------------------------------------------------------
     2. PROGRESS BAR
     -------------------------------------------------------------------------- */
  (function initProgressBar() {
    var bar = document.querySelector('.progress-bar');
    if (!bar) return;

    function updateProgress() {
      var scrollTop = window.scrollY || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = Math.min(progress, 100) + '%';
    }

    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  })();

  /* --------------------------------------------------------------------------
     3. SMOOTH SCROLL
     -------------------------------------------------------------------------- */
  (function initSmoothScroll() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;

      var targetId = link.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (!target) return;

      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });

      // Close mobile nav if open
      var navLinks = document.querySelector('.site-nav__links');
      if (navLinks) navLinks.classList.remove('open');
    });
  })();

  /* --------------------------------------------------------------------------
     4. NAV SCROLL BEHAVIOR
     -------------------------------------------------------------------------- */
  (function initNavScroll() {
    var nav = document.querySelector('.site-nav');
    if (!nav) return;

    function checkScroll() {
      if (window.scrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    }

    window.addEventListener('scroll', checkScroll, { passive: true });
    checkScroll();
  })();

  /* --------------------------------------------------------------------------
     5. SCROLL SPY
     -------------------------------------------------------------------------- */
  (function initScrollSpy() {
    var sections = document.querySelectorAll('main > section[id]');
    var navLinks = document.querySelectorAll('.site-nav__links a[href^="#"]');
    if (!sections.length || !navLinks.length) return;

    var sectionMap = {};
    navLinks.forEach(function (link) {
      var id = link.getAttribute('href').replace('#', '');
      sectionMap[id] = link;
    });

    function updateActive() {
      var scrollPos = window.scrollY + 120; // offset for fixed nav
      var current = '';

      sections.forEach(function (section) {
        if (section.offsetTop <= scrollPos) {
          current = section.id;
        }
      });

      navLinks.forEach(function (link) {
        link.classList.remove('active');
      });

      if (current && sectionMap[current]) {
        sectionMap[current].classList.add('active');
      }
    }

    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();
  })();

  /* --------------------------------------------------------------------------
     6. FADE-IN ON SCROLL
     -------------------------------------------------------------------------- */
  (function initFadeIn() {
    var elements = document.querySelectorAll('.fade-in');
    if (!elements.length) return;

    if (!('IntersectionObserver' in window)) {
      elements.forEach(function (el) {
        el.classList.add('visible');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    });

    elements.forEach(function (el) {
      observer.observe(el);
    });
  })();

  /* --------------------------------------------------------------------------
     8. REVEAL ANIMATIONS (enhanced: stagger, multi-direction)
     -------------------------------------------------------------------------- */
  (function initReveal() {
    var reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;

    if (!('IntersectionObserver' in window)) {
      reveals.forEach(function (el) { el.classList.add('visible'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);

          // Trigger progress bar fills inside this element
          var fills = entry.target.querySelectorAll('.progress-row__fill[data-width]');
          fills.forEach(function (f) {
            setTimeout(function () { f.style.width = f.dataset.width; }, 200);
          });
        }
      });
    }, {
      root: null,
      rootMargin: '0px 0px -60px 0px',
      threshold: 0.1
    });

    reveals.forEach(function (el) { observer.observe(el); });
  })();

  /* --------------------------------------------------------------------------
     9. COUNTER ANIMATION (hero stats)
     -------------------------------------------------------------------------- */
  (function initCounters() {
    var stats = document.querySelector('.hero-stats');
    if (!stats) return;

    function animateCounters() {
      var counters = stats.querySelectorAll('.hero-stat__val[data-count]');
      counters.forEach(function (el) {
        var target = parseInt(el.dataset.count, 10);
        var suffix = el.dataset.suffix || '';
        var duration = 1200;
        var start = performance.now();

        function tick(now) {
          var progress = Math.min((now - start) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
          el.textContent = Math.round(target * eased) + suffix;
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }

    if (!('IntersectionObserver' in window)) {
      animateCounters();
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounters();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    observer.observe(stats);
  })();

  /* --------------------------------------------------------------------------
     7. MOBILE NAV TOGGLE
     -------------------------------------------------------------------------- */
  (function initMobileNav() {
    var toggle = document.querySelector('.nav-toggle');
    var navLinks = document.querySelector('.site-nav__links');
    if (!toggle || !navLinks) return;

    toggle.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      toggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
    });

    // Close nav when clicking outside
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.site-nav') && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation');
      }
    });
  })();

})();
