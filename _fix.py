# -*- coding: utf-8 -*-
with open('index_final_sakura_curved_float.html','r',encoding='utf-8') as f:
    s = f.read()

old = '''  <div class="container">
    <div class="card">
      <div class="avatar-wrap">
        <div class="avatar-ring"></div>
        <div class="avatar">
          <img src="https://cdn.discordapp.com/avatars/1004917748264087665/archived/152084706283959'''

new_block = '''  <div class="container">
    <div class="card">
      <div class="avatar-wrap">
        <div class="avatar-ring"></div>
        <div class="avatar">
          <img src="https://cdn.discordapp.com/avatars/1004917748264087665/archived/1520847062839595079/b750fc414bdbeb1fe871604ff82428ce.webp?size=2048" alt="avatar" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
          <span class="avatar-fallback">忍</span>
        </div>
        <img class="avatar-decor" src="https://cdn.discordapp.com/media/v1/collectibles-shop/1228251144065777765/animated" alt="decoration" onerror="this.style.display='none';">
        <span class="status-dot" id="statusDot" aria-label="Discord status"></span>
      </div>

      <h1 class="name" id="nameTitle">
        <span id="typedTitle"></span><span class="cursor">|</span>
        <span class="kanji">こ ん に ち は</span>
      </h1>
      <p class="tagline" id="tagline"><span class="tagline-text">Doing nothing.. *mlem mlem*</span><span class="tagline-cursor">|</span></p>

      <div class="activity-card" id="activityCard">
        <img class="ac-art" id="acArt" alt="" style="display:none;">
        <div class="ac-art-placeholder" id="acArtPh" aria-hidden="true">&#127801;</div>
        <div class="ac-info">
          <div class="ac-type" id="acType">Doing nothing..</div>
          <div class="ac-title" id="acTitle">Stay hydrated, &#273;&#7915;ng code bug n&#7919;a</div>
          <div class="ac-sub" id="acSub">V&#7851;n s&#7889;ng, v&#7851;n chill</div>
        </div>
        <div class="ac-bars" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
      </div>

      <div class="divider"></div>
      <div class="badges"><span class="badge">Learning code</span><span class="badge">Gamer</span></div>
      <div class="links">
        <a class="link-btn" href="javascript:void(0)" data-copy="https://discord.com/users/1004917748264087665" data-label="Discord">
          <span class="sweep-mask"><span class="sweep"></span></span>
          <span class="icon"><svg viewBox="0 0 24 24"><path d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4447.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785-.037 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0943.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0105c3.9278 1.7933 8.18 1.7933 12.0614 0a.0739.0739 0 01.0785.0095c.1202.0991.246.1981.3728.2924a.077.077 0 01-.0066.1276 12.2986 12.2986 0 01-1.873.8914.0766.0766 0 00-.0407.1067c.3604.698.7719 1.3628 1.225 1.9932a.076.076 0 00.0842.0286c1.961-.6067 3.9495-1.5219 6.0023-3.0294a.077.077 0 00.0313-.0552c.5004-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0 00-.0312-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 2.1569-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.946 2.4189-2.1568 2.4189Z"/></svg></span>
          <span class="copy-tip">Copy Discord</span>
        </a>
        <a class="link-btn" href="javascript:void(0)" data-copy="https://www.youtube.com/watch?v=QDia3e12czc" data-label="YouTube">
          <span class="sweep-mask"><span class="sweep"></span></span>
          <span class="icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm-2.5 14.5v-9l7 4.5-7 4.5z"/></svg></span>
          <span class="copy-tip">Copy YouTube</span>
        </a>
      </div>
    </div>
  </div>

<script>'''

print('OLD found:', old in s)
if old in s:
    s = s.replace(old, new_block, 1)
    with open('index_final_sakura_curved_float.html','w',encoding='utf-8') as f:
        f.write(s)
    print('Replaced successfully.')
else:
    print('Old block not found - check file content')