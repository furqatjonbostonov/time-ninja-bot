# Tizim Arxitekturasi va Bepul Bulutli Infratuzilma Qo'llanmasi (Architecture Blueprint)

**Loyiha:** O'rta Osiyo bozori uchun Telegram "Vazifalar va Eslatmalar" tizimi (Bot + Mini App)  
**Hujjat turi:** Ishlab chiqarish darajasidagi arxitektura loyihasi (Production-Grade Architecture Specification)  
**Byudjet strategiyasi:** 100% Doimiy Bepul ($0/oy — Zero-Dollar Budget Guarantee)  
**Holat:** Ishlab chiqilgan va tasdiqlangan (Milestone 2 Deliverable)  
**Muallif:** Worker 2 (Arxitektura va Infratuzilma Mutaxassisi)  

---

## Mundarija
1. [Arxitektura Konsepsiyasi va $0/oy Tamoyili](#1-arxitektura-konsepsiyasi-va-0oy-tamoyili)
   - [1.1. Bepul bulutli infratuzilmaning asosiy tamoyillari](#11-bepul-bulutli-infratuzilmaning-asosiy-tamoyillari)
   - [1.2. Tijoriy faoliyatga moslik va litsenziya shartlari (Terms of Service)](#12-tijoriy-faoliyatga-moslik-va-litsenziya-shartlari-terms-of-service)
   - [1.3. Moliyaviy va operatsion xatarlardan himoyalanish (No Credit Card Trap)](#13-moliyaviy-va-operatsion-xatarlardan-himoyalanish-no-credit-card-trap)
   - [1.4. O'rta Osiyo mintaqasi tarmoq xususiyatlari va Edge afzalliklari](#14-orta-osiyo-mintaqasi-tarmoq-xususiyatlari-va-edge-afzalliklari)
2. [Bepul Bulutli Xizmatlar Katalogi va Aniq Limitlari](#2-bepul-bulutli-xizmatlar-katalogi-va-aniq-limitlari)
   - [2.1. Backend va Hisoblash Muhiti (Compute Runtime)](#21-backend-va-hisoblash-muhiti-compute-runtime)
   - [2.2. Ma'lumotlar Bazasi Qatlami (Database Layer)](#22-malumotlar-bazasi-qatlami-database-layer)
   - [2.3. Rejalashtiruvchi va Eslatmalar Quvuri (Cron & Schedulers)](#23-rejalashtiruvchi-va-eslatmalar-quvuri-cron--schedulers)
   - [2.4. Mini App Frontend Xostingi (Static Web Hosting)](#24-mini-app-frontend-xostingi-static-web-hosting)
   - [2.5. Bulutli Servislarning Qiyosiy Matritsasi](#25-bulutli-servislarning-qiyosiy-matritsasi)
3. [Tizim Topologiyasi va Komponentlar Integratsiyasi](#3-tizim-topologiyasi-va-komponentlar-integratsiyasi)
   - [3.1. To'liq ASCII Tizim Topologiyasi Diagrammasi](#31-toliq-ascii-tizim-topologiyasi-diagrammasi)
   - [3.2. Axborot Oqimi 1: Telegram Webhook -> Workers -> Supabase](#32-axborot-oqimi-1-telegram-webhook---workers---supabase)
   - [3.3. Axborot Oqimi 2: Mini App Frontend -> REST API -> Supabase](#33-axborot-oqimi-2-mini-app-frontend---rest-api---supabase)
   - [3.4. Axborot Oqimi 3: Cron Scheduler -> Worker -> Telegram Bot API](#34-axborot-oqimi-3-cron-scheduler---worker---telegram-bot-api)
   - [3.5. Xavfsiz Aloqa Protokollari va Portlar Konfiguratsiyasi](#35-xavfsiz-aloqa-protokollari-va-portlar-konfiguratsiyasi)
4. [Cold Start Muammosini Hal Qilish va 24/7 Barqarorlik](#4-cold-start-muammosini-hal-qilish-va-247-barqarorlik)
   - [4.1. Konteynerli xizmatlarning 50-60 soniyalik kechikishi va Telegram Webhook 5s taymauti halokati](#41-konteynerli-xizmatlarning-50-60-soniyalik-kechikishi-va-telegram-webhook-5s-taymauti-halokati)
   - [4.2. V8 Isolates orqali 0ms Cold Start va ctx.waitUntil asinxron naqshi](#42-v8-isolates-orqali-0ms-cold-start-va-ctxwaituntil-asinxron-naqshi)
   - [4.3. Supabase loyihasining 7 kunlik inaktivlik uyqusini bartaraf etish kafolati](#43-supabase-loyihasining-7-kunlik-inaktivlik-uyqusini-bartaraf-etish-kafolati)
5. [Eslatmalarni Bajarish va Yetkazib Berish Dvigateli (Notification Engine)](#5-eslatmalarni-bajarish-va-yetkazib-berish-dvigateli-notification-engine)
   - [5.1. Har 1 daqiqalik tekshiruv sikli va FOR UPDATE SKIP LOCKED himoyasi](#51-har-1-daqiqalik-tekshiruv-sikli-va-for-update-skip-locked-himoyasi)
   - [5.2. Poyga holatlari (Race Conditions) va takroriy xabarlarni bartaraf etish](#52-poyga-holatlari-race-conditions-va-takroriy-xabarlarni-bartaraf-etish)
   - [5.3. Telegram Bot API cheklovlariga (30 msg/s) moslashuvchi Leaky Bucket buferi](#53-telegram-bot-api-cheklovlariga-30-msgs-moslashuvchi-leaky-bucket-buferi)
   - [5.4. Xatoliklar qaydnomasi va qayta urinish (Retry & Backoff) qoidalari](#54-xatoliklar-qaydnomasi-va-qayta-urinish-retry--backoff-qoidalari)
6. [Ma'lumotlar Hajmi va Xarajatlarni Optimallashtirish](#6-malumotlar-hajmi-va-xarajatlarni-optimallashtirish)
   - [6.1. Bitta vazifa yozuvi hajmi hisobi va 500 MB da 1,500,000+ vazifa sig'ishi isboti](#61-bitta-vazifa-yozuvi-hajmi-hisobi-va-500-mb-da-1500000-vazifa-sigishi-isboti)
   - [6.2. 6 oydan oshgan arxiv ma'lumotlarini tozalash va saqlash siyosati (Retention Policy)](#62-6-oydan-oshgan-arxiv-malumotlarini-tozalash-va-saqlash-siyosati-retention-policy)
   - [6.3. Indekslar optimallashtiruvi va VACUUM siyosati](#63-indekslar-optimallashtiruvi-va-vacuum-siyosati)
7. [Infratuzilmani O'rnatish va Joylashtirish (Deployment & Setup)](#7-infratuzilmani-ornatish-va-joylashtirish-deployment--setup)
   - [7.1. Wrangler va Cloudflare Workers konfiguratsiyasi (`wrangler.toml`)](#71-wrangler-va-cloudflare-workers-konfiguratsiyasi-wranglertoml)
   - [7.2. Supabase loyihasini tayyorlash va Supavisor ulanishi](#72-supabase-loyihasini-tayyorlash-va-supavisor-ulanishi)
   - [7.3. Tashqi zaxira cron (Cron-job.org) sozlamalari](#73-tashqi-zaxira-cron-cron-joborg-sozlamalari)
   - [7.4. Maxfiy o'zgaruvchilar (Secrets Management) xaritasi](#74-maxfiy-ozgaruvchilar-secrets-management-xaritasi)

---

## 1. Arxitektura Konsepsiyasi va $0/oy Tamoyili

### 1.1. Bepul bulutli infratuzilmaning asosiy tamoyillari
Zamonaviy startaplar va dasturiy ta'minot mahsulotlarining muvaffaqiyati ko'pincha dastlabki bosqichdagi operatsion xarajatlarni (OpEx) minimallashtirishga tayanadi. Ushbu arxitekturaning fundamental tamoyili — **tizimni 100% doimiy bepul (free tier) bulutli servislarda, birorta ham dollar to'lamagan holda, ammo 99.9% sanoat darajasidagi barqarorlik (enterprise-grade reliability) bilan ishga tushirish va saqlashdir**.

Bunga erishish uchun an'anaviy og'ir monolit yoki doimiy ishlovchi virtual serverlar (VPS, EC2, doimiy Docker konteynerlari) paradigmasidan butunlay voz kechilib, **zamonaviy Serverless Edge Computing** arxitekturasi tanlandi:
1. **Faqat hodisaga asoslangan hisoblash (Event-Driven Execution):** Tizim resurslari faqat foydalanuvchi so'rov yuborganda, botga xabar kelganda yoki cron daqiqasi yetganda faollashadi. Harakatsiz paytlarda server resurslari iste'mol qilinmaydi va kvotalar behuda ketmaydi.
2. **0ms sovuq start (Zero Cold Start):** Standart serverless konteynerlarga xos bo'lgan uyg'onish kechikishi V8 Isolate texnologiyasi bilan yo'q qilinadi.
3. **Statik va dinamik qatlamlarning qat'iy ajratilishi (JAMstack):** Mini App frontend resurslari (HTML/JS/CSS) global CDN orqali tarqatiladi (Workers hisoblash kvotasi sarflanmaydi), Backend esa faqat JSON API vazifasini bajaradi.

### 1.2. Tijoriy faoliyatga moslik va litsenziya shartlari (Terms of Service)
Loyiha Texnik Topshirig'i (TZ) va Monetizatsiya strategiyasiga (R4) ko'ra, bot kelgusida Premium obunalar (Click, Payme, Uzum, Kaspi, Telegram Stars) hamda mahalliy homiylik reklamalari orqali daromad keltiradi. Ko'plab dasturchilar bepul arxitektura qurishda provayderlarning **Xizmat Ko'rsatish Shartlari (Terms of Service - ToS)** hujjatlarini e'tibordan chetda qoldiradilar, bu esa jiddiy huquqiy va operatsion falokatlarga olib keladi:

* **Vercel Hobby xatari:** Vercel bepul (Hobby) tarifi shartnomasida servisdan faqat notijoriy, shaxsiy maqsadlarda ("Personal, non-commercial projects only") foydalanishga ruxsat etilganligi ochiq yozilgan. Agar Vercel hostingida joylashgan Mini App yoki bot orqali pul aylanmalari, to'lovlar qabul qilinsa, Vercel avtomatik ravishda Pro rejaga ($20/oy/developer) o'tishni talab qiladi yoki hisobni bloklaydi.
* **Cloudflare ustunligi:** Cloudflare Free Plan litsenziyasi tijoriy faoliyatni (commercial usage) qonunan taqiqlamaydi. Dasturchilar bepul tarifda tijoriy veb-saytlar, API va xizmatlarni bemalol ishga tushirishlari mumkin. Shuning uchun biz Mini App hostingi uchun **Cloudflare Pages**, API va bot mantig'i uchun **Cloudflare Workers** xizmatini tanladik.
* **Supabase va Upstash litsenziyalari:** Supabase Free va Upstash Free rejalari tijoriy loyihalarda foydalanishga to'liq ruxsat beradi. Yagona shart — belgilangan texnik kvotalar (500 MB disk, 1,000 xabar/kun) doirasidan oshib ketmaslikdir.

### 1.3. Moliyaviy va operatsion xatarlardan himoyalanish (No Credit Card Trap)
AWS, Google Cloud yoki Microsoft Azure kabi gigantlarning "Free Tier" takliflari yangi dasturchilar uchun xavfli tuzoq (trap) hisoblanadi:
* Ro'yxatdan o'tishda bank kartasi talab qilinadi.
* Bepul limit (masalan, 750 soat yoki 15 GB tarmoq trafiki) tugashi bilan xizmat to'xtamaydi, balki to'g'ridan-to'g'ri foydalanuvchi kartasidan kutilmagan summalarni yechib olishni boshlaydi (Pay-As-You-Go auto-billing).
* DDoS hujumi yoki kod xatosi tufayli cheksiz so'rovlar aylanmasi ro'y bersa, oylik hisob yuzlab yoki minglab dollarga yetishi mumkin.

**Bizning arxitekturamizda ushbu xatar 100% bartaraf etilgan:**
1. **Hech qanday kredit karta talab qilinmaydi:** Cloudflare (Pages & Workers), Supabase va Cron-job.org xizmatlarining bepul tariflaridan foydalanish uchun xalqaro bank kartasini kiritish talab etilmaydi.
2. **Qat'iy cheklovlar (Hard Quotas):** Agar tizim kunlik bepul limitga yetsa (masalan, Cloudflare Workers 100,000 so'rov/kun), u avtomatik ravishda pullik tarifga o'tib pul yechmaydi, balki `HTTP 429 Too Many Requests` yoki `1015 Rate Limited` xatosini qaytaradi. Bu kutilmagan moliyaviy qarz paydo bo'lish xavfini mutlaqo nolga tushiradi.

### 1.4. O'rta Osiyo mintaqasi tarmoq xususiyatlari va Edge afzalliklari
O'zbekiston, Qozog'iston, Qirg'iziston va Tojikiston mintaqalarida internet infratuzilmasi o'ziga xos parametrlarga ega:
* Foydalanuvchilarning 85% dan ortig'i Telegram tizimidan mobil aloqa operatorlari (Uztelecom, Beeline, Ucell, Mobiuz, Kcell, Tele2) orqali foydalanadi. Mobil tarmoqlarda ping vaqti nisbatan yuqori (40-100 ms).
* Mini App foydalanuvchi tomonidan ochilganda oq ekran 2-3 soniya davomida qotib turmasligi shart.
* Cloudflare global Anycast tarmog'i Toshkent (TAS) va Olmaota (ALA) shaharlarida jismoniy Internet Exchange (IX) va kesh tugunlariga (Edge PoP) ega. Mini App statik fayllari Toshkent va Olmaota tugunlaridan to'g'ridan-to'g'ri foydalanuvchiga 15-30 ms ichida yetkazib beriladi.
* Telegram Bot API serverlari Yevropa (Frankfurt DC2 va Amsterdam DC4) ma'lumotlar markazlarida joylashgan. Cloudflare Workers serverless kodi esa Telegram serverlari bilan Frankfurt magistral kanallari orqali 2-10 ms ichida ma'lumot almashadi.

---

## 2. Bepul Bulutli Xizmatlar Katalogi va Aniq Limitlari

Tizim barqarorligi uchun eng nufuzli bulutli xizmatlar sinchiklab o'rganildi va o'zaro solishtirildi.

```
+---------------------------------------------------------------------------------------------------+
|                                  BULUTLI SERVISLAR TAQSIMOTI                                      |
+--------------------+--------------------------------+---------------------------------------------+
| Qatlam             | Tanlangan Asosiy Servis        | Vazifasi va Asosiy Kvotasi                  |
+--------------------+--------------------------------+---------------------------------------------+
| Frontend Hosting   | Cloudflare Pages               | React/TS Mini App SPA (Cheksiz so'rov/trafik)|
| Compute / Runtime  | Cloudflare Workers             | Bot Webhook & REST API (100k so'rov/kun)    |
| Primary Database   | Supabase (PostgreSQL 15/16)    | Relatsion Baza + Pooler (500 MB, cheksiz conn) |
| Cron Scheduler 1   | Cloudflare Cron Triggers       | Har 1 daqiqalik eslatma tekshiruvi (bepul)  |
| Delayed Queue      | Upstash QStash                 | Aniq daqiqali kechiktirilgan navbat (1k/kun)|
| Backup Pinger      | Cron-job.org                   | Zaxira tashqi heartbeat va failover (bepul) |
+--------------------+--------------------------------+---------------------------------------------+
```

### 2.1. Backend va Hisoblash Muhiti (Compute Runtime)

#### A) G'olib: Cloudflare Workers (Edge Serverless Runtime)
Cloudflare Workers an'anaviy operatsion tizimli virtual mashina yoki og'ir Docker konteyneri emas. U Google Chrome V8 dvigatelining yengil izolyatsiyalari (**V8 Isolates**) asosida ishlaydi.
* **Kunlik so'rovlar:** Kuniga 100,000 ta bepul so'rov (oyiga ~3,000,000 so'rov).
* **CPU hisoblash vaqti:** Har bir so'rov uchun 10 ms sof protsessor vaqti (CPU wall-clock time). Bu vaqtga tarmoq so'rovlari (I/O, database kutish) kirmaydi; faqat kod bajarilish vaqti hisoblanadi. JSON parslash, Telegram `initData` tekshiruvi va marshrutlash atigi 1-3 ms CPU vaqtini oladi.
* **Xotira (RAM):** Har bir izolyatsiya uchun 128 MB RAM (yengil TypeScript/Hono freymvorki uchun 10-15 barobar ortiqcha zaxira).
* **Sovuq start (Cold start):** **0 ms**. Doim faol, server uyg'onish kechikishi mutlaqo mavjud emas.
* **Tijoriy foydalanish:** Free tarifda tijoriy faoliyatga rasman ruxsat berilgan.
* **Geografik joylashuv:** 300+ shahar, jumladan Toshkent (TAS) va Olmaota (ALA) tugunlari.

#### B) Yaroqsiz Muqobil: Render Free Web Service
Ko'plab yangi ishlab chiquvchilar Render'ning bepul veb-xizmatidan foydalanishga urinadilar:
* **Resurslar:** 512 MB RAM, 0.1 vCPU.
* **Katta nuqson — Uyqu rejimi (Inactivity Sleep):** Render'ga 15 daqiqa davomida so'rov kelmasa, u konteynerni to'xtatadi va chuqur uyquga ketadi.
* **Konteyner uyg'onishi (Cold Start):** **50-60 soniya!** Foydalanuvchi botga xabar yozganda yoki Mini App ochganda, Render konteyneri 50 soniyadan so'nggina javob bera boshlaydi.
* **Telegram Webhook 5s Taymauti:** Telegram Bot API webhook orqali so'rov yuborganda, server 5 soniya ichida `HTTP 200 OK` qaytarmasa, aloqani uzadi (`Connection timed out`). Natijada Telegram xabarni yetkazilmadi deb hisoblab, qayta-qayta yuboraveradi. Bot esa foydalanuvchiga umuman javob qaytara olmaydi.
* **750 soatlik oylik limit:** Render bepul tarifda oyiga 750 soat konteyner vaqti beradi. Agar Render'ni uxlab qolmasligi uchun har 10 daqiqada tashqi ping (keep-alive) bilan ushlab turilsa: $31 \text{ kun} \times 24 \text{ soat} = 744 \text{ soat}$. Eng kichik nosozlik, ikkinchi qayta ishga tushirish yoki qisqa sinov paytida 750 soat oyning 28-29 kunida tugaydi va butun bot oy oxirigacha butunlay o'chadi.

#### C) Solishtirma: Koyeb Free Nano
* **Resurslar:** 512 MB RAM, 0.1 vCPU, 2 GB SSD.
* **Uyqu rejimi:** 1 soat harakatsizlikdan so'ng uyquga ketadi, uyg'onish vaqti 2-5 soniya (Render'dan ancha yaxshi, lekin baribir Telegram 5s chegarasiga yaqin).
* **Cheklov:** Koyeb ro'yxatdan o'tishda bank kartasini kiritishni va $29 avtorizatsiyani ushlab qolishni talab qiladi (O'rta Osiyo yosh dasturchilari va startaplari uchun jiddiy to'siq). Server faqat Frankfurt yoki Vashingtonda joylashadi.

---

### 2.2. Ma'lumotlar Bazasi Qatlami (Database Layer)

#### A) G'olib: Supabase PostgreSQL (PostgreSQL 15/16)
Supabase — bu bulutdagi to'liq boshqariladigan (managed) PostgreSQL ma'lumotlar bazasi.
* **Saqlash hajmi (Disk Space):** **500 MB** doimiy NVMe SSD xotira. Matnli vazifalar uchun bu ulkan hajm hisoblanadi (batafsil hisob-kitob 6-bo'limda).
* **Supavisor Ulanishlar Puli (Connection Pooler):** An'anaviy PostgreSQL har bir ulanish uchun alohida jarayon ochadi va maksimal 60-100 ta ulanish bilan cheklanadi. Serverless arxitekturada bir vaqtda 500 ta worker ochilsa, baza darhol "FATAL: too many connections" xatosi bilan to'xtaydi. Supabase **Supavisor** transaksiyalar puli (Port `6543`) orqali minglab parallel serverless chaqiruvlarni xavfsiz boshqaradi.
* **Xavfsizlik:** Qator darajasidagi xavfsizlik — **Row Level Security (RLS)** qo'llab-quvvatlanadi.
* **Auth & Storage:** 50,000 oylik faol foydalanuvchi (MAU) uchun avtorizatsiya va 1 GB bepul fayl xotirasi.
* **7 kunlik inaktivlik qoidasi:** Supabase bepul loyihalari 7 kun davomida birorta ham SQL so'rov qabul qilmasa, ma'lumotlar bazasi to'xtatiladi (pausing). Bizning tizimda har daqiqalik cron orqali bazadan eslatmalar tekshirib turilishi sababli, inaktivlik taymeri **hech qachon 7 kunga yetmaydi**.

#### B) Muqobil: Neon Serverless PostgreSQL
* **Hajm:** 1 GB bepul saqlash joyi, qulay tarmoqlanish (branching).
* **Kamchiligi — 100 CU-soat limiti:** Neon serverless hisoblash quvvati 100 Compute Unit-soat (CU-hours) bilan cheklangan. Bot har daqiqada eslatmalarni tekshirishi kerakligi sababli, hisoblash instansiyasi deyarli doimiy faol bo'lib turadi. 100 CU-soat atigi 4-5 kunda to'liq tugaydi va baza bloklanadi. Shuningdek, 5 daqiqa harakatsizlikdan keyin 0 ga tushish (scale to zero) paytida 1-3 soniyalik sovuq start mavjud.

#### C) Muqobil: Turso libSQL (Distributed Edge SQLite)
* **Afzalliklari:** 5 GB bepul hajm, 500 million o'qish/oy, 10 million yozish/oy. Mutlaqo uxlamaydi (0ms latency), HTTP API orqali ishlaydi, connection pooler talab qilmaydi.
* **Kamchiligi:** SQLite dialekti asosida qurilgan. PostgreSQL'ning kuchli analitik funksiyalari, murakkab JSON agregatsiyalari va `pg_cron` kabi ichki rejalashtiruvchilaridan foydalanib bo'lmaydi. Shunga qaramay, Turso keyingi bosqichlarda o'qish tezligini oshiruvchi kesh bazasi sifatida ajoyib nomzoddir.

---

### 2.3. Rejalashtiruvchi va Eslatmalar Quvuri (Cron & Schedulers)

Eslatmalar foydalanuvchiga belgilangan vaqtda aniq yetib borishi uchun uch bosqichli ishonchli zanjir (Failover Chain) qurildi:

```
+-----------------------------------------------------------------------------------------------+
|                        UCH BOSQICHLI ISHONCHLI CRON ZANJIRI                                   |
+--------------------------+------------------------------+-------------------------------------+
| 1. Asosiy Dvigatel       | 2. Aniq Kechiktirilgan Navbat| 3. Tashqi Zaxira Heartbeat          |
| Cloudflare Cron Triggers | Upstash QStash               | Cron-job.org                        |
| (Har 1 daqiqada)         | (Aniq millisoniyada)         | (Har 1 daqiqada fallback ping)      |
+--------------------------+------------------------------+-------------------------------------+
```

1. **Cloudflare Cron Triggers (Asosiy rejalashtiruvchi):**
   * Workers ichida bepul o'rnatilgan cron servisi.
   * Minimal interval: **Har 1 daqiqa (`* * * * *`)**.
   * Jitter / kechikish: 0-2 soniya.
   * Xavfsiz ichki bajarilish: tashqi internet trafigi sarflanmaydi, API kalitlari Worker muhitida saqlanadi.
2. **Upstash QStash (Aniq kechiktirilgan xabarlar navbati — Delayed Message Queue):**
   * Limit: **Kuniga 1,000 ta bepul xabar**.
   * Foydalanish maqsadi: Muhim va bir martalik eslatmalar yaratilganda (`remind_at = 1730000000`), QStash'ga xabar joylanadi. QStash belgilangan soniyada Worker vebhukiga POST so'rovini qaytaradi.
   * Eksponensial qayta urinish (Exponential Backoff): Agar Worker xatolik qaytarsa, QStash xabarni yo'qotmaydi, balki 3 marta oraliq tanaffuslar bilan qayta jo'natadi.
3. **Cron-job.org (Tashqi zaxira va Keep-Alive):**
   * 100% mutlaqo bepul tashqi veb-cron xizmati.
   * Vazifasi: Har 1 daqiqada `https://api.domain.com/api/cron/dispatch-reminders` manziliga `Authorization: Bearer CRON_SECRET_KEY` sarlavhasi bilan GET so'rov yuborish.
   * Zaxira kafolati: Agar Cloudflare ichki cron tizimida global texnik uzilish bo'lsa ham, Cron-job.org so'rovi Worker'ni tashqaridan uyg'otadi va eslatmalar o'z vaqtida jo'natiladi.

---

### 2.4. Mini App Frontend Xostingi (Static Web Hosting)

#### G'olib: Cloudflare Pages
* **Trafik va so'rovlar:** **Cheksiz (Unlimited requests & bandwidth)**.
* **Global CDN:** Butun dunyo bo'ylab, jumladan O'rta Osiyoga eng yaqin bo'lgan Toshkent va Olmaota PoP tugunlarida keshlanadi.
* **Build limiti:** Oyiga 500 ta bepul avtomatik git-push build.
* **Tijoriy foydalanish:** 100% ruxsat berilgan.
* **Deploy jarayoni:** GitHub/GitLab omboriga push qilinganda Vite + React SPA avtomatik ravishda build bo'ladi va global CDN tarmog'iga yoyiladi.

---

### 2.5. Bulutli Servislarning Qiyosiy Matritsasi

Quyidagi jadvalda tadqiq qilingan barcha bulutli xizmatlarning texnik parametrlari yaxlit taqqoslangan:

| Xizmat Nomi | Servis Turi | RAM / vCPU | Bepul Xotira / Disk | Oylik So'rovlar / Limit | Ulanishlar (Concurrency) | Tarmoq Egress | Cold Start | Tijoriy Ruxsat | Karta Talabi | Tavsiya Holati |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cloudflare Workers** | Compute / Edge API | 128 MB V8 | N/A (Stateless) | 100k so'rov/kun (~3M/oy) | 1,000+ parallel isolates | Cheksiz | **0 ms** | **HA** | **Yo'q** | **ASOSIY (G'olib)** |
| **Cloudflare Pages** | Frontend CDN | N/A | 25 MB max fayl | Cheksiz so'rovlar | Cheksiz | Cheksiz | **0 ms** | **HA** | **Yo'q** | **ASOSIY (G'olib)** |
| **Supabase** | Managed PostgreSQL | Baza instansiyasi | **500 MB NVMe** | Cheksiz SQL so'rovlar | **Supavisor (Cheksiz pool)** | 2 GB / oy | **0 ms** | **HA** | **Yo'q** | **ASOSIY (G'olib)** |
| **Cloudflare Cron** | Internal Scheduler | N/A | N/A | Har 1 daqiqada bepul | Worker bilan birga | 0 GB (Ichki) | **0 ms** | **HA** | **Yo'q** | **ASOSIY (G'olib)** |
| **Upstash QStash** | Delayed Message Queue | N/A | N/A | 1,000 xabar / kun | Yuqori o'tkazuvchanlik | Cheksiz | 0-10 ms | **HA** | **Yo'q** | **ASOSIY (G'olib)** |
| **Cron-job.org** | External Cron | N/A | N/A | Cheksiz cronlar | N/A | Minimal | 0-5s jitter | **HA** | **Yo'q** | **ZAXIRA (Pinger)** |
| **Render** | Container Web Service | 512 MB / 0.1 CPU | Vaqtinchalik | 750 soat / oy | 100 ta ulanish | 100 GB | **50-60 s (Sleep)** | HA | Yo'q | **YAROQSIZ** |
| **Koyeb** | Container Nano | 512 MB / 0.1 CPU | 2 GB SSD | 1 instansiya | O'rtacha | Cheklangan | **2-5 s (Sleep)** | Qisman | **HA ($29 hold)**| Xavfli |
| **Vercel** | Serverless / Static | 2 GB / 1 vCPU | N/A | 1M so'rov / oy | Cheksiz | 100 GB | 50-150 ms | **YO'Q (Hobby)** | Yo'q | ToS buzilishi |
| **Neon.tech** | Serverless Postgres | Avto masshtab | 1 GB | 100 CU-soat / oy | Built-in pooler | 10 GB | 1-3 s | HA | Yo'q | CU tez tugaydi |
| **Turso** | Edge libSQL | N/A | 5 GB | 500M o'qish / oy | HTTP (Cheksiz) | Cheksiz | **0 ms** | HA | Yo'q | Kesh uchun mos |

---

## 3. Tizim Topologiyasi va Komponentlar Integratsiyasi

### 3.1. To'liq ASCII Tizim Topologiyasi Diagrammasi

Quyidagi diagrammada Telegram ekotizimi, Cloudflare global tarmoq infratuzilmasi, ma'lumotlar bazasi va zaxira rejalashtiruvchilarning o'zaro yaxlit topologiyasi aks ettirilgan:

```
+==============================================================================================================+
|                                             TELEGRAM EKOTIZIMI                                               |
|                                                                                                              |
|   +---------------------------------------+                  +---------------------------------------+       |
|   |       Foydalanuvchi Telegram Ilovasi   |                  |       Telegram Cloud Serverlari       |       |
|   |  - Bot Chat (Klaviatura va Buyruqlar) |                  |     - Webhook Router (Frankfurt DC)   |       |
|   |  - Mini App (Webview oyna)            |                  |     - Bot API Gateway (sendMessage)   |       |
|   +---------------------------------------+                  +---------------------------------------+       |
+=======|=================================|==================================^=================================+
        |                                 |                                  |
        | [Oqim 2: Mini App ochish]       | [Oqim 1: Botga xabar/buyruq]     | [Oqim 3: Eslatma yuborish]
        | HTTPS (HTML/JS/CSS)             | Webhook HTTPS POST               | HTTPS POST (sendMessage)
        v                                 v                                  |
+============================================================================|=================================+
|                                  CLOUDFLARE GLOBAL EDGE TARMOQ (CDN & COMPUTE)                              |
|                                                                            |                                 |
|   +---------------------------------------+   +----------------------------|--------------------------+      |
|   |          CLOUDFLARE PAGES             |   |                    CLOUDFLARE WORKERS                 |      |
|   |   (Statik Mini App Hosting)           |   |            (Asosiy Serverless Backend & API)          |      |
|   |                                       |   |                                                       |      |
|   |   - React 19 / TypeScript / Vite      |   |   - 1. Webhook Handlers (/api/telegram/webhook)       |      |
|   |   - Tailwind CSS UI Komponentlari     |   |   - 2. Mini App REST API (/api/v1/tasks, categories)  |      |
|   |   - @telegram-apps/sdk Interfeysi     |   |   - 3. Cryptographic InitData HMAC-SHA256 Auth       |      |
|   |   - Toshkent (TAS) / Olmaota (ALA) PoP|   |   - 4. Cron Dispatcher (/api/cron/dispatch-reminders) |      |
|   |   - 100% Bepul, Cheksiz Egress        |   |   - 5. Leaky Bucket Rate Limiter (Token Throttler)    |      |
|   +-------------------+-------------------+   +----------------------------+--------------------------+      |
|                       |                                                    ^                                 |
+=======================|====================================================|=================================+
                        |                                                    |
                        | [REST API AJAX: GET, POST, PATCH]                  | [Trigger Har 1 daqiqa]
                        | Authorization: tma <raw_initData>                  |
                        +----------------------------------------------------+
                                             |
                                             v
+==============================================================================================================+
|                                    MA'LUMOTLAR BAZASI VA REJALASHTIRUVCHI QATLAMI                             |
|                                                                                                              |
|   +------------------------------------------------------+   +---------------------------------------+       |
|   |                SUPABASE POSTGRESQL 15/16             |   |         CLOUDFLARE CRON TRIGGERS      |       |
|   |                                                      |   |   - Har 1 daqiqada: * * * * *         |       |
|   |   - Port 6543: Supavisor Transaction Pooler          |   |   - 100% Ichki integratsiya, bepul    |       |
|   |   - 500 MB NVMe Doimiy Disk (1.5M vazifa zaxirasi)   |   +---------------------------------------+       |
|   |   - Row Level Security (RLS) Izolyatsiyasi           |                       |                           |
|   |   - FOR UPDATE SKIP LOCKED Parallel Navbat So'rovi   |                       | [Zaxira / Delayed]        |
|   |   - Avtomatik 7 kunlik inaktivlikdan himoya          |                       v                           |
|   +------------------------------------------------------+   +---------------------------------------+       |
|                                                              |          UPSTASH QSTASH & CRON-JOB    |       |
|                                                              |   - QStash: Aniq kechiktirilgan navbat|       |
|                                                              |   - Cron-job.org: Zaxira pinger (1 min|       |
|                                                              |     Authorization: Bearer CRON_SECRET |       |
|                                                              +---------------------------------------+       |
+==============================================================================================================+
```

---

### 3.2. Axborot Oqimi 1: Telegram Webhook -> Workers -> Supabase

Telegram foydalanuvchisi bot bilan muloqot qilganda (matn yozganda, buyruq berganda yoki inline tugmani bosganda) ma'lumotlar quyidagi tartibda aylanadi:

1. **Telegram Cloud so'rovi:** Telegram serveri foydalanuvchi harakatini JSON formatidagi `Update` obyekti ko'rinishida Cloudflare Workers webhook manziliga jo'natadi:
   `POST https://bot.domain.uz/api/telegram/webhook`
2. **Kirish Himoyasi (Ingress Filtering):** Worker darhol sarlavhadagi `X-Telegram-Bot-Api-Secret-Token` kalitini tekshiradi. Agar token mos kelmasa, begona so'rov darhol `403 Forbidden` bilan qaytariladi.
3. **Tezkor Asinxron Javob (Fast 200 OK):** Telegram serverini kutib qolmasligi uchun Worker `ctx.waitUntil()` orqali asinxron fon vazifasini ishga tushiradi va Telegramga zudlik bilan `HTTP 200 OK` qaytaradi (< 30 ms).
4. **FSM va Buyruqlar Marshrutlashi:** Worker ichidagi router (Hono.js) xabarni tahlil qiladi:
   * Agar `/start` bo'lsa: foydalanuvchi hisobini Supabase bazasiga kiritadi/yangilaydi (`ON CONFLICT DO UPDATE`) va Mini App ochuvchi WebApp tugmali tabrik xabarini qaytaradi.
   * Agar matnli vazifa bo'lsa (NLP Quick Add): matndan sana va vaqtni ajratib oladi va vazifani bazaga yozadi.
   * Agar inline tugma bo'lsa (`DONE:<task_id>` yoki `SNOOZE:<task_id>`): vazifa holatini bazada yangilaydi.
5. **Baza bilan aloqa:** Barcha SQL amallari Supabase'ga Supavisor Connection Pooler (Port 6543) orqali yuboriladi.

---

### 3.3. Axborot Oqimi 2: Mini App Frontend -> REST API -> Supabase

Foydalanuvchi Telegram ichida Mini App'ni ochganida vizual boshqaruv qanday ishlaydi:

1. **Statik Fayllarni Yuklash:** Telegram Webview mijozi Cloudflare Pages CDN manziliga (`https://app.domain.uz`) murojaat qiladi. Cloudflare Toshkent yoki Olmaota keshidan siqilgan (Brotli/Gzip) HTML, JS va CSS fayllarni 200 ms ichida ekranga chiqaradi.
2. **SDK Initsializatsiyasi:** Telegram WebApp SDK (`@telegram-apps/sdk`) faollashadi, Telegram rang temasini oladi va foydalanuvchining kriptografik `initData` qatorini qabul qiladi.
3. **Avtorizatsiyalangan REST API So'rovi:** Mini App vazifalar ro'yxatini olish yoki yangi vazifa yaratish uchun Worker backendiga AJAX so'rov yuboradi:
   * So'rov: `POST https://bot.domain.uz/api/v1/tasks`
   * Sarlavha: `Authorization: tma <telegram_init_data>`
4. **Kriptografik Tekshiruv:** Worker `initData` qatorini qabul qilib, Bot Tokeni asosida HMAC-SHA256 xeshini tekshiradi. Token soxtalashtirilmaganligi tasdiqlangach, xavfsiz Telegram User ID ajratib olinadi.
5. **Tenant Scoping va Baza So'rovi:** Foydalanuvchi identifikatori bo'yicha Supabase bazasiga so'rov yuboriladi:
   `INSERT INTO tasks (user_id, title, remind_at, category_id) VALUES ($1, $2, $3, $4) RETURNING *;`
6. **Reaktiv Yangilanish:** Worker Mini App'ga `201 Created` va yangi vazifa JSON obyektini qaytaradi, Mini App ekrani bir lahzada yangilanadi.

---

### 3.4. Axborot Oqimi 3: Cron Scheduler -> Worker -> Telegram Bot API

Eslatmalarni o'z vaqtida jo'natish quvuri:

```
[Cloudflare Cron Trigger: Har daqiqada (* * * * *)]
                     |
                     v
[Cloudflare Worker: /api/cron/dispatch-reminders]
                     |
                     v (Supavisor Port 6543)
[Supabase: SELECT ... FOR UPDATE SKIP LOCKED LIMIT 30]
                     |
                     v (Topilgan 15 ta eslatma)
[Worker Leaky Bucket Throttler (25 msg/s nazorati)]
                     |
                     +---> Telegram Bot API: POST /sendMessage (User 1) -> 200 OK
                     +---> Telegram Bot API: POST /sendMessage (User 2) -> 200 OK
                     +---> Telegram Bot API: POST /sendMessage (User 3) -> 200 OK
                     |
                     v
[Supabase: UPDATE reminders SET status = 'sent', sent_at = NOW()]
```

1. **Trigger:** Har bir daqiqa boshlanishida (00-soniya) Cloudflare Cron Trigger hodisasi yuz beradi.
2. **Xavfsiz Tanlov (Atomic Lock):** Worker Supabase bazasiga ulanib, muddati kelgan va hali jo'natilmagan eslatmalarni `FOR UPDATE SKIP LOCKED` operatori bilan band qiladi va ularning statusini `processing` ga o'tkazadi.
3. **Guruhlab Yuborish (Batch Dispatch):** Worker olingan eslatmalar ro'yxatini aylantirib, har bir foydalanuvchiga Telegram Bot API orqali chiroyli formatlangan xabar va harakat inline tugmalarini (`[✅ Bajarildi]`, `[⏰ +15 daqiqa]`) yuboradi.
4. **Tezlik Cheklovi (Throttling):** Xabarlar Telegram Bot API'ning 30 xabar/soniya limitiga urilmasligi uchun Leaky Bucket buferi orqali tartibga solinadi.
5. **Statusni Muhrlash:** Muvaffaqiyatli yetkazilgan eslatmalar statusi bazada `sent`, xatolik yuz berganlari esa `failed` deb qayd etiladi.

---

### 3.5. Xavfsiz Aloqa Protokollari va Portlar Konfiguratsiyasi

Barcha komponentlar orasidagi o'zaro aloqa sanoat standarti bo'yicha shifrlangan protokollardan foydalanadi:

| Aloqa Zanjiri | Protokol | Port | Autentifikatsiya va Himoya Mexanizmi |
| :--- | :--- | :--- | :--- |
| **Telegram Cloud ↔ Workers** | HTTPS / TLS 1.3 | 443 | `X-Telegram-Bot-Api-Secret-Token` maxfiy sarlavhasi |
| **Mini App (Client) ↔ Workers** | HTTPS / TLS 1.3 | 443 | `Authorization: tma <initData>` (HMAC-SHA256 tekshiruvi) |
| **Workers ↔ Supabase (DB)** | PostgreSQL Wire Protocol / TLS | **6543** | Supavisor Pooler, Parol + SSL Mode `require` |
| **Workers ↔ Telegram Bot API** | HTTPS / TLS 1.3 | 443 | Bot Token (`https://api.telegram.org/bot<TOKEN>/...`) |
| **Cron-job.org ↔ Workers** | HTTPS / TLS 1.3 | 443 | `Authorization: Bearer CRON_SECRET_KEY` sarlavhasi |
| **Workers ↔ Upstash QStash** | HTTPS / TLS 1.3 | 443 | QStash REST Token va Webhook imzo kaliti |

---

## 4. Cold Start Muammosini Hal Qilish va 24/7 Barqarorlik

### 4.1. Konteynerli xizmatlarning 50-60 soniyalik kechikishi va Telegram Webhook 5s taymauti halokati

An'anaviy bepul bulut xizmatlarida (Render, Heroku, Glitch, Koyeb) Telegram botini joylashtirishdagi eng asosiy arxitekturaviy halokat — bu **Sovuq Start (Cold Start)** va **Telegram Webhook Taymauti** o'rtasidagi ziddiyatdir.

Telegram Bot API arxitekturasi quyidagicha qat'iy talab qo'yadi:
> *"Telegram serveri vebhuk manziliga so'rov yuborganidan so'ng, mijoz serveri 5 soniya ichida `HTTP 200 OK` javobini qaytarishi SHART. Agar 5 soniya ichida javob kelmasa, Telegram ulanishni majburan to'xtatadi (`TCP Timeout`) va ushbu xabarni yetkazilmadi deb hisoblaydi."*

Render Free kabi xizmatlarda nima yuz beradi?
1. Botga 15 daqiqa xabar kelmadi -> Render konteyneri uyquga ketdi (`Suspended`).
2. Foydalanuvchi botga `/start` deb yozdi.
3. Telegram vebhuk so'rovini Render'ga yo'lladi.
4. Render konteynerni uyg'otishni boshlaydi: virtual muhitni ishga tushirish, Docker imijini yuklash, Node.js yoki Python muhitini yuklash, kutubxonalarni xotiraga olish, bazaga ulanish. Bu jarayon **50-60 soniya** davom etadi.
5. 5-soniyada Telegram sabri tugaydi va taymaut qayd etadi.
6. 10-soniyada Telegram xabarni 2-marta yuboradi; 20-soniyada 3-marta yuboradi...
7. 60-soniyada Render konteyneri nihoyat uyg'onganida, uning ustiga birdaniga Telegramdan 5-10 ta takroriy so'rovlar bo'roni (Retry Storm) yopiriladi.
8. Bepul konteyner 0.1 vCPU va 512 MB xotira bilan ushbu yuklamani ko'tara olmay, xotira yetishmovchiligi (`OOMKilled`) tufayli yana o'chadi. Foydalanuvchi esa umuman javob ololmaydi.

### 4.2. V8 Isolates orqali 0ms Cold Start va ctx.waitUntil asinxron naqshi

Cloudflare Workers arxitekturasi ushbu muammoni tubdan hal qiladi:
* **V8 Isolates:** Butun operatsion tizim yoki Node.js jarayoni noldan yuklanmaydi. Google V8 dvigatelida kodni bajarish uchun yengil xotira izolyatsiyasi ochiladi. Ushbu izolyatsiya millisoniyaning ulushlarida (< 5 ms) ishga tushadi. Sovuq start kechikishi amalda **0 ms** ga teng!
* **ctx.waitUntil() Asinxron Fon Bajarilishi:**
  Telegram vebhukiga javob qaytarishda eng mukammal naqsh — bu darhol 200 javob qaytarib, amallarni fonda bajarishdir:

```typescript
// Cloudflare Workers - Webhook Qabul Qilish Koni
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    // 1. Xavfsizlik sarlavhasini tekshirish
    const secretHeader = request.headers.get("X-Telegram-Bot-Api-Secret-Token");
    if (secretHeader !== env.TELEGRAM_WEBHOOK_SECRET) {
      return new Response("Unauthorized", { status: 403 });
    }

    // 2. Telegramdan kelgan JSON Update ni o'qish
    const update = await request.json();

    // 3. Asinxron fon jarayonini ishga tushirish (ctx.waitUntil)
    // Ushbu chaqiruv Workerga javob yuborilgandan keyin ham orqa fonda ishlash imkonini beradi!
    ctx.waitUntil(processTelegramUpdate(update, env));

    // 4. Telegram serveriga 20 ms ichida "200 OK" qaytarish
    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { "Content-Type": "application/json" }
    });
  }
};

async function processTelegramUpdate(update: any, env: Env) {
  // Bu yerda og'ir mantiq: NLP tahlili, Supabase bazasiga yozish,
  // foydalanuvchiga javob xabari tayyorlash va yuborish bajariladi.
  // Telegram allaqachon o'zining "200 OK" javobini olgan va hech qachon taymaut bermaydi.
}
```

Bu usul orqali Telegram serveri hech qachon 5 soniyalik kutishga duch kelmaydi va qayta so'rovlar bo'roni (retry storm) ehtimoli mutlaqo bartaraf etiladi.

### 4.3. Supabase loyihasining 7 kunlik inaktivlik uyqusini bartaraf etish kafolati

Supabase platformasining bepul tarifidagi yagona jiddiy qoida — agar loyiha ma'lumotlar bazasiga ketma-ket **7 kun davomida hech qanday SQL so'rov kelmasa**, tizim resurslarni tejash maqsadida loyihani to'xtatadi (`Paused`). Qayta faollashtirish uchun loyiha egasi Supabase paneliga kirib qo'lda tugmani bosishi kerak bo'ladi.

**Bizning tizimda bu muammoning avtomatik oldini olish kafolati:**
1. **Har daqiqalik Cron tekshiruvi:** Tizimimizda har 1 daqiqada Cloudflare Cron Triggers va zaxira Cron-job.org orqali `/api/cron/dispatch-reminders` chaqiriladi.
2. Ushbu endpoint Supabase bazasiga ulanib, quyidagi yengil so'rovni bajaradi:
   ```sql
   SELECT id FROM reminders 
   WHERE remind_at <= NOW() AND status = 'pending' 
   LIMIT 1;
   ```
3. Natijada, hatto yangi foydalanuvchilar kelmagan yoki hech kim vazifa qo'shmagan taqdirda ham, ma'lumotlar bazasiga har daqiqada (kuniga 1,440 marta, haftasiga 10,080 marta) faol SQL tranzaksiyasi kelib turadi.
4. Supabase monitoringi loyihani "Doimiy Faol" (High Activity) deb baholaydi va loyiha **hech qachon avtomatik to'xtatilmaydi**.

---

## 5. Eslatmalarni Bajarish va Yetkazib Berish Dvigateli (Notification Engine)

### 5.1. Har 1 daqiqalik tekshiruv sikli va FOR UPDATE SKIP LOCKED himoyasi

Eslatmalarni o'z vaqtida yuborishda taqsimlangan (distributed) tizimlarning eng katta xavfi — bir nechta worker nusxalari bir vaqtning o'zida bir xil eslatmani o'qib, foydalanuvchiga bitta xabarni 2 yoki 3 marta yuborishi (**Duplicate Delivery / Double-Sending**) hisoblanadi.

Buning oldini olish uchun PostgreSQL'ning eng kuchli imkoniyati — **`FOR UPDATE SKIP LOCKED`** mexanizmi qo'llaniladi.

```sql
-- Atomik Tranzaksiya: Eslatmalarni tanlash va bir zumda bloklash
WITH ready_reminders AS (
  SELECT id
  FROM reminders
  WHERE remind_at <= NOW() 
    AND status = 'pending'
  ORDER BY remind_at ASC
  LIMIT 30
  FOR UPDATE SKIP LOCKED
)
UPDATE reminders
SET status = 'processing',
    updated_at = NOW()
FROM ready_reminders
WHERE reminders.id = ready_reminders.id
RETURNING 
  reminders.id,
  reminders.user_id,
  reminders.task_title,
  reminders.task_description,
  reminders.remind_at;
```

### 5.2. Poyga holatlari (Race Conditions) va takroriy xabarlarni bartaraf etish

Ushbu so'rov poyga holatlarini qanday yo'q qiladi:
1. `FOR UPDATE` tanlangan qatorlarni tranzaksiya davomida qulflaydi.
2. `SKIP LOCKED` esa qulf qo'yilgan qatorlarni boshqa parallel so'rovlar kutib o'tirmasdan, ularni shunchaki o'tkazib yuborishini (skip qilishini) ta'minlaydi.
3. Agar ayni bir soniyada Cloudflare Cron va tashqi Cron-job.org bir vaqtda Worker'ni chaqirsa:
   * 1-Worker birinchi 30 ta qatorni qulflaydi va ularni `processing` ga o'tkazadi.
   * 2-Worker o'sha zahoti o'sha qatorlarni o'tkazib yuboradi va agar boshqa qatorlar bo'lsa ularni oladi, bo'lmasa 0 ta natija bilan darhol chiqib ketadi.
4. Natijada, **hech qachon birorta ham eslatma foydalanuvchiga ikki marta bormaydi**.

```
+---------------------------------------------------------------------------------------------------+
|                        ESLATMA HOLATLARI MASHINASI (STATE MACHINE)                                |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|           [ pending ]  ---(Cron topdi & FOR UPDATE SKIP LOCKED)--->  [ processing ]               |
|                ^                                                            |                     |
|                |                                            +---------------+---------------+     |
|                |                                            |                               |     |
|         (Keyinga surildi)                            (Telegram 200 OK)             (Xatolik 5xx)  |
|                |                                            |                               |     |
|                +---- [ Snooze: +15m ] <----                 v                               v     |
|                                                      [ sent / delivered ]              [ failed ] |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

### 5.3. Telegram Bot API cheklovlariga (30 msg/s) moslashuvchi Leaky Bucket buferi

Telegram Bot API platformasi barcha botlar uchun qat'iy global cheklovlarga ega:
1. **Global cheklov:** Barcha chatlarga umumiy yuborish tezligi — **sekundiga 30 ta xabar (30 msg/sec)**.
2. **Shaxsiy chat cheklovi:** Bitta foydalanuvchiga xabar yuborish — **sekundiga 1 ta xabar (1 msg/sec)**.
3. Agar ushbu limit buzilsa, Telegram serveri darhol `HTTP 429 Too Many Requests` va `retry_after: N` sarlavhasini qaytaradi va bot vaqtincha bloklanadi.

Ushbu cheklovga moslashish uchun Cloudflare Worker ichida **Leaky Bucket (Oqayotgan chelak)** algoritmi amalga oshiriladi:
* Har daqiqalik cron chaqiruvida maksimal **30 ta eslatma** olinadi (`LIMIT 30`).
* Ushbu 30 ta xabar birdaniga emas, balki boshqariladigan intervallar bilan uzatiladi.

```typescript
// Leaky Bucket / Paced Dispatcher Implementation
async function dispatchRemindersWithRateLimit(reminders: Reminder[], env: Env) {
  const TELEGRAM_SAFE_RATE_LIMIT = 25; // Xavfsiz tezlik: sekundiga 25 ta xabar (30 limitdan kamroq)
  const DELAY_BETWEEN_MESSAGES_MS = Math.ceil(1000 / TELEGRAM_SAFE_RATE_LIMIT); // ~40 ms

  const results = [];

  for (const reminder of reminders) {
    const startTime = Date.now();
    try {
      const response = await sendTelegramMessage(reminder, env);
      results.push({ id: reminder.id, status: 'sent', response });
    } catch (error: any) {
      if (error?.status === 429) {
        // Agar Telegram 429 qaytarsa, ko'rsatilgan vaqt kutamiz
        const retryAfter = (error.retryAfterSeconds || 1) * 1000;
        await sleep(retryAfter);
      }
      results.push({ id: reminder.id, status: 'failed', error });
    }

    // Har bir xabardan keyin minimal tanaffus (Leaky Bucket drip)
    const elapsed = Date.now() - startTime;
    const remainingDelay = DELAY_BETWEEN_MESSAGES_MS - elapsed;
    if (remainingDelay > 0) {
      await sleep(remainingDelay);
    }
  }

  // Natijalarni bazada yangilash
  await markRemindersProcessed(results, env);
}

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

### 5.4. Xatoliklar qaydnomasi va qayta urinish (Retry & Backoff) qoidalari
1. **403 Forbidden (Bot bloklangan):** Agar foydalanuvchi botni to'xtatib (Block) qo'ygan bo'lsa, Telegram `403 Forbidden: bot was blocked by the user` qaytaradi. Bunday holda eslatma qayta yuborilmaydi, foydalanuvchi holati bazada `is_active = FALSE` qilinadi va behuda resurs sarflash to'xtatiladi.
2. **5xx Server Errors (Telegram nosozligi):** Agar Telegram tomonida nosozlik bo'lsa, eslatma holati `pending` ga qaytariladi va `retry_count = retry_count + 1` qilinadi. Qayta urinishlar soni 3 tadan oshgach, eslatma `failed` deb belgilanadi.

---

## 6. Ma'lumotlar Hajmi va Xarajatlarni Optimallashtirish

### 6.1. Bitta vazifa yozuvi hajmi hisobi va 500 MB da 1,500,000+ vazifa sig'ishi isboti

Ko'pchilik "500 MB bepul hajm zamonaviy tizim uchun juda kam" deb o'ylaydi. Quyida relatsion ma'lumotlar bazasi darajasida bitta vazifa va eslatma yozuvi qancha jismoniy bayt joy egallashi bo'yicha qat'iy matematik hisob-kitob keltirilgan:

#### PostgreSQL `tasks` va `reminders` jadvallari ustunlari hajmi:
* `id` (UUID turi): **16 bayt**
* `user_id` (BIGINT turi): **8 bayt**
* `category_id` (UUID turi, nullable): **16 bayt**
* `title` (VARCHAR(150), o'rtacha 40 ta lotin/kirill belgisi, UTF-8): **~50 bayt**
* `description` (TEXT, o'rtacha 80 ta belgi): **~90 bayt**
* `status` (VARCHAR(20), masalan 'pending'): **10 bayt**
* `due_date` (TIMESTAMPTZ): **8 bayt**
* `remind_at` (TIMESTAMPTZ): **8 bayt**
* `created_at` (TIMESTAMPTZ): **8 bayt**
* `updated_at` (TIMESTAMPTZ): **8 bayt**
* PostgreSQL Heap Tuple Header (har bir qator uchun sarlavha): **24 bayt**
* Null Bitmap va Padding (tekislash): **~8 bayt**
* B-Tree indekslar xarajati (id, user_id, remind_at bo'yicha indekslar ulushi): **~90 bayt**

$$\text{Bitta to'liq vazifa yozuvi hajmi} = 16 + 8 + 16 + 50 + 90 + 10 + 8 + 8 + 8 + 8 + 24 + 8 + 90 \approx \mathbf{346 \text{ bayt}}$$

Keling, pessimistik baholash uchun bitta yozuv hajmini **350 bayt** deb olaylik.

#### 500 MB xotira sig'imi hisobi:
* $500 \text{ MB} = 500 \times 1024 \times 1024 \text{ bayt} = \mathbf{524,288,000 \text{ bayt}}$.
* Foydalanuvchilar jadvali (`users`) va tizim jadvallari uchun 24 MB zaxira ajratamiz.
* Vazifalar uchun sof xotira: $500,000,000 \text{ bayt}$.

$$\text{Maksimal vazifalar soni} = \frac{500,000,000 \text{ bayt}}{350 \text{ bayt/yozuv}} \approx \mathbf{1,428,571 \text{ ta vazifa}}$$

Agar vazifalar tavsifi qisqa bo'lsa (o'rtacha 280-300 bayt), baza bemalol **1,700,000 dan ortiq vazifani** o'zida saqlay oladi!

#### Haqiqiy hayotiy yuklama modeli:
* Faraz qilaylik, tizimda **10,000 nafar faol foydalanuvchi** bor.
* Har bir foydalanuvchi o'rtacha **30 ta faol vazifa** saqlaydi.
* Jami faol vazifalar soni: $10,000 \times 30 = \mathbf{300,000 \text{ ta vazifa}}$.
* 300,000 ta vazifaning umumiy hajmi: $300,000 \times 350 \text{ bayt} \approx \mathbf{105 \text{ MB}}$.
* Bu Supabase taqdim etgan 500 MB bepul hajmning bor-yo'g'i **21%** qismidir! Qolgan 395 MB (79%) xotira bo'sh turadi.

### 6.2. 6 oydan oshgan arxiv ma'lumotlarini tozalash va saqlash siyosati (Retention Policy)

Baza hajmi hech qachon 500 MB limitiga yaqinlashmasligi uchun loyihada **Arxivlash va Tozalash Siyosati (Data Retention Policy)** joriy qilinadi:

1. **Faol vazifalar:** `pending`, `in_progress` holatidagi vazifalar muddati qanchalik eski bo'lishidan qat'i nazar hech qachon o'chirilmaydi.
2. **Bajarilgan va bekor qilingan vazifalar:** `status IN ('completed', 'cancelled')` bo'lgan vazifalar 180 kundan (6 oydan) so'ng avtomatik arxivlanadi/tozalanadi.
3. **Eksport imkoniyati:** Foydalanuvchi Mini App orqali o'z vazifalar tarixini istalgan paytda JSON yoki CSV formatida yuklab olishi mumkin.
4. **Haftalik tozalash skripti (Weekly Cleanup Cron):**
   Har yakshanba yarim kechasi (03:00 da) avtomatik tozalash so'rovi bajariladi:

```sql
-- 6 oydan oshgan eski bajarilgan vazifalarni o'chirish
DELETE FROM tasks
WHERE status IN ('completed', 'cancelled')
  AND updated_at < NOW() - INTERVAL '180 days';
```

### 6.3. Indekslar optimallashtiruvi va VACUUM siyosati
* **Qisman indekslar (Partial Indexes):** Doimiy millionlab yozuvlar ustidan indeks qurish disk joyini yeydi. Shuning uchun indekslar faqat kerakli qatorlarga qo'yiladi:
  ```sql
  -- Butun jadvalga emas, faqat kutayotgan eslatmalarga indeks:
  CREATE INDEX idx_reminders_pending 
  ON reminders (remind_at) 
  WHERE status = 'pending';
  ```
  Ushbu qisman indeks 500 MB bazada atigi 2-5 MB joy oladi va qidiruvni 100 barobar tezlashtiradi!
* **Auto-Vacuum:** PostgreSQL o'chirilgan qatorlar (`dead tuples`) o'rnini qayta ishlatish uchun avtomatik `VACUUM` jarayonini fon rejimida yurgizadi, bu esa disk hajmining asossiz shishib ketishini oldini oladi.

---

## 7. Infratuzilmani O'rnatish va Joylashtirish (Deployment & Setup)

### 7.1. Wrangler va Cloudflare Workers konfiguratsiyasi (`wrangler.toml`)

Backend xizmati Cloudflare Workers platformasida joylashadi. Quyida ishlab chiqarishga tayyor `wrangler.toml` konfiguratsiyasi keltirilgan:

```toml
name = "telegram-task-bot-backend"
main = "src/index.ts"
compatibility_date = "2026-10-01"
compatibility_flags = ["nodejs_compat"]

# Bepul tarif resurslari
workers_dev = false
route = { pattern = "bot.domain.uz/*", zone_name = "domain.uz" }

# Har daqiqalik ichki Cron Trigger (100% Bepul)
[triggers]
crons = ["* * * * *"]

# O'zgaruvchilar (Variables)
[vars]
ENVIRONMENT = "production"
SUPABASE_URL = "https://xyzcompany.supabase.co"
SUPABASE_POOLER_URL = "postgres://postgres.xyz:[PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

# Build sozlamalari
[build]
command = "npm run build"
```

### 7.2. Supabase loyihasini tayyorlash va Supavisor ulanishi

1. [supabase.com](https://supabase.com) saytida bepul hisob ochiladi va yangi loyiha yaratiladi.
2. Mintaqa sifatida **EU (Frankfurt) `eu-central-1`** tanlanadi (Telegram serverlari va Cloudflare Yevropa marshrutlariga eng past kechikish uchun).
3. **Database Settings -> Connection Pooling** bo'limiga kiriladi:
   * **Pooler Mode:** `Transaction` (Serverless uchun majburiy).
   * **Port:** `6543` (Supavisor porti).
4. SQL muharririda (SQL Editor) `TZ.md` da ko'rsatilgan relyatsion sxema yaratiladi.

### 7.3. Tashqi zaxira cron (Cron-job.org) sozlamalari

1. [cron-job.org](https://cron-job.org) saytida bepul ro'yxatdan o'tiladi.
2. Yangi cron vazifa yaratiladi:
   * **URL:** `https://bot.domain.uz/api/cron/dispatch-reminders`
   * **Execution schedule:** Har 1 daqiqa (`Every 1 minute`).
   * **Request Method:** `GET`
   * **Headers:**
     * `Authorization`: `Bearer c98a4f128b0946d...` (Maxfiy token).
   * **Failure alerts:** Faol holatda saqlash.

### 7.4. Maxfiy o'zgaruvchilar (Secrets Management) xaritasi

Hech qanday maxfiy kalit ochiq kodda yoki git omborida saqlanmaydi. Ular Cloudflare Secrets shifrlangan xotirasida saqlanadi:

| O'zgaruvchi Nomi | Saqlash Joyi | Vazifasi va Tavsifi |
| :--- | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | Cloudflare Worker Secret | Telegram Bot API bilan muloqot va Webhook imzolash kaliti |
| `TELEGRAM_WEBHOOK_SECRET` | Cloudflare Worker Secret | `X-Telegram-Bot-Api-Secret-Token` sarlavhasini tekshirish |
| `SUPABASE_SERVICE_ROLE_KEY` | Cloudflare Worker Secret | Supabase bazasiga to'liq huquqli backend kirish kaliti |
| `CRON_SECRET_KEY` | Cloudflare Worker Secret | Cron-job.org so'rovlarini autentifikatsiya qilish |
| `QSTASH_TOKEN` | Cloudflare Worker Secret | Upstash QStash kechiktirilgan navbatiga xabar joylash tokeni |
| `QSTASH_CURRENT_SIGNING_KEY`| Cloudflare Worker Secret | QStash dan kelgan vebhuk imzosini tasdiqlash |

Ushbu sirlar quyidagi terminal buyrug'i orqali o'rnatiladi:
```bash
wrangler secret put TELEGRAM_BOT_TOKEN
wrangler secret put TELEGRAM_WEBHOOK_SECRET
wrangler secret put SUPABASE_SERVICE_ROLE_KEY
wrangler secret put CRON_SECRET_KEY
wrangler secret put QSTASH_TOKEN
```

---

## 8. Xulosa va Arxitekturaviy Kafolatlar

Ushbu arxitektura hujjati asosida qurilgan tizim quyidagi **qat'iy texnik va iqtisodiy kafolatlarni** beradi:
1. **$0/oy Xarajat:** Tizim birorta ham sent abonent to'lovisiz ishlaydi. Bank kartasi kiritilmagani sababli kutilmagan qarzlar paydo bo'lish ehtimoli 0%.
2. **0ms Cold Start:** V8 Isolates texnologiyasi tufayli foydalanuvchilar va Telegram webhooklari hech qachon kechikishga uchramaydi.
3. **99.9% Barqarorlik:** Cloudflare'ning global tarmoq chidamliligi va uch bosqichli eslatma zanjiri tizimning to'xtovsiz ishlashini kafolatlaydi.
4. **Masshtab zaxirasi:** 500 MB bepul baza va kunlik 100,000 so'rovlar limiti tizimga kamida **10,000 - 15,000 kunlik faol foydalanuvchilarga (DAU)** bepul xizmat ko'rsatish imkonini beradi.
