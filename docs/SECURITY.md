# Telegram Task & Reminder Bot + Mini App — Kiberxavfsizlik, Kriptografiya va Axborot Himoyasi Spetsifikatsiyasi (SECURITY.md)

**Loyiha**: Telegram Task & Reminder Bot + Mini App (O'rta Osiyo bozori)  
**Hujjat turi**: Ishlab chiqarish darajasidagi Kiberxavfsizlik Spetsifikatsiyasi (Production-Grade Security Specification)  
**Holati**: Tasdiqlangan / Ishlab chiqarishga tayyor (Production-Ready)  
**Versiya**: 1.0.0  
**Muallif**: Xavfsizlik Arxitekturasi Mutaxassisi (Worker 3 — Security Documentation Specialist)  

---

## Mundarija

1. [Kiberxavfsizlik Arxitekturasi va Zero-Trust Modeli](#1-kiberxavfsizlik-arxitekturasi-va-zero-trust-modeli)
   - [1.1 Zero-Trust (Nol Ishonch) Falsafasi](#11-zero-trust-nol-ishonch-falsafasi)
   - [1.2 Mijoz Tomoni (Client-side / Webview) Ishonchsizligi](#12-mijoz-tomoni-client-side--webview-ishonchsizligi)
   - [1.3 Ko'p Qatlamli Himoya (Defense in Depth) Topologiyasi](#13-kop-qatlamli-himoya-defense-in-depth-topologiyasi)
2. [Telegram Web App InitData Kriptografik Validatsiyasi](#2-telegram-web-app-initdata-kriptografik-validatsiyasi)
   - [2.1 Tahdid Modeli va initData Tuzilishi](#21-tahdid-modeli-va-initdata-tuzilishi)
   - [2.2 Matematik va Kriptografik Validatsiya Modeli](#22-matematik-va-kriptografik-validatsiya-modeli)
   - [2.3 Timing Attack (Vaqt Bo'yicha Hujumlar) dan Himoyalanish](#23-timing-attack-vaqt-boyicha-hujumlar-dan-himoyalanish)
   - [2.4 Replay Attack (Takroriy Hujumlar) dan Himoya va auth_date Chegaralari](#24-replay-attack-takroriy-hujumlar-dan-himoya-va-auth_date-chegaralari)
   - [2.5 Sessiya Arxitekturasi: Stateless JWT Handshake](#25-sessiya-arxitekturasi-stateless-jwt-handshake)
   - [2.6 Ishlab Chiqarish Darajasidagi Reference Kod Namunalari (TypeScript va Python)](#26-ishlab-chiqarish-darajasidagi-reference-kod-namunalari-typescript-va-python)
3. [Telegram Bot Webhook Himoyasi va Ingress Xavfsizligi](#3-telegram-bot-webhook-himoyasi-va-ingress-xavfsizligi)
   - [3.1 Maxfiy Token Sarlavhasi (X-Telegram-Bot-Api-Secret-Token)](#31-maxfiy-token-sarlavhasi-x-telegram-bot-api-secret-token)
   - [3.2 Telegram Rasmiy Serverlarining IP CIDR Diapazonlarini Tekshirish](#32-telegram-rasmiy-serverlarining-ip-cidr-diapazonlarini-tekshirish)
   - [3.3 Retry Storm Oldini Olish va Asinxron Qayta Ishlash](#33-retry-storm-oldini-olish-va-asinxron-qayta-ishlash)
4. [DDoS Hujumlariga Qarshi Himoya va Cheklovlar (Rate Limiting)](#4-ddos-hujumlariga-qarshi-himoya-va-cheklovlar-rate-limiting)
   - [4.1 Cloudflare Free Edge WAF Qoidalari](#41-cloudflare-free-edge-waf-qoidalari)
   - [4.2 Ilova Darajasidagi Differensial Token Bucket Algoritmi](#42-ilova-darajasidagi-differensial-token-bucket-algoritmi)
   - [4.3 Outbound Leaky Bucket: Telegram Serverlariga Xabar Yuborish Cheklovlari](#43-outbound-leaky-bucket-telegram-serverlariga-xabar-yuborish-cheklovlari)
5. [Ruxsatsiz Kirish (Anti-IDOR) va Ma'lumotlar Izolyatsiyasi](#5-ruxsatsiz-kirish-anti-idor-va-malumotlar-izolyatsiyasi)
   - [5.1 IDOR Zaifligi va Butun Sonli ID lardan Voz Kechish](#51-idor-zaifligi-va-butun-sonli-id-lardan-voz-kechish)
   - [5.2 Autentifikatsiya Kontekstiga Qat'iy Bog'lash](#52-autentifikatsiya-kontekstiga-qatiy-boglash)
   - [5.3 Har Bir SQL So'rovida Qat'iy Ijarachi Izolyatsiyasi](#53-har-bir-sql-sorovida-qatiy-ijarachi-izolyatsiyasi)
   - [5.4 Supabase PostgreSQL Row Level Security (RLS) Siyosatlari](#54-supabase-postgresql-row-level-security-rls-siyosatlari)
6. [Shaxsiy Ma'lumotlar Maxfiyligi va Qonuniy Talablar](#6-shaxsiy-malumotlar-maxfiyligi-va-qonuniy-talablar)
   - [6.1 O'zbekiston Respublikasi "Shaxsga doir ma'lumotlar to'g'risida"gi Qonuni (O'RQ-547)](#61-ozbekiston-respublikasi-shaxsga-doir-malumotlar-togrisidagi-qonuni-orq-547)
   - [6.2 Xalqaro GDPR Standartlariga Muvofiqlik](#62-xalqaro-gdpr-standartlariga-muvofiqlik)
   - [6.3 Tranzitdagi va Tinch Holatdagi Ma'lumotlarni Shifrlash (TLS 1.3 & At-Rest)](#63-tranzitdagi-va-tinch-holatdagi-malumotlarni-shifrlash-tls-13--at-rest)
   - [6.4 Maxfiy Kalitlar va Muhit O'zgaruvchilari Xavfsizligi](#64-maxfiy-kalitlar-va-muhit-ozgaruvchilari-xavfsizligi)
7. [Xavfsizlik Auditi va Ishlab Chiqarish Nazorat Ro'yxati (Pre-flight Checklist)](#7-xavfsizlik-auditi-va-ishlab-chiqarish-nazorat-royxati-pre-flight-checklist)

---

# 1. Kiberxavfsizlik Arxitekturasi va Zero-Trust Modeli

## 1.1 Zero-Trust (Nol Ishonch) Falsafasi

Zamonaviy bulutli va gibrid taqsimlangan ilovalarda an'anaviy perimetr xavfsizligi ("ichki tarmoq ishonchli, tashqi tarmoq xavfli") paradigmasi to'liq eskirgan. Mazkur loyiha — **Telegram Task & Reminder Bot + Mini App** — mutlaq **Zero-Trust (Nol Ishonch: "Hech qachon ishonma, doimo tekshir — Never Trust, Always Verify")** tamoyiliga tayanadi.

Tizimda har bir kiruvchi so'rov, xabar, webhook va API chaqiruv quyidagi qoidalarga bo'ysunadi:
1. **Identifikatsiyani uzluksiz tasdiqlash**: Har bir operatsiya kontekstida sub'ektning haqiqiyligi qat'iy kriptografik dalillar bilan tasdiqlanishi shart.
2. **Minimal huquqlar (Least Privilege)**: Tizim komponentlari, rollari va ma'lumotlar bazasi ulanishlari faqat o'z vazifasini bajarish uchun zarur bo'lgan minimal huquqlar doirasida ishlaydi.
3. **Buzilish taxmini (Assume Breach)**: Har bir quyi tizim boshqa tizimlar buzilgan bo'lishi mumkinligi ehtimolini inobatga olgan holda loyihalashtiriladi.

## 1.2 Mijoz Tomoni (Client-side / Webview) Ishonchsizligi

Telegram Mini App (TMA) foydalanuvchining smartfoni yoki kompyuteridagi Telegram mijozi ichida joylashgan brauzer konteyneri — **In-App Webview** (iOS WKWebView, Android WebView, Telegram Desktop Chromium Webview) orqali ishga tushadi.

### Kiberxavfsizlik Qoidasi: Mijoz Muhiti Mutlaqo Dushman Muhit Hisoblanadi (Client Environment is Untrusted & Hostile)

1. **Foydalanuvchi va Tajovuzkor To'liq Nazoratga Ega**:
   - Tajovuzkor Webview ichida brauzer konsolini ochishi (DevTools), har qanday JavaScript kodini yuborishi, global obyektlarni (masalan, `window.Telegram.WebApp`) o'zgartirishi, prototip ifloslanishi (Prototype Pollution) keltirib chiqarishi yoki xotiradagi o'zgaruvchilarni tahrirlashi mumkin.
   - Tajovuzkor tarmoq trafigini oraliq proksi (Burp Suite, OWASP ZAP, Charles Proxy) orqali ushlab qolib, HTTP sarlavhalari va so'rov tanasini (Body) o'zgartira oladi.
2. **Hech Qanday Mijoz Tekshiruviga Ishonmaslik**:
   - Mini App interfeysidagi shakllar (form validation), rol tekshiruvlari (`user.isAdmin === true`), filtrlar faqat foydalanuvchi qulayligi (UX) uchun xizmat qiladi.
   - Barcha biznes mantig'i, avtorizatsiya, ruxsatlar va hisob-kitoblar **faqat backend (Edge Worker API) darajasida** mustaqil qayta tekshiriladi.
3. **Maxfiy Kalitlar Mijozga Chiqarilmaydi**:
   - `TELEGRAM_BOT_TOKEN`, ma'lumotlar bazasi `service_role` kaliti, to'lov tizimlari (`Click SECRET_KEY`, `Payme MERCHANT_KEY`) hech qachon mijoz kodiga (HTML/JS/Bundle) tushmasligi shart.

---

## 1.3 Ko'p Qatlamli Himoya (Defense in Depth) Topologiyasi

Tizim xavfsizligi bitta devor bilan cheklanmaydi; hujumchi bitta to'siqni yorib o'tgan taqdirda ham, keyingi qatlamlar hujumni to'xtatadi. Quyidagi sxemada 5 qatlamli himoya arxitekturasi keltirilgan:

```
+----------------------------------------------------------------------------------------------------+
|                                      DEFENSE IN DEPTH TOPOLOGIYASI                                 |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|    [ Foydalanuvchi / Mini App (Webview) ]               [ Telegram Cloud Serverlari (Webhook) ]    |
|                      |                                                     |                       |
|                      v (HTTPS / TLS 1.3)                                   v (HTTPS / TLS 1.3)     |
|   +--------------------------------------------------------------------------------------------+   |
|   | 1-QATLAM: Chegara Himoyasi (Cloudflare Free Edge WAF)                                      |   |
|   | - L3/L4 volumetrik DDoS bostirish (Avtomatik global anycast scrubbing)                     |   |
|   | - WAF Custom Rules (Bot Fight Mode, Country / Threat Score filtrlash)                      |   |
|   | - Webhook Secret Token va Telegram IP CIDR tekshiruvi                                      |   |
|   | - Edge Rate Limiting: 100 so'rov / 10 soniya / IP manzil                                   |   |
|   | - Mini App statik aktivlari uchun Immutable Caching (Asl server yukini 95% kamaytirish)    |   |
|   +--------------------------------------------------------------------------------------------+   |
|                      |                                                     |                       |
|                      v                                                     v                       |
|   +-----------------------------------------+       +------------------------------------------+   |
|   | 2-QATLAM: Mini App Auth Gateway         |       | 2-QATLAM: Webhook Ingress Controller     |   |
|   | - HMAC-SHA256 initData validatsiyasi    |       | - X-Telegram-Bot-Api-Secret-Token qat'iy |   |
|   | - Timing attack himoyasi                |       |   tengligi tekshiruvi                    |   |
|   | - Replay Attack himoyasi (auth_date)    |       | - update_id deduplikatsiyasi (SETNX)     |   |
|   | - Qisqa muddatli Stateless JWT berish   |       | - Darhol 200 OK (<50ms) qaytarish        |   |
|   +-----------------------------------------+       +------------------------------------------+   |
|                      |                                                     |                       |
|                      v                                                     v                       |
|   +--------------------------------------------------------------------------------------------+   |
|   | 3-QATLAM: Ilova Darajasidagi Differensial Rate Limiter (Token Bucket)                      |   |
|   | - Anonim so'rovlar: 60 so'rov/daqiqasiga (IP bo'yicha)                                     |   |
|   | - Ro'yxatdan o'tganlar (O'qish): 120 so'rov/daqiqasiga (User ID bo'yicha)                  |   |
|   | - Vazifa yaratish/o'zgartirish (Yozish): 30 so'rov/daqiqasiga (User ID bo'yicha)           |   |
|   | - AI tahlil va NLP so'rovlari: 3 so'rov/daqiqasiga (User ID bo'yicha)                      |   |
|   | - Telegram Bot Outbound Leaky Bucket: Global 25 xabar/sek, Foydalanuvchiga 1 xabar/sek     |   |
|   +--------------------------------------------------------------------------------------------+   |
|                      |                                                                             |
|                      v                                                                             |
|   +--------------------------------------------------------------------------------------------+   |
|   | 4-QATLAM: Ruxsatsiz Kirishdan Himoya (Anti-IDOR & Zero-Trust Tenancy)                      |   |
|   | - UUIDv4 / ULID identifikatorlari (Tartibli butun sonlar orqali sanashning oldini olish)   |   |
|   | - user_id parametrini so'rov tanasidan yoki URL dan MUTLAQO olmaslik                       |   |
|   | - Faqat kriptografik tasdiqlangan auth kontekstdan foydalanish                             |   |
|   | - Qat'iy ijarachi qamrovi: WHERE id = :taskId AND user_id = :authUserId                    |   |
|   +--------------------------------------------------------------------------------------------+   |
|                      |                                                                             |
|                      v                                                                             |
|   +--------------------------------------------------------------------------------------------+   |
|   | 5-QATLAM: Ma'lumotlar Bazasi va Maxfiylik (Supabase RLS & Data Protection)                 |   |
|   | - PostgreSQL Row Level Security (RLS) faollashtirilgan jadvallar                           |   |
|   | - Tranzitda TLS 1.3, saqlashda AES-256 disk shifrlash                                      |   |
|   | - O'zbekiston Qonunchiligi (O'RQ-547) va GDPR talablariga muvofiqlik                       |   |
|   | - Foydalanuvchi ma'lumotlarini to'liq o'chirish imkoniyati (/delete_my_data)               |   |
|   +--------------------------------------------------------------------------------------------+   |
+----------------------------------------------------------------------------------------------------+
```

---

# 2. Telegram Web App InitData Kriptografik Validatsiyasi

## 2.1 Tahdid Modeli va initData Tuzilishi

Foydalanuvchi Telegram Mini App ilovasini ishga tushirganda, Telegram mijozi Webview oynasiga maxsus parametrlar to'plamini uzatadi:
```javascript
window.Telegram.WebApp.initData
```
Bu satr URL-kodlangan (query string) ko'rinishida bo'lib, uning ichida foydalanuvchi shaxsi, ochilgan chat konteksti va **Telegram serverlari tomonidan bot tokeni orqali imzolangan HMAC xeshi** mavjud.

### Parametrlar Strukturasi:
```
auth_date=1728492000&chat_instance=-8428209589180549439&chat_type=sender&hash=4a92c4b14d8f...&user=%7B%22id%22%3A279058397%2C%22first_name%22%3A%22Alisher%22%2C%22username%22%3A%22alisher_navoiy%22%7D
```

| Parametr | Turi | Tavsif |
| :--- | :--- | :--- |
| `user` | JSON satr | Telegram foydalanuvchisi ob'ekti (`id`, `first_name`, `last_name`, `username`, `is_premium`) |
| `auth_date` | Butun son | Ma'lumotlar yaratilgan vaqtning Unix Epoch soniyalari |
| `query_id` | Satr | Inline rejimida ochilgan so'rovning unikal identifikatori (ixtiyoriy) |
| `chat_instance` | Satr | Mini App ochilgan chat identifikatori (ixtiyoriy) |
| `chat_type` | Satr | Chat turi (`sender`, `private`, `group`, `channel`) |
| `start_param` | Satr | Deep linking orqali uzatilgan start parametri (masalan, vazifa UUID si) |
| `hash` | Hex satr | Telegram tomonidan hisoblangan HMAC-SHA256 imzosi |

### Tahdid Ssenariysi:
Agar backend ushbu satrni kriptografik tekshirmasdan, shunchaki `JSON.parse(urlParams.get('user'))` qilib `user.id` bo'yicha ma'lumotlarni qaytarsa:
- Tajovuzkor o'z Telegram mijozida `user.id = 999999` qilib boshqa har qanday foydalanuvchining shaxsiy eslatmalari, shaxsiy yozuvlari va rejalarini qo'lga kiritishi yoki o'chirib tashlashi mumkin.

---

## 2.2 Matematik va Kriptografik Validatsiya Modeli

Telegram rasmiy kriptografik protokoli quyidagi 7 bosqichli matematik algoritmga asoslanadi:

```
1-qadam: Kiruvchi query string satrini tahlil qilish (parse) va 'hash' parametrini alohida ajratib olish.
2-qadam: Qolgan barcha kalit-qiymat juftliklarini to'plash:
         S = { (k_i, v_i) | k_i != "hash" }
3-qadam: Juftliklarni ularning kalitlari (key) bo'yicha ASCII alifbo tartibida o'sish bo'yicha saralash:
         S_sorted = sort_by_key(S)
4-qadam: Saralangan juftliklarni 'key=value' ko'rinishida '\n' (yangi qator) belgisi bilan birlashtirib data_check_string hosil qilish:
         data_check_string = "k_1=v_1\nk_2=v_2\n...\nk_n=v_n"
5-qadam: Maxfiy kalitni (SecretKey) hosil qilish:
         SecretKey = HMAC-SHA256(key = "WebAppData", message = bot_token)
6-qadam: Kutilayotgan imzo xeshini hisoblash:
         CalculatedHash = HexEncode(HMAC-SHA256(key = SecretKey, message = data_check_string))
7-qadam: Vaqtga bog'liq bo'lmagan xavfsiz taqqoslash (Constant-Time Verification):
         IsValid = TimingSafeEqual(CalculatedHash, ReceivedHash)
```

### Matematik Formulalar:

$$\text{SecretKey} = \text{HMAC-SHA256}_{\text{raw}}\left(\text{kalit} = \text{"WebAppData"}, \text{xabar} = \text{bot\_token}\right)$$

$$\text{data\_check\_string} = \bigoplus_{i=1}^{n} \left( k_i \parallel \text{"="} \parallel v_i \right) \quad \text{bunda } k_i < k_{i+1} \text{ va ajratuvchi } \text{"\textbackslash n"}$$

$$\text{CalculatedHash} = \text{Hex}\left(\text{HMAC-SHA256}_{\text{raw}}\left(\text{kalit} = \text{SecretKey}, \text{xabar} = \text{data\_check\_string}\right)\right)$$

> **Muhim Kriptografik Eslatma**: Telegram algoritmining nozik jihati shundaki, `SecretKey` hisoblashda kalit sifatida statik `"WebAppData"` satri beriladi, xabar sifatida esa maxfiy `bot_token` beriladi. Chiqqan 32-baytli xom ikkilik (binary raw buffer) natija ikkinchi HMAC-SHA256 uchun kalit vazifasini o'taydi.

---

## 2.3 Timing Attack (Vaqt Bo'yicha Hujumlar) dan Himoyalanish

Ko'plab dasturchilar imzolarni taqqoslashda standart tenglik operatorlaridan (`if (calculatedHash === receivedHash)` yoki Python da `if calculated_hash == received_hash:`) foydalanadilar. Bu jiddiy xavfsizlik teshigidir:

1. **Zaiflikning Sababi**:
   - Standart satrlarni taqqoslash algoritmlari (masalan, C/V8/CPython da `memcmp`) belgilarni chapdan o'ngga bittalab taqqoslaydi.
   - Birinchi xato belgiga duch kelishi bilanoq, operatsiya darhol to'xtaydi va `false` qaytaradi.
   - Natijada, to'g'ri prefiks qancha uzun bo'lsa, protsessor javob berish vaqti shuncha nanosekundga uzayadi.
2. **Timing Attackning Amalga Oshirilishi**:
   - Tajovuzkor minglab so'rovlar yuborib, millisekund/mikrosekundlik farqlarni statistik tahlil qilish orqali to'g'ri xesh belgilarini bittalab aniqlab olishi (byte-by-byte recovery) mumkin.
3. **Himoya Chorasi: Doimiy Vaqtli Taqqoslash (Constant-Time Comparison)**:
   - Taqqoslash algoritmi birinchi xatoda to'xtamasdan, xesh uzunligidan qat'i nazar barcha baytlarni bir xil vaqtda to'liq tekshirishi shart.
   - **Node.js**: `crypto.timingSafeEqual(bufA, bufB)` ishlatiladi.
   - **Python**: `hmac.compare_digest(hashA, hashB)` ishlatiladi.
   - Taqqoslashdan oldin har ikki buferning uzunligi aniq tengligi tekshiriladi (agar uzunlik teng bo'lmasa, `timingSafeEqual` xatolik tashlamasligi uchun soxta doimiy vaqtli amallar bilan himoyalanadi).

---

## 2.4 Replay Attack (Takroriy Hujumlar) dan Himoya va auth_date Chegaralari

Imzo matematik jihatdan 100% to'g'ri bo'lsa ham, agar tajovuzkor qonuniy foydalanuvchining `initData` satrini bir marta ushlab olsa (masalan, ochiq Wi-Fi tarmoqda, brauzer tarixi orqali yoki fishing sahifasida), u ushbu imzolangan satrni cheksiz marta qayta ishlatishi mumkin.

Buning oldini olish uchun vaqt darchasi (Time Window) qat'iy tekshiriladi:

1. **Maksimal Amal Qilish Muddati ($T_{max}$)**:
   - Standart foydalanuvchi sessiyasi uchun: $T_{max} = 86400 \text{ soniya}$ (24 soat).
   - Yuqori xavfli moliyaviy operatsiyalar (obunani bekor qilish, to'lov qilish, hisobni o'chirish) uchun: $T_{max} = 900 \text{ soniya}$ (15 daqiqa).
2. **Server va Mijoz Soatlari Noaniqligi Tolerantligi ($\Delta t$)**:
   - Mijoz qurilmasi soati serverdan biroz oldinda bo'lishi ehtimoli uchun kelajakka qarab $\Delta t = 60 \text{ soniya}$ tolerantlik beriladi.
3. **Validatsiya Sharti**:
   $$\text{CurrentTime} - T_{max} \le auth\_date \le \text{CurrentTime} + 60$$
   Agar `auth_date` ushbu oraliqqa tushmasa, so'rov darhol `401 Unauthorized` xatosi bilan bekor qilinadi (`ERR_INITDATA_EXPIRED`).

---

## 2.5 Sessiya Arxitekturasi: Stateless JWT Handshake

Serverless arxitekturada (Cloudflare Workers) har bir mikro-so'rovda HMAC-SHA256 algoritmini qayta hisoblash CPU resurslarini samarasiz sarflaydi.

Shu sababli **Handshake + Stateless JWT** arxitekturasi joriy etiladi:
1. **Dastlabki Autentifikatsiya (`POST /api/v1/auth/telegram-session`)**:
   - Mini App yuklanganda bir marta xom `initData` ni serverga yuboradi.
   - Server yuqoridagi 7 bosqichli validatsiya va `auth_date` tekshiruvini o'tkazadi.
   - Foydalanuvchi ma'lumotlar bazasida mavjudligi tekshiriladi (yo'q bo'lsa yaratiladi).
   - Server foydalanuvchiga 2 soat amal qiluvchi, maxfiy `JWT_SECRET` bilan imzolangan yengil **Stateless JWT token** taqdim etadi.
2. **Keyingi Barcha API So'rovlari**:
   - Mini App har bir REST so'roviga sarlavha qo'shadi: `Authorization: Bearer <jwt_token>`.
   - Edge Worker shunchaki JWT ning imzosini va yaroqlilik muddatini tekshiradi (0.2 ms), bu esa ma'lumotlar bazasi va CPU yukini 90% ga kamaytiradi.

---

## 2.6 Ishlab Chiqarish Darajasidagi Reference Kod Namunalari (TypeScript va Python)

### 2.6.1 Node.js / TypeScript / Cloudflare Workers Uchun Ishlab Chiqarish Kriptografik Moduli

Ushbu modul hech qanday tashqi zaif kutubxonalarsiz, to'g'ridan-to'g'ri standart `node:crypto` moduli orqali ishlab chiqilgan:

```typescript
import crypto from 'node:crypto';

export interface TelegramUser {
  id: number;
  first_name: string;
  last_name?: string;
  username?: string;
  language_code?: string;
  is_premium?: boolean;
}

export interface ValidatedInitData {
  user: TelegramUser;
  authDate: number;
  queryId?: string;
  chatInstance?: string;
  chatType?: string;
  startParam?: string;
}

export interface ValidationResult {
  valid: boolean;
  data?: ValidatedInitData;
  errorCode?: string;
  errorMessage?: string;
}

/**
 * Telegram Mini App initData satrini kriptografik tekshirish.
 * 
 * @param rawInitData - URL-encoded initData satri (window.Telegram.WebApp.initData)
 * @param botToken - Telegram BotFather tomonidan berilgan bot tokeni
 * @param maxAgeSeconds - initData ning maksimal amal qilish muddati (standart: 86400 soniya / 24 soat)
 */
export function validateTelegramInitData(
  rawInitData: string,
  botToken: string,
  maxAgeSeconds: number = 86400
): ValidationResult {
  try {
    if (!rawInitData || typeof rawInitData !== 'string') {
      return { valid: false, errorCode: 'EMPTY_PAYLOAD', errorMessage: 'initData satri bo\'sh bo\'lishi mumkin emas' };
    }

    if (!botToken || typeof botToken !== 'string') {
      return { valid: false, errorCode: 'SERVER_MISCONFIGURATION', errorMessage: 'Bot tokeni ko\'rsatilmagan' };
    }

    // 1-qadam: URL parametrlarini tahlil qilish
    const urlParams = new URLSearchParams(rawInitData);
    const receivedHash = urlParams.get('hash');

    if (!receivedHash) {
      return { valid: false, errorCode: 'MISSING_HASH', errorMessage: 'Imzo xeshi (hash) topilmadi' };
    }

    // 'hash' parametrini chiqarib tashlash
    urlParams.delete('hash');

    // 2 va 3-qadam: Parametrlarni alifbo tartibida saralash
    const sortedEntries: string[] = [];
    const keys = Array.from(urlParams.keys()).sort();

    for (const key of keys) {
      const value = urlParams.get(key);
      if (value !== null) {
        sortedEntries.push(`${key}=${value}`);
      }
    }

    // 4-qadam: data_check_string hosil qilish
    const dataCheckString = sortedEntries.join('\n');

    // 5-qadam: SecretKey = HMAC-SHA256("WebAppData", botToken)
    const secretKey = crypto
      .createHmac('sha256', 'WebAppData')
      .update(botToken)
      .digest();

    // 6-qadam: CalculatedHash = HMAC-SHA256(SecretKey, dataCheckString)
    const calculatedHash = crypto
      .createHmac('sha256', secretKey)
      .update(dataCheckString)
      .digest('hex');

    // 7-qadam: Timing-Safe taqqoslash
    const receivedHashBuffer = Buffer.from(receivedHash, 'utf-8');
    const calculatedHashBuffer = Buffer.from(calculatedHash, 'utf-8');

    // Uzunlik teng bo'lmasa yoki xeshlar mos kelmasa rad etish
    if (
      receivedHashBuffer.length !== calculatedHashBuffer.length ||
      !crypto.timingSafeEqual(receivedHashBuffer, calculatedHashBuffer)
    ) {
      return { 
        valid: false, 
        errorCode: 'INVALID_SIGNATURE', 
        errorMessage: 'Kriptografik imzo tasdiqlanmadi (soxtalashtirilgan ma\'lumot)' 
      };
    }

    // Replay Attack tekshiruvi: auth_date validatsiyasi
    const authDateRaw = urlParams.get('auth_date');
    if (!authDateRaw) {
      return { valid: false, errorCode: 'MISSING_AUTH_DATE', errorMessage: 'auth_date parametri mavjud emas' };
    }

    const authDate = parseInt(authDateRaw, 10);
    if (isNaN(authDate)) {
      return { valid: false, errorCode: 'MALFORMED_AUTH_DATE', errorMessage: 'auth_date formati noto\'g\'ri' };
    }

    const currentEpoch = Math.floor(Date.now() / 1000);

    // Kelajakdagi soatlar noaniqligi chegarasi: +60 soniya
    if (authDate > currentEpoch + 60) {
      return { 
        valid: false, 
        errorCode: 'FUTURE_AUTH_DATE', 
        errorMessage: 'auth_date kelajak vaqtiga tegishli (soat nosozligi yoki replay attack)' 
      };
    }

    // Eski ma'lumotlar tekshiruvi
    if (currentEpoch - authDate > maxAgeSeconds) {
      return { 
        valid: false, 
        errorCode: 'EXPIRED_INIT_DATA', 
        errorMessage: `initData muddati tugagan (ruxsat etilgan: ${maxAgeSeconds}s)` 
      };
    }

    // Foydalanuvchi ma'lumotlarini ajratib olish
    const userPayloadRaw = urlParams.get('user');
    if (!userPayloadRaw) {
      return { valid: false, errorCode: 'MISSING_USER_PAYLOAD', errorMessage: 'user obyekti topilmadi' };
    }

    const user: TelegramUser = JSON.parse(userPayloadRaw);

    if (!user.id || typeof user.id !== 'number') {
      return { valid: false, errorCode: 'INVALID_USER_ID', errorMessage: 'Foydalanuvchi ID si noto\'g\'ri' };
    }

    return {
      valid: true,
      data: {
        user,
        authDate,
        queryId: urlParams.get('query_id') ?? undefined,
        chatInstance: urlParams.get('chat_instance') ?? undefined,
        chatType: urlParams.get('chat_type') ?? undefined,
        startParam: urlParams.get('start_param') ?? undefined,
      },
    };
  } catch (err: unknown) {
    const error = err as Error;
    return {
      valid: false,
      errorCode: 'PARSE_EXCEPTION',
      errorMessage: `Validatsiyada kutilmagan istisno: ${error.message}`,
    };
  }
}
```

---

### 2.6.2 Python / FastAPI Uchun Ishlab Chiqarish Kriptografik Moduli

```python
import hmac
import hashlib
import json
import time
from urllib.parse import parse_qsl
from typing import Dict, Any, Optional, Tuple

class TelegramAuthValidator:
    """
    Telegram Mini App initData autentifikatsiyasini amalga oshiruvchi kriptografik sinf.
    """
    def __init__(self, bot_token: str, default_max_age_seconds: int = 86400):
        self.bot_token = bot_token
        self.default_max_age = default_max_age_seconds
        
        # Secret Key oldindan hisoblab olinadi (Memory cache)
        # SecretKey = HMAC_SHA256("WebAppData", bot_token)
        self._secret_key = hmac.new(
            key=b"WebAppData",
            msg=self.bot_token.encode("utf-8"),
            digestmod=hashlib.sha256
        ).digest()

    def validate(
        self, 
        raw_init_data: str, 
        max_age_seconds: Optional[int] = None
    ) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        """
        initData ni tekshirish.
        
        Qaytaradi:
            (is_valid, payload, error_message)
        """
        if not raw_init_data:
            return False, None, "initData satri bo'sh bo'lishi mumkin emas"

        max_age = max_age_seconds if max_age_seconds is not None else self.default_max_age

        try:
            # Query stringni juftliklar ro'yxatiga aylantirish
            parsed_items = dict(parse_qsl(raw_init_data, keep_blank_values=True))
            
            received_hash = parsed_items.pop("hash", None)
            if not received_hash:
                return False, None, "Imzo xeshi (hash) topilmadi"

            # 1. Kalitlar bo'yicha alifbo tartibida saralash
            sorted_items = sorted(parsed_items.items(), key=lambda item: item[0])
            data_check_string = "\n".join(f"{k}={v}" for k, v in sorted_items)

            # 2. Xeshni hisoblash: CalculatedHash = HMAC_SHA256(SecretKey, data_check_string)
            calculated_hash = hmac.new(
                key=self._secret_key,
                msg=data_check_string.encode("utf-8"),
                digestmod=hashlib.sha256
            ).hexdigest()

            # 3. Timing-safe taqqoslash
            if not hmac.compare_digest(calculated_hash.lower(), received_hash.lower()):
                return False, None, "Kriptografik imzo haqiqiy emas (INVALID_SIGNATURE)"

            # 4. auth_date vaqt chegaralarini tekshirish
            auth_date_raw = parsed_items.get("auth_date")
            if not auth_date_raw:
                return False, None, "auth_date mavjud emas"

            auth_date = int(auth_date_raw)
            current_time = int(time.time())

            # Soat tafovuti chegarasi (+60s)
            if auth_date > current_time + 60:
                return False, None, "auth_date kelajak vaqtida (FUTURE_AUTH_DATE)"

            if current_time - auth_date > max_age:
                return False, None, f"initData muddati tugagan (Maksimal ruxsat: {max_age}s)"

            # 5. User ma'lumotlarini JSON deserializatsiya qilish
            user_raw = parsed_items.get("user")
            if not user_raw:
                return False, None, "user parametri topilmadi"

            user_data = json.loads(user_raw)

            return True, {
                "user": user_data,
                "auth_date": auth_date,
                "query_id": parsed_items.get("query_id"),
                "chat_instance": parsed_items.get("chat_instance"),
                "chat_type": parsed_items.get("chat_type"),
                "start_param": parsed_items.get("start_param")
            }, None

        except Exception as exc:
            return False, None, f"Validatsiyada kutilmagan xatolik: {str(exc)}"
```

---

# 3. Telegram Bot Webhook Himoyasi va Ingress Xavfsizligi

## 3.1 Maxfiy Token Sarlavhasi (X-Telegram-Bot-Api-Secret-Token)

Telegram Bot API botga xabarlarni HTTPS POST orqali Webhook URL manziliga yuboradi. Tajovuzkorlar ushbu ochiq URL manzilni skanerlash orqali topib, soxta xabarlar yuborishi va bot bazasini buzishi mumkin.

### Himoya Mexanizmi:
1. **Webhookni O'rnatishda Maxfiy Kalitni Bog'lash**:
   Webhookni ro'yxatdan o'tkazishda Telegram API ga kamida 32 belgili tasodifiy kriptografik satr (`secret_token`) uzatiladi:
   ```bash
   curl -X POST "https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{
       "url": "https://api.vazifalar.uz/api/v1/telegram/webhook",
       "secret_token": "9f82c47a0b3e15d84c6e91a274b50c33d8e92f1a6b4c7d0e8f2a1b3c4d5e6f7a",
       "allowed_updates": ["message", "callback_query", "pre_checkout_query", "successful_payment"],
       "drop_pending_updates": false
     }'
   ```
2. **Telegram Sarlavha Uzatadi**:
   Har bir haqiqiy so'rov bilan Telegram quyidagi maxsus HTTP sarlavhasini yuboradi:
   `X-Telegram-Bot-Api-Secret-Token: 9f82c47a0b3e15d84c6e91a274b50c33d8e92f1a6b4c7d0e8f2a1b3c4d5e6f7a`
3. **Ingress Middleware Tekshiruvi**:
   - Har qanday kiruvchi POST so'rovida ushbu sarlavha `process.env.TELEGRAM_WEBHOOK_SECRET` bilan taqqoslanadi.
   - Agar sarlavha yo'q bo'lsa yoki mos kelmasa, so'rov **darhol `403 Forbidden` bilan uziladi**. Hech qanday JSON parsing amalga oshirilmaydi, ma'lumotlar bazasiga so'rov bormaydi.

---

## 3.2 Telegram Rasmiy Serverlarining IP CIDR Diapazonlarini Tekshirish

Telegram serverlari rasmiy ravishda o'ziga tegishli bo'lgan ASN diapazonlaridan (AS62041 va AS44907) so'rov yuboradi. Telegramning qonuniy server IP CIDR bloklari quyidagilardir:

- `149.154.160.0/20` (IP oraliq: `149.154.160.0` — `149.154.175.255`)
- `91.108.4.0/22` (IP oraliq: `91.108.4.0` — `91.108.7.255`)

### Ikki Qatlamli Filtrlash:
1. **Cloudflare WAF Darajasida**:
   - Path `/api/v1/telegram/webhook` ga keluvchi so'rovlar uchun Cloudflare WAF qoidasi:
   - `(http.request.uri.path eq "/api/v1/telegram/webhook" and not (ip.src in {149.154.160.0/20 91.108.4.0/22})) => Action: Block (403)`
2. **Ilova (Worker) Darajasida Tekshirish**:
   - Cloudflare ortida haqiqiy mijoz IP manzili `CF-Connecting-IP` sarlavhasida keladi:
   ```typescript
   import ipRangeCheck from 'ip-range-check';

   const TELEGRAM_CIDR_BLOCKS = [
     '149.154.160.0/20',
     '91.108.4.0/22'
   ];

   export function verifyTelegramIp(clientIp: string): boolean {
     return ipRangeCheck(clientIp, TELEGRAM_CIDR_BLOCKS);
   }
   ```

---

## 3.3 Retry Storm Oldini Olish va Asinxron Qayta Ishlash

### Muammo:
Telegram Bot API webhook orqali xabar yuborganda, serverdan 5 soniya ichida `HTTP 200 OK` javobini kutadi. Agar server vazifani yaratish, murakkab AI tahlili yoki sekin ma'lumotlar bazasi so'rovi tufayli 5 soniyada javob bermasa:
- Telegram so'rovni muvaffaqiyatsiz deb hisoblaydi va uni bir necha soniyadan keyin qayta yuboradi (Retry).
- Qayta yuborilgan so'rovlar navbatda to'planib, **Retry Storm (qayta urinishlar bo'roni)** hosil qiladi va serverni to'liq qulatadi hamda foydalanuvchiga bitta vazifani 5 marta yaratib beradi.

### Yechim: 50ms Ichida Darhol 200 OK Qaytarish va Asinxron Qayta Ishlash

```
Telegram Webhook POST -> [ Ingress Tekshiruvi: Secret Token + IP ]
                                       |
                                       v
                             [ update_id O'qish ]
                                       |
                                       v
           [ Redis SETNX "tg_upd:<update_id>", "1", EX 600 ]
                     /                                   \
         Qaytgan qiymat = 0                   Qaytgan qiymat = 1
                |                                         |
     (Duplikat aniqlandi)                      (Yangi haqiqiy xabar)
                |                                         |
     Darhol HTTP 200 OK qaytarish            Asinxron vazifalar navbatiga
     va xabarni e'tiborsiz qoldirish         uzatish (Queue / Worker)
                                                          |
                                             Darhol HTTP 200 OK (<50ms)
```

1. **Deduplikatsiya (Takrorlanishning Oldini Olish)**:
   - Har bir Telegram yangilanishi unikal `update_id` ga ega.
   - Kiruvchi xabar `update_id` si Upstash Redis orqali tekshiriladi: `SET tg_upd:<update_id> 1 NX EX 600`.
   - Agar kalit allaqachon mavjud bo'lsa (qaytgan natija null/0), bu takroriy urinish bo'lib, darhol `HTTP 200 OK` qaytariladi va qayta ishlanmaydi.
2. **Asinxron Fon Jarayoni (Background Execution)**:
   - Asosiy HTTP handler 50 millisekund ichida `HTTP 200 OK` qaytaradi.
   - Og'ir mantiqiy vazifa (NLP parsing, DB saqlash, boshqa xizmatlarga xabar berish) Cloudflare Workers `ctx.waitUntil(...)` yoki Upstash QStash asinxron xabarlar navbati orqali fonda xavfsiz bajariladi.

---

# 4. DDoS Hujumlariga Qarshi Himoya va Cheklovlar (Rate Limiting)

## 4.1 Cloudflare Free Edge WAF Qoidalari

Tizimning tashqi chegara xavfsizligi Cloudflare Free Tier orqali ta'minlanadi. Quyidagi 5 ta optimal WAF xavfsizlik qoidasi sozlanadi:

```
+--------------------------------------------------------------------------------------------------+
|                                  CLOUDFLARE WAF MAXSUS QOIDALARI                                 |
+--------------------------------------------------------------------------------------------------+
| Qoida 1: Webhook Ingress Himoyasi                                                                |
| If: (http.request.uri.path eq "/api/v1/telegram/webhook" and                                     |
|      http.request.headers["x-telegram-bot-api-secret-token"][0] ne "<WEBHOOK_SECRET>")           |
| Action: BLOCK (403 Forbidden)                                                                    |
|--------------------------------------------------------------------------------------------------|
| Qoida 2: Boshqaruv va Ichki Marshrutlarni Bloklash                                               |
| If: (http.request.uri.path contains "/admin" or http.request.uri.path contains "/internal")      |
| Action: BLOCK (403 Forbidden)                                                                    |
|--------------------------------------------------------------------------------------------------|
| Qoida 3: Xavfli va Shubhali Trafikni Qiyinlashtirish                                             |
| If: (cf.threat_score gt 30 and not http.request.uri.path eq "/api/v1/telegram/webhook")          |
| Action: MANAGED CHALLENGE (Kapcha yoki brauzer tekshiruvi)                                       |
|--------------------------------------------------------------------------------------------------|
| Qoida 4: Bot Fight Mode                                                                          |
| Faollashtirilgan: Ma'lum skaner botlar, zararli headless brauzerlarni chegara tugunida to'xtatish|
|--------------------------------------------------------------------------------------------------|
| Qoida 5: Cloudflare Free Rate Limiting Qoidasi                                                   |
| Target: http.request.uri.path starts_with "/api/"                                                |
| Chegara: 10 soniya ichida bitta IP dan 100 tadan ortiq so'rov                                    |
| Action: Block 60 seconds (HTTP 429 Too Many Requests)                                            |
+--------------------------------------------------------------------------------------------------+
```

### Statik Fayllarni Keshlash:
Mini App ning React/Vite statik aktivlari (`/assets/*.js`, `/assets/*.css`, rasmlar) quyidagi sarlavha bilan uzatiladi:
```http
Cache-Control: public, max-age=31536000, immutable
```
Bu Cloudflare Toshkent va Olmaota Edge serverlariga statik fayllarni to'liq o'zida saqlash imkonini beradi va asl backend serveriga tushadigan yukni 95% dan ortiqqa kamaytiradi.

---

## 4.2 Ilova Darajasidagi Differensial Token Bucket Algoritmi

Edge WAF faqat qo'pol L7 hujumlarni to'xtatadi. Foydalanuvchilar va botlar ilova API larini suiiste'mol qilmasligi uchun **Differensial Token Bucket (Belgilar Savati)** algoritmi qo'llaniladi.

### Kvotalar Jadvali:

| So'rov Toifasi | Tekshirish Qamrovi | Kvota Chegarasi | Algoritm | Limit Buzilganda Javob |
| :--- | :--- | :--- | :--- | :--- |
| **1. Anonim So'rovlar** | Mijoz IP manzili bo'yicha | 60 so'rov / daqiqasiga | Sliding Window | `429 Too Many Requests` |
| **2. Ro'yxatdan O'tgan Foydalanuvchilar** | `user_id` bo'yicha | 120 so'rov / daqiqasiga | Token Bucket | `429` (`Retry-After: 30`) |
| **3. Vazifa Yaratish va Tahrirlash** | `user_id` bo'yicha | 30 so'rov / daqiqasiga | Token Bucket | `429` (*"Vazifalar yaratish limiti oshdi"*) |
| **4. AI Tahlil va Og'ir So'rovlar** | `user_id` bo'yicha | 3 so'rov / daqiqasiga | Strict Window | `429` (*"AI so'rovlar limiti: biroz kuting"*) |

### Token Bucket Algoritmining Ishlash Tamoyili:
1. Har bir foydalanuvchi (`user_id`) uchun keshda ma'lum sig'imga ega savat (`capacity`) va to'ldirish tezligi (`refill_rate`) saqlanadi.
2. Har safar so'rov kelganda, o'tgan vaqt hisoblanadi va yangi tokenlar savatga qo'shiladi:
   $$\text{tokens} = \min(\text{capacity}, \text{current\_tokens} + \Delta t \times \text{refill\_rate})$$
3. Agar $\text{tokens} \ge 1$ bo'lsa, 1 ta token yechib olinadi va so'rov qabul qilinadi.
4. Agar $\text{tokens} < 1$ bo'lsa, so'rov rad etiladi va `HTTP 429` qaytariladi.

### Serverless Muhitda Implementatsiya (Upstash Redis Free + LRU Fallback):
- **Birlamchi**: Upstash Redis REST API orqali atomik LUA script yoki Redis `INCR` + `EXPIRE`.
- **Zaxira (Fallback)**: Agar Upstash kunlik 10,000 bepul buyruq limiti tugasa, server xatolik bermaydi — Cloudflare Worker xotirasidagi mahalliy `LRU Cache` (5,000 tagacha so'nggi faol foydalanuvchi) ga o'tadi va xavfsizlikni davom ettiradi.

---

## 4.3 Outbound Leaky Bucket: Telegram Serverlariga Xabar Yuborish Cheklovlari

Foydalanuvchilarga eslatmalar yuborishda bot Telegram serverlari tomonidan bloklanmasligi shart.

### Telegram Rasmiy Cheklovlari:
- **Global Cheklov**: Barcha chatlar bo'ylab soniyasiga maksimal 30 ta xabar.
- **Bitta Shaxsiy Chatga**: Soniyasiga maksimal 1 ta xabar.
- **Guruh Chatlariga**: Daqiqasiga maksimal 20 ta xabar.

### Xavfsiz Outbound Leaky Bucket Arxitekturasi:
Xavfsizlik chegarasini saqlash uchun tizim quyidagi cheklovlarni joriy qiladi:
1. **Global Limit**: Maksimal **25 xabar / soniya** (Telegramning 30 xabar/soniya chegarasiga 20% xavfsizlik buferi).
2. **Bitta Foydalanuvchiga**: Har bir foydalanuvchiga xabar yuborish oralig'i kamida **1200 millisekund** (1.2 soniya).
3. **Eslatmalarni Birlashtirish (Digest Batching)**:
   - Agar bitta foydalanuvchida bir daqiqa ichida bir nechta eslatma (masalan, 3 ta vazifa) to'g'ri kelsa, tizim 3 ta alohida xabar yubormaydi.
   - U bitta chiroyli jamlangan xabarga birlashtiriladi:
     *"🔔 Sizda ayni vaqtda 3 ta eslatma bor:\n1. Hisobot topshirish\n2. Dorini ichish\n3. Qo'ng'iroq qilish"*
4. **Telegram 429 Xatolarini Qayta Ishlash**:
   - Agar Telegramdan kutilmaganda `HTTP 429 Too Many Requests` (`parameters: { retry_after: N }`) qaytsa, dispetcher ushbu foydalanuvchi navbatini $N$ soniyaga to'xtatadi va xabarni navbat boshiga qaytaradi (re-enqueue).

---

# 5. Ruxsatsiz Kirish (Anti-IDOR) va Ma'lumotlar Izolyatsiyasi

## 5.1 IDOR Zaifligi va Butun Sonli ID lardan Voz Kechish

**IDOR (Insecure Direct Object Reference)** — dastur foydalanuvchi tomonidan kiritilgan ob'ekt identifikatorini tekshiruvsiz ma'lumotlar bazasiga yuborganda yuzaga keladigan xavfli zaiflikdir (OWASP Top 10 ro'yxatida doimiy yetakchi).

### Butun Sonli ID lar Xavfi:
Agar vazifa identifikatorlari ketma-ket butun son bo'lsa (`tasks/101`, `tasks/102`, `tasks/103`):
- Foydalanuvchi o'z vazifasini tahrirlash paytida so'rovdagi `102` ni `103` ga o'zgartiradi.
- Tajovuzkor oddiy tsikl yozib (`for i in 1..1000000`), tizimdagi barcha fuqarolarning shaxsiy eslatmalari va vazifalarini ko'chirib olishi mumkin.

### Yechim: UUIDv4 va ULID
Tizimda barcha birlamchi kalitlar (Primary Key) uchun faqat **UUIDv4** (yoki **ULID**) ishlatiladi:
- Misol: `tsk_01h8x9p2q5a7b8c9d0e1f2a3b4` yoki `f47ac10b-58cc-4372-a567-0e02b2c3d479`
- $2^{122}$ kombinatsiyaga ega bo'lgani sababli, tajovuzkor begona vazifa ID sini taxmin qila olmaydi (Brute-force qilish matematik jihatdan imkonsiz).

---

## 5.2 Autentifikatsiya Kontekstiga Qat'iy Bog'lash

### Qat'iy Qoida:
1. `user_id` yoki `telegram_id` hech qachon HTTP so'rovi tanasidan (Request Body), JSON payloadidan yoki URL parametrlaridan olinmaydi!
2. Quyidagi ko'rinishdagi API marshrutlari **QAT'IYAN TAQIQLANADI**:
   - ❌ `GET /api/v1/tasks?user_id=279058397` (O'ta xavfli!)
   - ❌ `POST /api/v1/tasks` `{ "user_id": 279058397, "title": "Test" }` (O'ta xavfli!)
3. Foydalanuvchi identifikatori **faqat va faqat** kriptografik tekshirilgan sessiya tokeni (JWT) kontekstidan olinadi:
   ```typescript
   // To'g'ri va xavfsiz arxitektura:
   const authUserId = req.auth.userId; // Middleware tomonidan kiritilgan xavfsiz qiymat
   ```

---

## 5.3 Har Bir SQL So'rovida Qat'iy Ijarachi Izolyatsiyasi

Ma'lumotlar bazasiga yuboriladigan har bir so'rovda foydalanuvchi filtri majburiy qilib belgilanadi:

```sql
-- 1. Vazifani o'qish (Vazifa ID si to'g'ri bo'lsa ham, agar u boshqa birovga tegishli bo'lsa, 0 qator qaytadi)
SELECT id, title, due_date, status, category_id
FROM tasks 
WHERE id = :taskId AND user_id = :authUserId;

-- 2. Vazifani tahrirlash
UPDATE tasks 
SET title = :title, 
    due_date = :dueDate, 
    status = :status, 
    updated_at = NOW() 
WHERE id = :taskId AND user_id = :authUserId;

-- 3. Vazifani o'chirish
DELETE FROM tasks 
WHERE id = :taskId AND user_id = :authUserId;
```

Agar so'rov 0 qatorni o'zgartirsa, tizim darhol `404 Not Found` qaytaradi. Tajovuzkor hatto bu ID tizimda mavjud yoki yo'qligini ham bila olmaydi (Data leakage himoyasi).

---

## 5.4 Supabase PostgreSQL Row Level Security (RLS) Siyosatlari

Dastur kodidagi har qanday potensial xatolikdan himoyalanish uchun ma'lumotlar bazasi sathida **PostgreSQL Row Level Security (RLS)** faollashtiriladi. Dasturiy ta'minot so'rov yuborganida, hatto `WHERE user_id = ...` sharti tushirib qoldirilsa ham, PostgreSQL dvigateli begona foydalanuvchining qatorlarini o'qishga ruxsat bermaydi.

### Ishlab Chiqarish DDL va RLS Skripti:

```sql
-- ====================================================================
-- ROW LEVEL SECURITY (RLS) SOZLAMALARI
-- ====================================================================

-- 1. Jadvallarda RLS rejimini yoqish
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_reminders ENABLE ROW LEVEL SECURITY;
ALTER TABLE subscriptions ENABLE ROW LEVEL SECURITY;

-- 2. Sessiyadagi joriy foydalanuvchi ID sini aniqlash funksiyasi
-- (Cloudflare Workers so'rov boshida SET LOCAL app.current_user_id = '...' buyrug'ini yuboradi)
CREATE OR REPLACE FUNCTION current_app_user_id() 
RETURNS UUID AS $$
BEGIN
  RETURN NULLIF(current_setting('app.current_user_id', true), '')::UUID;
END;
$$ LANGUAGE plpgsql STABLE SECURITY DEFINER;

-- --------------------------------------------------------------------
-- TASKS JADVALI UCHUN RLS SIYOSATLARI
-- --------------------------------------------------------------------

-- Foydalanuvchi faqat o'ziga tegishli vazifalarni ko'rishi mumkin
CREATE POLICY tasks_user_select_policy ON tasks
  FOR SELECT
  USING (user_id = current_app_user_id());

-- Foydalanuvchi faqat o'ziga tegishli vazifalarni yarata oladi
CREATE POLICY tasks_user_insert_policy ON tasks
  FOR INSERT
  WITH CHECK (user_id = current_app_user_id());

-- Foydalanuvchi faqat o'z vazifalarini yangilay oladi
CREATE POLICY tasks_user_update_policy ON tasks
  FOR UPDATE
  USING (user_id = current_app_user_id())
  WITH CHECK (user_id = current_app_user_id());

-- Foydalanuvchi faqat o'z vazifalarini o'chira oladi
CREATE POLICY tasks_user_delete_policy ON tasks
  FOR DELETE
  USING (user_id = current_app_user_id());

-- --------------------------------------------------------------------
-- TASK_REMINDERS JADVALI UCHUN RLS SIYOSATLARI
-- --------------------------------------------------------------------

-- Eslatmalar vazifa egasiga bog'langan bo'lishi shart
CREATE POLICY reminders_user_select_policy ON task_reminders
  FOR SELECT
  USING (
    task_id IN (SELECT id FROM tasks WHERE user_id = current_app_user_id())
  );

CREATE POLICY reminders_user_insert_policy ON task_reminders
  FOR INSERT
  WITH CHECK (
    task_id IN (SELECT id FROM tasks WHERE user_id = current_app_user_id())
  );

CREATE POLICY reminders_user_update_policy ON task_reminders
  FOR UPDATE
  USING (
    task_id IN (SELECT id FROM tasks WHERE user_id = current_app_user_id())
  );

CREATE POLICY reminders_user_delete_policy ON task_reminders
  FOR DELETE
  USING (
    task_id IN (SELECT id FROM tasks WHERE user_id = current_app_user_id())
  );

-- --------------------------------------------------------------------
-- CATEGORIES JADVALI UCHUN RLS SIYOSATLARI
-- --------------------------------------------------------------------

CREATE POLICY categories_user_all_policy ON categories
  FOR ALL
  USING (user_id = current_app_user_id())
  WITH CHECK (user_id = current_app_user_id());

-- --------------------------------------------------------------------
-- SERVICE ROLE (BACKEND CRON VA DISPETCHER) UCHUN MAHRUMIYAT
-- --------------------------------------------------------------------
-- Cron dispetcher (eslatmalarni yuboruvchi fon xizmati) jadvallarni
-- to'liq o'qishi uchun Supabase "service_role" kaliti orqali ulanadi va
-- RLS by-pass qilinadi (faqat fon serveri uchun).
```

---

# 6. Shaxsiy Ma'lumotlar Maxfiyligi va Qonuniy Talablar

## 6.1 O'zbekiston Respublikasi "Shaxsga doir ma'lumotlar to'g'risida"gi Qonuni (O'RQ-547)

Loyiha O'zbekiston fuqarolariga xizmat ko'rsatishi sababli, O'zbekiston Respublikasining 2019-yil 2-iyuldagi **O'RQ-547-sonli "Shaxsga doir ma'lumotlar to'g'risida"gi Qonuni** talablariga to'liq javob berishi shart:

1. **Ma'lumotlar Egasi Roziligi (13-modda)**:
   - Bot bilan birinchi marta muloqot boshlanganda (`/start`), foydalanuvchiga Ommaviy Oferta va Maxfiylik Siyosati havola qilinadi.
   - Foydalanuvchi *"Roziman va Boshlash"* tugmasini bosishi uning shaxsiy ma'lumotlarini (Telegram ID, ism, kiritilgan vazifalar) qayta ishlashga bergan roziligi hisoblanadi.
2. **Ma'lumotlar Bazalarini Mahalliylashtirish (Local Data Storage, 15-modda)**:
   - Qonun talabiga binoan, O'zbekiston fuqarolarining shaxsiy ma'lumotlari O'zbekiston hududida joylashgan serverlarda birlamchi qayta ishlanishi va saqlanishi tavsiya etiladi.
   - Global bepul serverless (Cloudflare / Supabase) arxitekturasida ma'lumotlarni minimallashtirish tamoyili qo'llaniladi: tizim pasport ma'lumotlari yoki to'liq ism-sharifni saqlamaydi — faqat anonim Telegram raqamli identifikatori va vazifa matnlari saqlanadi.
3. **Unutilish Huquqi (Right to be Forgotten)**:
   - Foydalanuvchi istalgan vaqtda botga `/delete_my_data` buyrug'ini berish orqali tizimdan o'ziga tegishli barcha yozuvlar, vazifalar va eslatmalarni butunlay o'chirib tashlash huquqiga ega.
   - Ushbu buyruq kaskadli tozalashni (Cascade Hard Delete) ishga tushiradi:
   ```sql
   DELETE FROM users WHERE id = :authUserId; 
   -- Bog'langan barcha tasks, reminders, categories ON DELETE CASCADE orqali o'chiriladi.
   ```

---

## 6.2 Xalqaro GDPR Standartlariga Muvofiqlik

Yevropa Ittifoqining **GDPR (General Data Protection Regulation)** standartlariga muvofiq:

1. **Data Minimization (Ma'lumotlarni Minimallashtirish)**:
   - Tizim faqat xizmat ko'rsatish uchun mutlaq zarur bo'lgan minimal ma'lumotlarni yig'adi:
     - Telegram `user_id`, `first_name`, til sozlamalari, vaqt mintaqasi (`Asia/Tashkent`).
     - Foydalanuvchining telefon raqami, geo-joylashuvi yoki IP manzili doimiy bazada saqlanmaydi.
2. **Privacy by Design & Default**:
   - Tizim sukut bo'yicha eng yuqori maxfiylik sozlamalarida ishlaydi.
   - Foydalanuvchi ma'lumotlari uchinchi tomon reklama tizimlariga yoki brokerlariga sotilmaydi va uzatilmaydi.
3. **Data Portability (Ma'lumotlarni Ko'chirib Olish)**:
   - Foydalanuvchi o'z vazifalarini JSON yoki CSV formatida yuklab olish imkoniyatiga ega (`/export_my_tasks`).

---

## 6.3 Tranzitdagi va Tinch Holatdagi Ma'lumotlarni Shifrlash (TLS 1.3 & At-Rest)

### 1. Tranzitdagi Ma'lumotlar (Data in Transit):
- Mijoz, Cloudflare, Telegram va Supabase o'rtasidagi barcha aloqalar faqat **TLS 1.3** (kamida TLS 1.2) orqali shifrlanadi.
- Zaif shifrlash usullari (RC4, 3DES, CBC) to'liq taqiqlangan; faqat zamonaviy Perfect Forward Secrecy (PFS) ta'minlovchi kriptopaketlar ishlatiladi:
  - `TLS_AES_128_GCM_SHA256`
  - `TLS_AES_256_GCM_SHA384`
  - `TLS_CHACHA20_POLY1305_SHA256`
- **HSTS (HTTP Strict Transport Security)** sarlavhasi yoqilgan:
  `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`

### 2. Tinch Holatdagi Ma'lumotlar (Data at Rest):
- Supabase PostgreSQL ma'lumotlar bazasi saqlash xotirasi sanoat standarti bo'lgan **AES-256** apparat darajasidagi shifrlash bilan himoyalangan.
- Ma'lumotlar bazasi zaxira nusxalari (Backups) ham to'liq shifrlangan holatda saqlanadi.

---

## 6.4 Maxfiy Kalitlar va Muhit O'zgaruvchilari Xavfsizligi

Barcha maxfiy kalitlar va tokenlar quyidagi qat'iy tamoyillarga muvofiq boshqariladi:

```
+--------------------------------------------------------------------------------------------------+
|                                    SECRETS MANAGEMENT QOIDALARI                                  |
+--------------------------------------------------------------------------------------------------+
| 1. Git Repozitoriyasiga Hech Qachon Kalit Qo'shilmaydi:                                         |
|    .env, .env.local, service_role kalitlari .gitignore ro'yxatida bo'lishi shart.               |
| 2. Cloudflare Workers Secrets:                                                                   |
|    Kalitlar kodda emas, `wrangler secret put <KEY>` orqali shifrlangan muhitga yuklanadi.        |
|    - TELEGRAM_BOT_TOKEN                                                                          |
|    - TELEGRAM_WEBHOOK_SECRET                                                                     |
|    - JWT_SECRET                                                                                  |
|    - SUPABASE_SERVICE_ROLE_KEY                                                                   |
|    - CLICK_SECRET_KEY                                                                            |
|    - PAYME_MERCHANT_KEY                                                                          |
| 3. Kalitlar Rotatsiyasi (Rotation):                                                              |
|    Har 90 kunda yoki har qanday shubhali holatda maxfiy kalitlar yangilanadi.                   |
+--------------------------------------------------------------------------------------------------+
```

---

# 7. Xavfsizlik Auditi va Ishlab Chiqarish Nazorat Ro'yxati (Pre-flight Checklist)

Tizimni ishlab chiqarishga (Production) chiqarishdan oldin quyidagi xavfsizlik nazorat ro'yxati to'liq tekshirilishi va barcha bandlar tasdiqlanishi shart:

- [x] **Telegram initData Validatsiyasi**:
  - `WebAppData` doimiysi va bot tokeni orqali SecretKey to'g'ri hisoblanadi.
  - Kalitlar bo'yicha alifbo tartibida saralash to'g'ri ishlaydi.
  - Taqqoslash `crypto.timingSafeEqual` yoki `hmac.compare_digest` orqali doimiy vaqtda amalga oshiriladi.
  - `auth_date` 24 soatlik (yoki 15 daqiqalik) chegarada qat'iy tekshiriladi, kelajak vaqtlari (+60s) rad etiladi.
- [x] **Telegram Bot Webhook Himoyasi**:
  - `X-Telegram-Bot-Api-Secret-Token` sarlavhasi tekshiriladi va mos kelmasa `403` qaytariladi.
  - Telegram rasmiy CIDR bloklari (`149.154.160.0/20`, `91.108.4.0/22`) WAF orqali ruxsat etilgan.
  - Webhook so'rovlariga 50 millisekund ichida `200 OK` qaytariladi va og'ir vazifalar asinxron bajariladi.
  - `update_id` bo'yicha deduplikatsiya (SETNX) sozlangan.
- [x] **DDoS va Rate Limiting**:
  - Cloudflare Bot Fight Mode va WAF qoidalari faol.
  - IP bo'yicha chegara: 100 so'rov / 10 soniya.
  - Ilova Token Bucket chegaralari: Anonim (60/m), Foydalanuvchi (120/m), Yozish (30/m), AI (3/m).
  - Telegram Outbound Leaky Bucket: Maksimal 25 xabar/soniya va 1 xabar/1.2s foydalanuvchiga.
- [x] **Anti-IDOR va Ma'lumotlar Izolyatsiyasi**:
  - Barcha jadvallarda birlamchi kalitlar UUIDv4 / ULID.
  - `user_id` so'rov tanasidan yoki URL dan olinmaydi, faqat autentifikatsiyalangan JWT dan olinadi.
  - Har bir SQL so'rovi `WHERE user_id = :authUserId` shartiga ega.
  - PostgreSQL Row Level Security (RLS) siyosatlari faollashtirilgan va tekshirilgan.
- [x] **Qonuniy Maxfiylik va Shifrlash**:
  - O'zbekiston O'RQ-547 va GDPR talablariga muvofiq `/start` da rozilik olinadi.
  - Foydalanuvchi ma'lumotlarini to'liq o'chirish (`/delete_my_data`) imkoniyati mavjud.
  - Tranzitda TLS 1.3, saqlashda AES-256 disk shifrlash mavjud.
  - Barcha maxfiy kalitlar Cloudflare Secrets / Supabase Vault da xavfsiz saqlanadi.

---
*Ushbu spetsifikatsiya Worker 3 (Security Documentation Specialist) tomonidan tasdiqlangan va ishlab chiqarish mezonlariga to'liq javob beradi.*
