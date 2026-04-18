const sidebarToggle = document.querySelector('[data-sidebar-toggle]');
if (sidebarToggle) {
  sidebarToggle.addEventListener('click', () => {
    document.body.classList.toggle('sidebar-open');
  });
}

document.addEventListener('click', (event) => {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar || !document.body.classList.contains('sidebar-open')) return;
  const clickInsideSidebar = sidebar.contains(event.target);
  const clickToggle = sidebarToggle && sidebarToggle.contains(event.target);
  if (!clickInsideSidebar && !clickToggle) {
    document.body.classList.remove('sidebar-open');
  }
});

const defaultDoc = document.body.getAttribute('data-default-doc');
const renderer = document.querySelector('[data-doc-renderer]');
const mobileTitle = document.querySelector('[data-mobile-title]');
const sidebarTabs = document.querySelector('[data-sidebar-tabs]');
const sidebarNav = document.querySelector('[data-sidebar-nav]');

const stripChapterPrefix = (name) => name.replace(/^[一二三四五六七八九十]+、\s*/, '');
const stripFilePrefix = (name) => name.replace(/^\d+\.\s*/, '');

const TAB_GROUPS = [
  {
    label: '使用指南',
    chapters: ['一、平台接入概览', '二、 电商平台兑换指南', '三、 技术对接规范']
  },
  {
    label: '软件支持',
    chapters: ['四、 软件与客户端集成']
  },
  {
    label: 'API 文档',
    chapters: ['五、 接口参考手册']
  },
  {
    label: '联系我们',
    chapters: ['六、 企业与开发者生态', '七、 技术支持与排错', '八、 联系方式与反馈']
  }
];

let allChapters = [];
let activeTab = '使用指南';
let initialDoc = defaultDoc;

const resolveInitialDoc = () => {
  if (defaultDoc) return defaultDoc;
  return allChapters.flatMap((chapter) => chapter.files).find(Boolean)?.path || '';
};

const findTabForDoc = (docPath) => {
  if (!docPath) return activeTab;
  const chapter = allChapters.find((item) =>
    item.files.some((file) => file.path === docPath)
  );
  if (!chapter) return activeTab;
  return TAB_GROUPS.find((tab) => tab.chapters.includes(chapter.name))?.label || activeTab;
};

const setActiveLink = (docPath) => {
  document.querySelectorAll('[data-doc]').forEach((link) => {
    const isActive = link.getAttribute('data-doc') === docPath;
    link.classList.toggle('active', isActive);
  });
};

const encodeDocPath = (docPath) => {
  const parts = docPath.split('/').map((part, index) => {
    if (index === 0) return part;
    return encodeURIComponent(part);
  });
  return parts.join('/');
};

const normalizeDisplayTitle = (title) => title.replace(/^第[一二三四五六七八九十0-9]+章[:：]\s*/, '');

const createMarkedRenderer = () => {
  const renderer = new marked.Renderer();
  const linkRenderer = renderer.link.bind(renderer);
  renderer.link = ({ href, title, tokens }) => {
    const html = linkRenderer({ href, title, tokens });
    return html.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ');
  };
  return renderer;
};

marked.setOptions({
  gfm: true,
  breaks: false,
  renderer: createMarkedRenderer()
});

const attachCopyButtons = () => {
  renderer.querySelectorAll('pre').forEach((pre) => {
    if (pre.parentElement?.classList.contains('doc-code-block')) return;
    const wrapper = document.createElement('div');
    wrapper.className = 'doc-code-block';
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'doc-copy-button';
    button.textContent = '复制';
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(pre.textContent || '');
        button.textContent = '已复制';
        button.classList.add('copied');
        setTimeout(() => {
          button.textContent = '复制';
          button.classList.remove('copied');
        }, 1200);
      } catch (error) {
        button.textContent = '失败';
        setTimeout(() => {
          button.textContent = '复制';
        }, 1200);
      }
    });
    wrapper.appendChild(button);
  });
};

const loadDoc = async (docPath) => {
  if (!renderer || !docPath) return;
  try {
    const encodedPath = encodeDocPath(docPath);
    const response = await fetch(`${encodedPath}?t=${Date.now()}`);
    if (!response.ok) throw new Error(`Failed to load ${docPath}`);
    const markdown = await response.text();
    renderer.innerHTML = marked.parse(markdown);
    const heading = renderer.querySelector('h1');
    const rawTitle = heading ? heading.textContent.trim() : '文档';
    const title = normalizeDisplayTitle(rawTitle);
    if (heading) heading.textContent = title;
    attachCopyButtons();
    document.title = `${title} - 无限星河 AI 文档`;
    if (mobileTitle) mobileTitle.textContent = title;
    setActiveLink(docPath);
  } catch (error) {
    renderer.innerHTML = `<p>文档加载失败：${docPath}</p>`;
  }
};

const renderSidebarTabs = () => {
  if (!sidebarTabs) return;
  sidebarTabs.innerHTML = TAB_GROUPS.map((tab) => {
    const activeClass = tab.label === activeTab ? 'active' : '';
    return `<button type="button" class="sidebar-tab ${activeClass}" data-tab="${tab.label}">${tab.label}</button>`;
  }).join('');

  sidebarTabs.querySelectorAll('[data-tab]').forEach((button) => {
    button.addEventListener('click', () => {
      activeTab = button.getAttribute('data-tab');
      renderSidebarTabs();
      renderSidebarSections();
    });
  });
};

const renderSidebarSections = () => {
  if (!sidebarNav) return;
  const tabConfig = TAB_GROUPS.find((tab) => tab.label === activeTab);
  const visibleChapters = allChapters.filter((chapter) => tabConfig.chapters.includes(chapter.name));
  sidebarNav.innerHTML = visibleChapters.map((chapter) => {
    const chapterTitle = stripChapterPrefix(chapter.name);
    const filesHtml = chapter.files.length
      ? chapter.files.map((file) => `<a data-doc="${file.path}">${stripFilePrefix(file.name)}</a>`).join('')
      : '<span class="nav-muted">当前目录暂无文件</span>';
    return `<section class="nav-section"><div class="nav-section-title">${chapterTitle}</div><div class="nav-links">${filesHtml}</div></section>`;
  }).join('');

  document.querySelectorAll('[data-doc]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const docPath = link.getAttribute('data-doc');
      loadDoc(docPath);
      document.body.classList.remove('sidebar-open');
    });
  });

  setActiveLink(initialDoc);
};

const renderSidebar = async () => {
  if (!sidebarNav) return;
  try {
    sidebarNav.innerHTML = '<div class="nav-muted">目录加载中...</div>';
    const response = await fetch(`assets/docs-index.json?t=${Date.now()}`);
    allChapters = await response.json();
    initialDoc = resolveInitialDoc();
    activeTab = findTabForDoc(initialDoc);
    renderSidebarTabs();
    renderSidebarSections();
  } catch (error) {
    sidebarNav.innerHTML = '<div class="nav-muted">目录加载失败</div>';
  }
};

(async () => {
  await renderSidebar();
  await loadDoc(initialDoc);
})();
