(() => {
  const course = document.querySelector('.course');
  if (!course) return;

  if (navigator.clipboard?.writeText) {
    course.querySelectorAll('pre[data-copy]').forEach((block) => {
      const controls = document.createElement('div');
      controls.className = 'controls';
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = 'Copy';
      button.setAttribute('aria-label', `Copy ${block.dataset.copy}`);
      const status = document.createElement('span');
      status.setAttribute('role', 'status');
      controls.append(button, status);
      block.after(controls);
      button.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(block.textContent.trim());
          status.textContent = 'Copied.';
        } catch {
          status.textContent = 'Clipboard unavailable. Select and copy the text above.';
        }
      });
    });
  }

  const checks = [...course.querySelectorAll('[data-completion]')];
  const meter = course.querySelector('#course-progress');
  if (checks.length && meter) {
    const key = 'claude-aidlc:course-progress:v1';
    const update = (note = '') => {
      const count = checks.filter((check) => check.checked).length;
      meter.textContent = `${count} of ${checks.length} complete.${note}`;
    };
    try {
      const saved = JSON.parse(localStorage.getItem(key) || '[]');
      if (Array.isArray(saved)) checks.forEach((check) => {
        check.checked = saved.includes(check.dataset.completion);
      });
    } catch {
      update(' Saved progress could not be loaded.');
    }
    if (!meter.textContent) update();
    checks.forEach((check) => check.addEventListener('change', () => {
      try {
        localStorage.setItem(key, JSON.stringify(checks.filter((item) => item.checked)
          .map((item) => item.dataset.completion)));
        update();
      } catch {
        update(' Progress cannot be saved in this browser.');
      }
    }));
  }

  const walk = [...course.querySelectorAll('.walk-nav a')];
  if (walk.length) {
    const highlight = () => {
      walk.forEach((link) => {
        if (link.hash === location.hash) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    highlight();
    window.addEventListener('hashchange', highlight);
  }
})();
