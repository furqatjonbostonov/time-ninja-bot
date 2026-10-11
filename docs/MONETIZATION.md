# Telegram "Vazifalar va Eslatmalar" Tizimi: O'rta Osiyo Bozori Uchun Keng Qamrovli Monetizatsiya Strategiyasi va To'lov Shlyuzlari Arxitekturasi

**Loyiha**: Telegram Task & Reminder Bot + Mini App (Central Asia Market)  
**Hujjat Maqomi**: Ishlab Chiqarishga Tayyor (Production-Grade Specification)  
**Hujjat Keltirilgan Manzil**: `MONETIZATION.md`  
**Hududiy Qamrov**: O'zbekiston, Qozog'iston, Qirg'iziston, Tojikiston va xalqaro bozor  
**Muallif / Rol**: Worker 4 — Monetizatsiya va FinTex Hujjatlashtirish Mutaxassisi  

---

## Mundarija

1. [O'rta Osiyo Bozori Tahlili va Iste'molchi Psixologiyasi](#1-orta-osiyo-bozori-tahlili-va-istimolchi-psixologiyasi)
   - 1.1 [Mintaqada Telegramning Monopol O'rni va Raqamli Hayot Tarzi](#11-mintaqada-telegramning-monopol-orni-va-raqamli-hayot-tarzi)
   - 1.2 [Mahalliy To'lov Madaniyati va FinTex Ekologiyasi](#12-mahalliy-tolov-madaniyati-va-fintex-ekologiyasi)
   - 1.3 [Mobil-First Mentalitet va "Bir Bosishda To'lash" Odatlari](#13-mobil-first-mentalitet-va-bir-bosishda-tolash-odatlari)
   - 1.4 [Mikro-To'lovlarga Munosabat va Xarid Qobiliyati Psixologiyasi](#14-mikro-tolovlarga-munosabat-va-xarid-qobiliyati-psixologiyasi)
   - 1.5 [Xalqaro Tizimlarning (Stripe, PayPal) O'rta Osiyodagi Inqirozi](#15-xalqaro-tizimlarning-stripe-paypal-orta-osiyodagi-inqirozi)
2. [Kamida 3 Ta Aniq Monetizatsiya Modeli](#2-kamida-3-ta-aniq-monetizatsiya-modeli)
   - 2.1 [Model 1: Freemium + Premium SaaS Obuna Modeli](#21-model-1-freemium--premium-saas-obuna-modeli)
     - 2.1.1 [Bepul (Free) va Pullik (Premium) Tariflar Taqqoslash Matritsasi](#211-bepul-free-va-pullik-premium-tariflar-taqqoslash-matritsasi)
     - 2.1.2 [Obuna Davriyligi va Paketlar Arxitekturasi](#212-obuna-davriyligi-va-paketlar-arxitekturasi)
     - 2.1.3 [Konversiya Triggorlari va Foydalanuvchini Premiumga O'tkazish Voronkasi](#213-konversiya-triggorlari-va-foydalanuvchini-premiumga-otkazish-voronkasi)
     - 2.1.4 [Obuna Holatlar Mashinasi (Subscription State Machine)](#214-obuna-holatlar-mashinasi-subscription-state-machine)
   - 2.2 [Model 2: Mahalliy Giper-Lokal Reklama va Homiylik Eslatmalari](#22-model-2-mahalliy-giper-lokal-reklama-va-homiylik-eslatmalari)
     - 2.2.1 [Foydalanuvchiga Xalaqit Bermaydigan, Qadriyat Qo'shuvchi Mahalliy Reklama](#221-foydalanuvchiga-xalaqit-bermaydigan-qadriyat-qoshuvchi-mahalliy-reklama)
     - 2.2.2 [B2B Hamkorlik va Homiylik Kanallari](#222-b2b-hamkorlik-va-homiylik-kanallari)
     - 2.2.3 [Reklama Kontenti Standartlari va Filtrlash](#223-reklama-kontenti-standartlari-va-filtrlash)
   - 2.3 [Model 3: Mikro-Billing va Pullik Qo'shimcha Xizmatlar (Pay-As-You-Go)](#23-model-3-mikro-billing-va-pullik-qoshimcha-xizmatlar-pay-as-you-go)
     - 2.3.1 [AI Task Breakdown (Sun'iy Intellekt Orqali Vazifalarni Bo'lish) To'plamlari](#231-ai-task-breakdown-suniy-intellekt-orqali-vazifalarni-bolish-toplamlari)
     - 2.3.2 [Favqulodda SMS Eslatma Paketlari (Eskiz.uz / PlayMobile)](#232-favqulodda-sms-eslatma-paketlari-eskizuz--playmobile)
     - 2.3.3 [Kengaytirilgan PDF va Excel Hosildorlik Hisobotlari Eksporti](#233-kengaytirilgan-pdf-va-excel-hosildorlik-hisobotlari-eksporti)
3. [O'rta Osiyo To'lov Tizimlari va Integratsiya Protokollari](#3-orta-osiyo-tolov-tizimlari-va-integratsiya-protokollari)
   - 3.1 [O'zbekiston To'lov Shlyuzlari](#31-ozbekiston-tolov-shlyuzlari)
     - 3.1.1 [Click.uz Shop API Integratsiyasi](#311-clickuz-shop-api-integratsiyasi)
     - 3.1.2 [Payme (Inspire Group / TBC Bank) JSON-RPC 2.0 Integratsiyasi](#312-payme-inspire-group--tbc-bank-json-rpc-20-integratsiyasi)
     - 3.1.3 [O'zbekiston Davlat Soliq Qo'mitasi (Soliq) OFD Fiskallashuvi va IKPU Kodi](#313-ozbekiston-davlat-soliq-qomitasi-soliq-ofd-fiskallashuvi-va-ikpu-kodi)
     - 3.1.4 [Uzum Pay (Uzum Bank) Merchant API va Dinamik QR Integratsiyasi](#314-uzum-pay-uzum-bank-merchant-api-va-dinamik-qr-integratsiyasi)
   - 3.2 [Qozog'iston To'lov Shlyuzlari](#32-qozogiston-tolov-shlyuzlari)
     - 3.2.1 [Kaspi Pay va Kaspi QR Integratsiyasi](#321-kaspi-pay-va-kaspi-qr-integratsiyasi)
     - 3.2.2 [Halyk Epay (Halyk Bank) Integratsiyasi](#322-halyk-epay-halyk-bank-integratsiyasi)
   - 3.3 [Telegram Stars (XTR) — Native Digital Goods Tizimi](#33-telegram-stars-xtr--native-digital-goods-tizimi)
     - 3.3.1 [Telegram Bot API 7.4+ Native Stars Arxitekturasi](#331-telegram-bot-api-74-native-stars-arxitekturasi)
     - 3.3.2 [Apple App Store va Google Play Qoidalariga Moslik](#332-apple-app-store-va-google-play-qoidalariga-moslik)
     - 3.3.3 [Yuridik Shaxs Talabisiz Butun Dunyodan To'lov Qabul Qilish va Fragment Orqali TON Ga Yechib Olish](#333-yuridik-shaxs-talabisiz-butun-dunyodan-tolov-qabul-qilish-va-fragment-orqali-ton-ga-yechib-olish)
4. [Mahalliy Valyutalardagi Narxlar Matritsasi va Unit Iqtisodiyot](#4-mahalliy-valyutalardagi-narxlar-matritsasi-va-unit-iqtisodiyot)
   - 4.1 [Ko'p Valyutali Rasmiy Narxlar Matritsasi](#41-kop-valyutali-rasmiy-narxlar-matritsasi)
   - 4.2 [Nolinchi Server Xarajati ($0/oy) va Unit Iqtisodiyot Tahlili](#42-nolinchi-server-xarajati-0oy-va-unit-iqtisodiyot-tahlili)
   - 4.3 [To'lov Shlyuzlari Komissiyalari va Sof Marja Taqqoslashi](#43-tolov-shlyuzlari-komissiyalari-va-sof-marja-taqqoslashi)
   - 4.4 [Foydalanuvchilar Soni Bo'yicha Moliyaviy Prognoz (1K, 5K, 25K MAU)](#44-foydalanuvchilar-soni-boyicha-moliyaviy-prognoz-1k-5k-25k-mau)
5. [Qonunchilik, Xavfsizlik va Litsenziyalash](#5-qonunchilik-xavfsizlik-va-litsenziyalash)
   - 5.1 [O'zbekiston va Qozog'istonda Shaxsiy Ma'lumotlarni Saqlash Talablari](#51-ozbekiston-va-qozogistonda-shaxsiy-malumotlarni-saqlash-talablari)
   - 5.2 [PCI-DSS Cheklovlari va Karta Ma'lumotlarini Saqlamaslik Siyosati](#52-pci-dss-cheklovlari-va-karta-malumotlarini-saqlamaslik-siyosati)
   - 5.3 [Anti-Fraud va Qaytarilgan Tranzaksiyalarni (Chargeback) Boshqarish](#53-anti-fraud-va-qaytarilgan-tranzaksiyalarni-chargeback-boshqarish)
6. [Amalga Oshirish Yo'l Xaritasi (FinTech Roadmap)](#6-amalga-oshirish-yol-xaritasi-fintech-roadmap)

---

# 1. O'rta Osiyo Bozori Tahlili va Iste'molchi Psixologiyasi

## 1.1 Mintaqada Telegramning Monopol O'rni va Raqamli Hayot Tarzi

O'rta Osiyo, xususan **O'zbekiston**, **Qozog'iston**, **Qirg'iziston** va **Tojikiston** bozorlarida Telegram messenjeri shunchaki shaxsiy yozishmalar vositasi emas, balki jamiyatning kundalik faoliyati, davlat xizmatlari, ommaviy axborot vositalari va elektron tijoratning asosiy raqamli markazi (de-fakto operatsion tizimi) hisoblanadi.

```
+--------------------------------------------------------------------------------------------------+
+                              O'RTA OSIYO TELEGRAM EKOTIZIMI VA AHAMIYATI                         +
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   +---------------------------------------+       +------------------------------------------+   |
|   |         O'ZBEKISTON RESPUBLIKASI      |       |          QOZOG'ISTON RESPUBLIKASI        |   |
|   | - Aholi: 37+ million                  |       | - Aholi: 20+ million                     |   |
|   | - Faol Telegram foydalanuvchilari:    |       | - Faol Telegram foydalanuvchilari:       |   |
|   |   25+ million (Aholining ~70%)        |       |   12+ million (Shaharliklar orasida 85%) |   |
|   | - Foydalanish maqsadi: Barcha xizmat, |       | - Foydalanish maqsadi: Biznes, yangilik, |   |
|   |   davlat idoralari botlari, e-tijorat |       |   professional hamjamiyatlar, Ta'lim     |   |
|   +---------------------------------------+       +------------------------------------------+   |
|                       |                                                 |                        |
|                       +-----------------------+-------------------------+                        |
|                                               |                                                  |
|                                               v                                                  |
|                      +--------------------------------------------------+                        |
|                      |        TELEGRAM MINI APPS (TMA) INQILOBI         |                        |
|                      | - App Store / Google Play dan yuklab olish yo'q  |                        |
|                      | - Ro'yxatdan o'tish (SMS / Parol) bosqichi yo'q  |                        |
|                      | - Telegram ichida bitta bosishda ochilish        |                        |
|                      | - Mahalliy to'lovlar bilan uzviy integratsiya    |                        |
|                      +--------------------------------------------------+                        |
+--------------------------------------------------------------------------------------------------+
```

### Bozorning o'ziga xos asosiy omillari:
1. **Yuklab olish to'sig'ining yo'qligi (Zero-Install Barrier)**:
   O'rta Osiyo foydalanuvchilarining aksariyati o'rta va arzon segmentdagi smartfonlardan (32GB-64GB xotiraga ega Android qurilmalar) foydalanadi. Foydalanuvchilar har bir kichik ehtiyoj uchun App Store yoki Google Play orqali alohida mobil ilova yuklab olishni xohlamaydi (xotira to'lib qolishi va sekin internet sababli). Telegram Mini App esa smartfonda qo'shimcha xotira egallamaydi va bir zumda ishga tushadi.
2. **Autentifikatsiya osonligi**:
   Standart mobil ilovalarda foydalanuvchidan telefon raqamini kiritish, SMS-kod kutish va parol o'ylab topish talab etiladi (bu 40-50% konversiya yo'qotilishiga sabab bo'ladi). Telegram bot va Mini App platformasida foydalanuvchi Telegram akkaunti orqali bir lahzada (avtomatik `initData` orqali) tizimga kiritiladi.
3. **Kun tartibining Telegram orqali boshqarilishi**:
   Ishchi yozishmalar, oilaviy guruhlar, universitet kanallari, do'kon buyurtmalari — barchasi bitta ilovada jamlangan. Foydalanuvchi doimiy ravishda Telegramda bo'lganligi sababli, eslatmalar va vazifalar botining o'z vaqtida keladigan bildirishnomalarini e'tibordan chetda qoldirish ehtimoli minimaldir.

---

## 1.2 Mahalliy To'lov Madaniyati va FinTex Ekologiyasi

O'rta Osiyoda bank kartalari tizimi va to'lov infratuzilmasi g'arb davlatlaridan tubdan farq qiladi. Bu yerda xalqaro kredit kartalari (Visa/Mastercard) ikkilamchi o'rinda bo'lib, ichki milliy to'lov tizimlari mutlaq ustunlikka ega.

### O'zbekiston: Uzcard va Humo duopoliyasi
- O'zbekiston Respublikasida barcha chakana to'lovlarning 98% dan ortig'i **Uzcard** va **Humo** milliy kartalari orqali amalga oshiriladi.
- Aholining deyarli 100% bank kartalari mobil to'lov ilovalariga (**Click**, **Payme**, **Uzum Bank**) ulangan.
- Har qanday raqamli mahsulot O'zbekistonda muvaffaqiyat qozonishi uchun ushbu uchta to'lov shlyuzidan kamida ikkitasini qo'llab-quvvatlashi shart.

### Qozog'iston: Kaspi.kz super-ilovasining mutlaq gegemonligi
- Qozog'iston Respublikasida aholining 75% dan ortig'i barcha to'lov va xaridlarni **Kaspi.kz** (Kaspi Gold, Kaspi QR) orqali bajaradi.
- Ikkilamchi to'lov vositasi sifatida **Halyk Bank** (Halyk QR va Epay tizimi) xizmat qiladi.
- Qozog'istonda har qanday xaridda QR-kod skanerlash yoki to'g'ridan-to'g'ri Kaspi ilovasiga o'tish (Deep Link) qabul qilingan umummilliy standartdir.

---

## 1.3 Mobil-First Mentalitet va "Bir Bosishda To'lash" Odatlari

O'rta Osiyo iste'molchisi veb-saytlarda 16 xonali karta raqami, amal qilish muddati va CVV kodini qo'lda kiritishdan qattiq hadiksiraydi (kiberfiribgarlik xavfi sababli). Buning o'rniga mintaqada quyidagi to'lov tajribalari shakllangan:
1. **Deep Link orqali mobil bankka sakrash**: Foydalanuvchi "Click orqali to'lash" tugmasini bosganda, telefonida o'rnatilgan Click yoki Payme ilovasi ochiladi.
2. **Biometrik tasdiqlash**: Foydalanuvchi karta raqamini kiritmasdan, FaceID yoki barmoq izi orqali to'lovni 2 soniya ichida tasdiqlaydi.
3. **SMS OTP talab qilinmaydi**: Mobil banking ichida to'lov qilingani sababli qo'shimcha SMS kod kutish asabiylashuvidan xalos bo'linadi.

Tizimimiz Telegram Mini App interfeysida to'lov tugmasini bosganda to'g'ridan-to'g'ri mobil to'lov ilovalarining Deep Link'lariga yo'naltiradi, bu esa to'lov konversiyasini **80-85% gacha** oshiradi.

---

## 1.4 Mikro-To'lovlarga Munosabat va Xarid Qobiliyati Psixologiyasi

O'rta Osiyo bozorida oylik daromad va sarf-xarajatlar xususiyatlaridan kelib chiqqan holda, raqamli mahsulotlarning narxlari psixologik qulay nuqtaga (sweet-spot) ega:
- **10,000 – 25,000 UZS (O'zbekiston)**: Bir chashka sifatli qahva yoki bitta tushlik narxi. Bunday narxdagi oylik obuna foydalanuvchi byudjetiga salbiy yuk bo'lmaydi va xarid qilish to'g'risida uzoq o'ylashni talab qilmaydi.
- **500 – 1,200 KZT (Qozog'iston)**: Qozog'iston aholisi uchun kundalik arzon xarid ekvivalenti.
- **Mikro-to'lovlar afzalligi**: Katta miqdordagi bir martalik to'lovlardan (masalan, $50-$100) ko'ra, 5,000 so'm yoki 19,000 so'mlik kichik tranzaksiyalar 10 barobar osonroq qabul qilinadi.

---

## 1.5 Xalqaro Tizimlarning (Stripe, PayPal) O'rta Osiyodagi Inqirozi

Ko'plab xalqaro startaplar O'rta Osiyo bozoriga Stripe yoki PayPal orqali kirishga urinib, muvaffaqiyatsizlikka uchraydi. Buning sabablari:
1. **Stripe O'zbekistonda yuridik shaxslarni ro'yxatdan o'tkazmaydi**: O'zbekiston rezidentlari Stripe orqali to'g'ridan-to'g'ri hisob ocholmaydi.
2. **PayPal O'zbekiston bank kartalariga pul qabul qilishni qo'llab-quvvatlamaydi**: Mahalliy foydalanuvchilar o'z kartalariga mablag' yechib ololmaydi.
3. **Valyuta konvertatsiyasi va komissiyalar**: Xalqaro shlyuzlar foydalanuvchining so'm kartasidan AQSH dollarida to'lov yechganda, mahalliy banklar 2-5% konvertatsiya komissiyasini ushlab qoladi.
4. **Uzcard va Humo qabul qilinmaydi**: Stripe va PayPal faqat xalqaro Visa/Mastercard bilan ishlaydi, aholining 90% dan ortig'i esa Uzcard/Humo kartalariga ega.

**Xulosa**: Loyiha muvaffaqiyati uchun faqat mahalliy shlyuzlar (**Click**, **Payme**, **Uzum Pay**, **Kaspi**) hamda Telegramning rasmiy ichki valyutasi bo'lgan **Telegram Stars** integratsiya qilinishi shart.

---

# 2. Kamida 3 Ta Aniq Monetizatsiya Modeli

Tizim barqaror daromad keltiruvchi ekotizimga aylanishi uchun bir-birini to'ldiruvchi uchta mustaqil monetizatsiya modeli loyihalashtirilgan.

```
+--------------------------------------------------------------------------------------------------+
|                            UCHTA ASOSIY MONETIZATSIYA USTUNI                                     |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   +------------------------------------+   +------------------------------------+   +------------------------------------+
|   |   MODEL 1: FREEMIUM + PREMIUM      |   |   MODEL 2: GIPER-LOKAL REKLAMA     |   |   MODEL 3: MIKRO-BILLING (PAYG)    |
|   | - 50 ta vazifa cheklovi            |   | - Foydali, qadriyatli takliflar    |   | - AI Task Breakdown paketlari      |
|   | - Cheksiz vazifa & RRULE           |   | - Ertalabki eslatmada kuponlar     |   | - Favqulodda SMS ogohlantirish     |
|   | - Ovozni matnga aylantirish (AI)   |   | - B2B homiylik kanallari & brend   |   | - PDF / Excel audit eksport        |
|   | - 1 oylik, 6 oylik, 1 yillik, Pass |   | - O'quv markazlari, kafelar        |   | - Bir martalik arzon xaridlar      |
|   +------------------------------------+   +------------------------------------+   +------------------------------------+
|                      \                                       |                                       /
|                       \                                      |                                      /
|                        v                                     v                                     v
|   +--------------------------------------------------------------------------------------------------+
|   |                      YAGONA YUQORI MARJALI FINANSIYAVIY STRATEGIYA                               |
|   |               (Server xarajati $0 -> Daromadning 70-98% sof foyda hisoblanadi)                   |
|   +--------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------+
```

---

## 2.1 Model 1: Freemium + Premium SaaS Obuna Modeli

Ushbu model loyihaning asosiy takrorlanuvchi daromad (MRR — Monthly Recurring Revenue) manbai hisoblanadi. Asosiy maqsad — yangi foydalanuvchiga barcha asosiy funksiyalarni bepul taqdim etib, uning odatlanishini (retention) ta'minlash va tizimdan faol foydalana boshlaganida qulaylik yaratuvchi "Power User" xususiyatlari orqali pullik obunaga o'tkazishdir.

### 2.1.1 Bepul (Free) va Pullik (Premium) Tariflar Taqqoslash Matritsasi

| Funksiya / Xususiyat | Bepul (Free) Tarif | Pullik (Premium) Tarif | Ta'rifi va Cheklov Sababi |
| :--- | :---: | :---: | :--- |
| **Faol vazifalar soni (Active Tasks)** | **Maksimal 50 ta vazifa** | **Cheksiz (Unlimited)** | Oddiy foydalanuvchiga yetarli, biznes/faol shaxslar limitga yetishi bilan Premiumga o'tadi |
| **Vazifani takrorlash mantig'i (RRULE)** | Oddiy takrorlash (faqat har kuni) | **Murakkab RRULE qoidalari** (ish kunlari, hafta kunlari, oyning ma'lum haftasi, maxsus intervallar) | Ish jadvali murakkab mutaxassislar va tadbirkorlar uchun muhim qiymat |
| **Audio xabarlarni matnga aylantirish (Voice-to-Task)** | Mavjud emas (0 ta) | **Oyiga 100 ta ovozli xabar** (O'zbek, Rus, Ingliz tillarida ovoz orqali vazifa yaratish) | Harakatda, mashinada yoki shoshilinchda ovozli xabar yuborib vazifa kiritish qulayligi |
| **Taqvim integratsiyasi (Calendar Sync)** | Mavjud emas | **Google Calendar va Apple Calendar** bilan 2 tomonlama avtomatik sinxronizatsiya | Vazifalarni tashqi korporativ taqvimlarda ko'rish imkoniyati |
| **Rangli mavzular va moslashtirish** | Standart Telegram mavzusi | **8 ta maxsus dizayn mavzusi**, shaxsiy fon va shriftlar | Shaxsiy did va qulaylikni qadrlovchilar uchun estetik ustunlik |
| **Jamoaviy va Oilaviy vazifalar doskasi** | 1 ta shaxsiy doska | **Cheksiz umumiy doskalar** (Oila a'zolari, hamkasblar bilan birgalikda boshqarish) | Bir nechta foydalanuvchini bitta to'lov orqali jalb qilish va saqlab qolish (stickiness) |
| **Eslatmalarni kechiktirish (Snooze)** | Faqat 15 daqiqaga kechiktirish | **Moslashuvchan kechiktirish** (15m, 1s, ertaga ertalab, dam olish kuniga) | Vaqtni qat'iy boshqarish imkoni |
| **Fayl va rasm biriktirish** | 1 ta rasm (maks 2MB) | **Cheksiz fayl va hujjatlar** (har biriga 20MB gacha) | Vazifaga hisobot yoki cheklarni ilova qilish |
| **Texnik qo'llab-quvvatlash** | Jamoat forumi / FAQ | **Tezkor VIP qo'llab-quvvatlash** (Priority Telegram Support) | 1 soat ichida muammolarni hal qilish kafolati |

### 2.1.2 Obuna Davriyligi va Paketlar Arxitekturasi

Obuna paketlari foydalanuvchining moliyaviy imkoniyatlari va sadoqat darajasiga moslashtirilgan 4 ta asosiy davrga bo'linadi:

1. **1 Oylik Obuna (Standard Monthly)**:
   - *O'zbekiston*: **19,000 so'm / oy**
   - *Qozog'iston*: **990 KZT / oy**
   - *Telegram Stars*: **75 Stars / oy**
   - *Maqsadi*: Past kirish to'sig'i, foydalanuvchi tizimni to'liq quvvatda sinab ko'rishi uchun qulay oylik to'lov.
2. **6 Oylik Obuna (Semi-Annual Saver)**:
   - *O'zbekiston*: **99,000 so'm / 6 oy** (oyiga ~16,500 so'm, 13% tejamkorlik)
   - *Qozog'iston*: **4,990 KZT / 6 oy** (oyiga ~831 KZT, 16% tejamkorlik)
   - *Telegram Stars*: **390 Stars / 6 oy** (13% tejamkorlik)
   - *Maqsadi*: O'rta muddatli rejalashtirish, mavsumiy foydalanuvchilar uchun foydali taklif.
3. **1 Yillik Obuna (Annual Best Value)**:
   - *O'zbekiston*: **169,000 so'm / yil** (oyiga ~14,000 so'm, 26% tejamkorlik)
   - *Qozog'iston*: **8,990 KZT / yil** (oyiga ~749 KZT, 24% tejamkorlik)
   - *Telegram Stars*: **690 Stars / yil** (23% tejamkorlik)
   - *Maqsadi*: Eng yuqori LTV (Customer Lifetime Value) beruvchi, jamoa uchun eng barqaror daromad keltiruvchi paket.
4. **Umrbod Litsenziya (Lifetime "Founder Pass")**:
   - *O'zbekiston*: **299,000 so'm** (bir martalik to'lov)
   - *Qozog'iston*: **15,900 KZT** (bir martalik to'lov)
   - *Telegram Stars*: **1,200 Stars** (bir martalik to'lov)
   - *Maqsadi*: Dastlabki 1,000 nafar sadoqatli foydalanuvchilarni jalb qilish, loyihaning dastlabki bosqichida tezkor naqd pul oqimi (Cash Flow) hosil qilish.

### 2.1.3 Konversiya Triggorlari va Foydalanuvchini Premiumga O'tkazish Voronkasi

Foydalanuvchini agressiv yoki asabiylashtiruvchi reklama orqali emas, balki tabiiy ehtiyoj yuzaga kelganda to'lovga yo'naltirish mexanizmi yo'lga qo'yiladi:

```
[ Foydalanuvchi Botga Kirdi ]
           |
           v
[ 1-qadam: 7 Kunlik Bepul Premium Trial (Karta talab qilinmaydi) ]
           |
           v
[ Trial tugadi -> Avtomatik ravishda Bepul (Free) tarifga o'tish ]
           |
           +---> Trigger A: 50 ta vazifa limitiga yetish (Paywall paydo bo'ladi)
           |
           +---> Trigger B: Ovozli xabar yuborish (Voice-to-Text demo tugaydi)
           |
           +---> Trigger C: Google Calendar tugmasini bosish
           |
           v
[ 1-bosishda Mahalliy To'lov (Click / Payme / Stars / Kaspi) ] -> [ Premium Faollashdi ]
```

1. **7 Kunlik Sinov Davri (No-Card Free Trial)**:
   Yangi foydalanuvchi botga kirganda unga bank kartasi kiritishni talab qilmasdan 7 kunga to'liq Premium funksiyalar taqdim etiladi. Foydalanuvchi qulaylikka o'rgangach, bepul tarifga qaytganda cheklovlarni yaqqol his qiladi.
2. **50-Vazifa Cheklovi Bloki**:
   Foydalanuvchi 51-vazifani kiritmoqchi bo'lganda, interaktiv Mini App oynasi chiqadi:
   > *"Siz bepul tarifdagi 50 ta vazifa chegarasiga yetdingiz! 🚀 Avvalgi vazifalaringiz xavfsiz saqlanmoqda. Cheksiz vazifalar va murakkab eslatmalar uchun Premiumga o'ting."*
   > Tugma: `[ 💎 Oyiga 19,000 so'mga Premium olish ]`
3. **RRULE Teaseri**:
   Foydalanuvchi takroriy eslatma o'rnatishda "Faqat dushanbadan jumagacha" tugmasini bosganda, kichik qulflangan belgi ko'rinadi va Premium taklif oynasi ochiladi.

### 2.1.4 Obuna Holatlar Mashinasi (Subscription State Machine)

Obuna ma'lumotlar bazasida qat'iy holatlar asosida boshqariladi:

```
        +---------------+
        |  0: FREE_TIER | <-----------------------------------+
        +---------------+                                     |
               |                                              |
               | Foydalanuvchi Trial oldi                     |
               v                                              |
        +---------------+                                     |
        |  1: IN_TRIAL  |                                     |
        +---------------+                                     |
               |                                              |
      +--------+--------+                                     |
      |                 |                                     |
      | Muddat tugadi   | To'lov qilindi                      |
      v                 v                                     |
+---------------+ +---------------+                           |
|4:TRIAL_EXPIRED| |   2: ACTIVE   |                           |
+---------------+ +---------------+                           |
      |                 |                                     |
      | To'lov qildi    | Obuna muddati tugadi                |
      +-------->        v                                     |
                 +-----------------+                          |
                 | 3: GRACE_PERIOD | (48 soatlik imtiyoz)     |
                 +-----------------+                          |
                        |                                     |
                        | 48 soat ichida to'lov qilinmadi     |
                        v                                     |
                 +-----------------+                          |
                 |   5: EXPIRED    | -------------------------+
                 +-----------------+ (Vazifalar o'chirilmaydi,
                                      faqat 50 tasi ko'rinadi)
```

- **Grace Period (48 soat)**: Foydalanuvchining kartasida mablag' yetmay qolsa, xizmat bir zumda to'xtatilmaydi. Unga eslatma yuboriladi:
  > *"Premium obunangiz muddati tugadi. Xizmatlaringiz to'xtab qolmasligi uchun 48 soatlik imtiyozli davr berildi. Hozir yangilang: [To'lov qilish]"*
- **Xavfsiz Saqlash Kafolati**: Bepul tarifga tushganda ham foydalanuvchining avvalgi 50 tadan ortiq vazifalari bazadan o'chirib yuborilmaydi; faqat yangi vazifa qo'shish vaqtincha cheklanadi.

---

## 2.2 Model 2: Mahalliy Giper-Lokal Reklama va Homiylik Eslatmalari

Foydalanuvchilarning taxminan 85-92% qismi bepul tarifda qoladi. Ushbu ulkan auditoriyani monetizatsiya qilish uchun foydalanuvchini asabiylashtirmaydigan, uning hayotiga real foyda keltiruvchi mahalliy reklama modeli kiritiladi.

### 2.2.1 Foydalanuvchiga Xalaqit Bermaydigan, Qadriyat Qo'shuvchi Mahalliy Reklama

Biz invaziv, butun ekranni to'sib qo'yuvchi pop-up reklamalarni qat'iyan taqiqlaymiz. Buning o'rniga "Native & Contextual Utility" yondashuvi qo'llaniladi:
1. **Mini App Pastki Qismidagi Yengil Banner (50px Banner)**:
   Mini App dashboardining eng pastki qismida ko'zga tashlanmaydigan, toza dizayndagi mikro-banner joylashadi. Premium foydalanuvchilarda bu banner butunlay o'chiriladi.
2. **Qadriyat Qo'shuvchi Ertalabki Homiylik Xabari (Morning Digest Sponsorship)**:
   Har kuni soat 08:30 da foydalanuvchiga uning bugungi rejalari keltirilgan "Kunlik Xulosa" xabari yuboriladi. Xabarning eng tagida homiyning foydali taklifi ilova qilinadi:
   
   ```
   🌅 Xayrli tong, Alisher!
   Bugungi rejalaringiz (4 ta vazifa):
   1. 09:30 - Loyiha hisobotini topshirish
   2. 12:00 - Mijoz bilan uchrashuv
   3. 16:00 - Ingliz tili darsi
   4. 19:30 - Sport zalga borish

   ☕️ Kunni sermahsul boshlang! "Coffee House" qahvaxonasida 
   barcha qahvalarga 15% chegirma. Promokod: TASKBOT
   📍 Toshkent, Amir Temur ko'chasi, 42
   ```

### 2.2.2 B2B Hamkorlik va Homiylik Kanallari

Mahalliy tadbirkorlar va ta'lim markazlari bilan to'g'ridan-to'g'ri oylik homiylik shartnomalari:
1. **O'quv Markazlari va IT Akademiyalar (Najot Ta'lim, PDP, Cambridge, Everest)**:
   Vazifalar botining auditoriyasi asosan talabalar, frilanserlar va xodimlardan iborat. "Ta'lim" yoki "Shaxsiy rivojlanish" kategoriyasidagi vazifalarni bajargan foydalanuvchilarga maqsadli chegirma va grant e'lonlari ko'rsatiladi.
2. **Kitob Do'konlari va Yetkazib Berish Xizmatlari (Asaxiy, Uzum Tezkor, Express24)**:
   "Kitob o'qish" yoki "Xarid qilish" eslatmalari uchun Asaxiy.uz promokodlari integratsiyasi orqali har bir xarid uchun CPA (Cost Per Action / 5-10% keshbek) daromadi olinadi.
3. **Kompaniyalar Uchun Brendlangan Ishchi Tablar (Co-Branded Workspace)**:
   Kichik kompaniya yoki o'quv guruhi o'z xodimlari uchun bot ichida alohida logotip va ranglarga ega korporativ vazifalar boshqaruvini yoqtirishni istasa, oylik **500,000 – 1,500,000 so'm** miqdorida B2B obuna to'laydi.

### 2.2.3 Reklama Kontenti Standartlari va Filtrlash
- Qimor o'yinlari (1xBet, Mostbet va hk.), moliyaviy piramidalar, kripto-feyklar va shubhali xizmatlar qat'iyan taqiqlanadi.
- Reklamalar faqat sifatli, qonuniy va mahalliy bizneslarga tegishli bo'lishi tizimga bo'lgan ishonchni kafolatlaydi.

---

## 2.3 Model 3: Mikro-Billing va Pullik Qo'shimcha Xizmatlar (Pay-As-You-Go)

Oylik doimiy obunani xohlamaydigan, lekin aniq bir qo'shimcha xizmatga muhtoj foydalanuvchilar uchun bir martalik arzon to'lov paketlari.

### 2.3.1 AI Task Breakdown (Sun'iy Intellekt Orqali Vazifalarni Bo'lish) To'plamlari

Ko'p hollarda foydalanuvchilar ulkan va noaniq maqsadlarni qanday rejalashtirishni bilmaydi (masalan: *"IELTS 7.5 olish"*, *"Yangi kvartiraga ko'chib o'tish"*, *"Mini App dasturlash"*).
- **AI Task Breakdown imkoniyati**: Foydalanuvchi bitta tugmani bosadi va sun'iy intellekt bu katta vazifani 7-30 kunlik ketma-ket, aniq soatli kichik qadamlarga ajratib, botga jadval qilib joylashtiradi.
- **Mikro-paketlar narxi**:
  - **10 ta AI so'rov to'plami**: **5,000 so'm** (~$0.40) yoki **20 Telegram Stars**
  - **50 ta AI so'rov to'plami**: **19,000 so'm** (~$1.50) yoki **75 Telegram Stars**
- Ushbu yondashuv orqali foydalanuvchi arzon to'lov evaziga o'zining murakkab rejasini bir soniyada tayyor qilib oladi.

### 2.3.2 Favqulodda SMS Eslatma Paketlari (Eskiz.uz / PlayMobile)

O'rta Osiyoning tog'li hududlarida, chekka tumanlarda yoki yo'lda mobil internet vaqtincha uzilishi mumkin. Shuningdek, ko'p foydalanuvchilar batareyani tejash uchun internetni o'chirib qo'yadi.
- **SMS Ogohlantirish Funktsiyasi**: Agar vazifa o'ta muhim (Critical / High Priority) deb belgilangan bo'lsa va Telegram xabari yetib bormasa, tizim mahalliy SMS shlyuz (Eskiz.uz yoki PlayMobile) orqali to'g'ridan-to'g'ri foydalanuvchining telefon raqamiga favqulodda SMS yuboradi.
- **SMS Paketlar Narxi**:
  - **10 ta SMS krediti**: **3,000 so'm** (SMS tannarxi Eskiz.uz da ~70-85 so'm bo'lib, loyihaga 70% sof foyda qoladi).
  - **50 ta SMS krediti**: **12,000 so'm**.

### 2.3.3 Kengaytirilgan PDF va Excel Hosildorlik Hisobotlari Eksporti

Frilanserlar, rahbarlar va o'z vaqtini qat'iy hisoblaydigan mutaxassislar uchun bajargan ishlari to'g'risida chiroyli dizayndagi, infografikali hisobot talab etiladi.
- **PDF/Excel Hisobot**: Haftalik yoki oylik bajarilgan vazifalar soni, kechiktirilganlar foizi, unumdorlik soatlari va toifalar grafigi.
- **Eksport narxi**: Bitta to'liq tahliliy hisobotni eksport qilish — **2,000 so'm** yoki Premium obunachilarga tekin.

---

# 3. O'rta Osiyo To'lov Tizimlari va Integratsiya Protokollari

Ushbu bo'limda O'rta Osiyoning yetakchi fintex platformalari bilan ishlab chiqarish (production) darajasida integratsiya qilishning to'liq protokollari va dasturiy kod namunalari keltirilgan.

```
+--------------------------------------------------------------------------------------------------+
|                            MINTAQAVIY TO'LOV ARXITEKTURASI TOPOLOGIYASI                          |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   +--------------------------+   +--------------------------+   +----------------------------+   |
|   |   O'ZBEKISTON SHLYUZLARI |   |   QOZOG'ISTON SHLYUZLARI |   |   XALQARO & BOT NATIVE     |   |
|   |  - Click.uz (Shop API)   |   |  - Kaspi Pay / Kaspi QR  |   |  - Telegram Stars (XTR)    |   |
|   |  - Payme (JSON-RPC 2.0)  |   |  - Halyk Epay (Halyk QR) |   |  - Fragment.com -> TON     |   |
|   |  - Soliq OFD Fiskallashuv|   |                          |   |  - Apple / Google xavfsiz  |   |
|   |  - Uzum Pay (Merchant)   |   |                          |   |                            |   |
|   +--------------------------+   +--------------------------+   +----------------------------+   |
|                 \                              |                              /                  |
|                  \                             |                             /                   |
|                   v                            v                            v                    |
|       +-------------------------------------------------------------------------------+          |
|       |               CLOUDFLARE WORKERS TO'LOV GATEWAY KONTROLLERI                   |          |
|       |  - HMAC-SHA256 & MD5 Raqamli Imzo Validatsiyasi                               |          |
|       |  - Idempotentlik va Takrorlanishdan Himoya (SETNX / UUID)                     |          |
|       |  - Soliq IKPU 10899001001000000 Fiskal Chek Generatsiyasi                     |          |
|       +-------------------------------------------------------------------------------+          |
|                                                |                                                 |
|                                                v                                                 |
|       +-------------------------------------------------------------------------------+          |
|       |            SUPABASE POSTGRESQL (TRANZAKSIYALAR VA OBUNALAR BAZASI)            |          |
|       |  - user_subscriptions jadvali (state: ACTIVE, expire_at: NOW() + INTERVAL)    |          |
|       +-------------------------------------------------------------------------------+          |
+--------------------------------------------------------------------------------------------------+
```

---

## 3.1 O'zbekiston To'lov Shlyuzlari

### 3.1.1 Click.uz Shop API Integratsiyasi

Click tizimi tranzaksiyalarning xavfsizligi va mablag'larning to'g'ri hisobdan chiqarilishini ta'minlash uchun ikki bosqichli (**Prepare** va **Complete**) modeldan foydalanadi.

#### Tranzaksiya Bosqichlari:
1. **Prepare (`action = 0`)**: Click serveri savdogar (TaskBot) backendiga so'rov yuborib, ushbu hisob/foydalanuvchi mavjudligini, to'lov miqdori to'g'riligini va buyurtma avval to'lanmaganligini tekshiradi.
2. **Complete (`action = 1`)**: Click foydalanuvchining kartasidan pulni yechib oladi va savdogarga yakuniy xabarnoma jo'natadi. Savdogar Premium obunani faollashtiradi va tasdiq javobini qaytaradi.

```
Foydalanuvchi                Click.uz Tizimi                TaskBot Backend
     |                              |                              |
     |--- 1. "Click orqali to'lash"->|                              |
     |                              |--- 2. POST /api/click ------>|
     |                              |    (action=0: Prepare)       |
     |                              |<-- 3. error=0 (Tayyor) ------|
     |--- 4. To'lovni tasdiqlash -->|                              |
     |                              |--- 5. POST /api/click ------>|
     |                              |    (action=1: Complete)      |
     |                              |<-- 6. error=0 (Muvaffaqiyat)-|
     |<-- 7. Premium Faollashdi ----|                              |
```

#### Raqamli Imzo (MD5 Sign String) Hisoblash Formulasi:
Savdogar har bir kelgan so'rovning Click tomonidan yuborilganligini tekshirish uchun quyidagi ketma-ketlikda MD5 heshini hisoblaydi:

$$\text{SignString} = \text{MD5}(\text{click\_trans\_id} + \text{service\_id} + \text{SECRET\_KEY} + \text{merchant\_trans\_id} + \text{amount} + \text{action} + \text{sign\_time})$$

Agar hisoblangan hesh `sign_string` parametri bilan mos kelmasa, so'rov darhol rad etiladi (`error = -1`).

#### Click Shop API So'rov Parametrlari:
| Parametr Nomi | Turi | Tavsifi |
| :--- | :--- | :--- |
| `click_trans_id` | Long | Click tizimidagi unikal tranzaksiya identifikatori |
| `service_id` | Integer | Click tomonidan savdogarga berilgan servis raqami |
| `merchant_trans_id` | String | TaskBot tizimidagi ichki hisob-faktura ID (masalan: `SUB_UZ_84920`) |
| `amount` | Float / String | To'lov summasi (so'mda, masalan: `19000.00`) |
| `action` | Integer | `0` = Prepare (Tayyorgarlik), `1` = Complete (Yakunlash) |
| `error` | Integer | Click tomonidan uzatilgan status kodi |
| `error_note` | String | Xatolik tafsiloti |
| `sign_time` | String | So'rov vaqti formati: `YYYY-MM-DD HH:mm:ss` |
| `sign_string` | String | Click MD5 raqamli imzosi |

#### Click Standart Xatolik Kodlari (Error Codes):
| Kod | Nomlanishi | Qachon Qaytariladi |
| :---: | :--- | :--- |
| **0** | **Success** | Amaliyot muvaffaqiyatli bajarildi |
| **-1** | **SIGN_CHECK_FAILED** | MD5 raqamli imzo tekshiruvdan o'tmadi (maxfiy kalit noto'g'ri) |
| **-2** | **INCORRECT_AMOUNT** | To'lov summasi tarif narxiga to'g'ri kelmadi |
| **-3** | **ACTION_NOT_FOUND** | Noto'g'ri action yuborildi (faqat 0 va 1 qo'llab-quvvatlanadi) |
| **-4** | **ALREADY_PAID** | Ushbu tranzaksiya avval to'lab bo'lingan |
| **-5** | **USER_NOT_FOUND** | Foydalanuvchi yoki hisob-faktura tizimda topilmadi |
| **-6** | **TRANSACTION_CANCELLED**| Tranzaksiya bekor qilingan |

#### TypeScript / Cloudflare Workers Uchun Ishlab Chiqarish Implementatsiyasi:
```typescript
import { createHash } from 'node:crypto';

interface ClickPayload {
  click_trans_id: string;
  service_id: string;
  merchant_trans_id: string;
  merchant_prepare_id?: string;
  amount: string;
  action: string;
  error: string;
  error_note: string;
  sign_time: string;
  sign_string: string;
}

export async function handleClickWebhook(payload: ClickPayload, secretKey: string, db: any) {
  // 1. MD5 Raqamli imzoni tekshirish
  const rawString = `${payload.click_trans_id}${payload.service_id}${secretKey}` +
                    `${payload.merchant_trans_id}` +
                    `${payload.action === '1' ? payload.merchant_prepare_id : ''}` +
                    `${payload.amount}${payload.action}${payload.sign_time}`;
  
  const expectedSign = createHash('md5').update(rawString).digest('hex');

  if (expectedSign.toLowerCase() !== payload.sign_string.toLowerCase()) {
    return {
      error: -1,
      error_note: 'SIGN_CHECK_FAILED: Raqamli imzo xato'
    };
  }

  // 2. Buyurtmani bazadan qidirish
  const order = await db.query('SELECT * FROM orders WHERE id = $1', [payload.merchant_trans_id]);
  if (!order) {
    return { error: -5, error_note: 'USER_NOT_FOUND: Buyurtma topilmadi' };
  }

  // 3. Summani tekshirish
  if (parseFloat(order.amount) !== parseFloat(payload.amount)) {
    return { error: -2, error_note: 'INCORRECT_AMOUNT: Summa mos kelmadi' };
  }

  // 4. Action = 0 (Prepare) bosqichi
  if (payload.action === '0') {
    if (order.status === 'PAID') {
      return { error: -4, error_note: 'ALREADY_PAID: Buyurtma to‘langan' };
    }
    // Tranzaksiyani tayyorgarlik holatiga o'tkazish
    const prepareId = Date.now().toString();
    await db.query('UPDATE orders SET status = $1, prepare_id = $2 WHERE id = $3', 
                    ['PREPARED', prepareId, order.id]);

    return {
      click_trans_id: payload.click_trans_id,
      merchant_trans_id: payload.merchant_trans_id,
      merchant_prepare_id: prepareId,
      error: 0,
      error_note: 'Success'
    };
  }

  // 5. Action = 1 (Complete) bosqichi
  if (payload.action === '1') {
    if (order.status === 'PAID') {
      return {
        click_trans_id: payload.click_trans_id,
        merchant_trans_id: payload.merchant_trans_id,
        merchant_confirm_id: order.prepare_id,
        error: 0,
        error_note: 'Already processed'
      };
    }

    // Obunani faollashtirish (Premium berish)
    await db.query('UPDATE orders SET status = $1 WHERE id = $2', ['PAID', order.id]);
    await db.query(
      'INSERT INTO user_subscriptions (user_id, plan, status, expires_at) ' +
      'VALUES ($1, $2, $3, NOW() + INTERVAL $4) ' +
      'ON CONFLICT (user_id) DO UPDATE SET status = $3, expires_at = user_subscriptions.expires_at + INTERVAL $4',
      [order.user_id, order.plan, 'ACTIVE', order.duration_interval]
    );

    return {
      click_trans_id: payload.click_trans_id,
      merchant_trans_id: payload.merchant_trans_id,
      merchant_confirm_id: payload.merchant_prepare_id,
      error: 0,
      error_note: 'Success'
    };
  }

  return { error: -3, error_note: 'ACTION_NOT_FOUND' };
}
```

---

### 3.1.2 Payme (Inspire Group / TBC Bank) JSON-RPC 2.0 Integratsiyasi

Payme savdogarlar uchun eng qat'iy va standartlashtirilgan xalqaro **JSON-RPC 2.0** protokolini qo'llaydi. Har bir so'rov HTTPS orqali keladi va `Authorization: Basic <base64("Paycom:" + MERCHANT_KEY)>` sarlavhasi bilan himoyalangan bo'ladi.

#### Talab Qilingan 6 Ta JSON-RPC Metodlari:
1. `CheckPerformTransaction`: Foydalanuvchi hisobi to'lovga tayyormi va summa to'g'rimi?
2. `CreateTransaction`: Tranzaksiya yozuvini yaratish va `state = 1` (Yaratildi) holatiga o'tkazish.
3. `PerformTransaction`: Pul muvaffaqiyatli yechildi, `state = 2` (Yakunlandi) holatiga o'tkazish, Premium berish.
4. `CancelTransaction`: To'lovni bekor qilish yoki qaytarish (`state = -1` yoki `-2`).
5. `CheckTransaction`: Tranzaksiyaning hozirgi holati va fiskal chek parametrlarini tekshirish.
6. `GetStatement`: Buxgalteriya solishtiruvi uchun belgilangan vaqt oralig'idagi barcha operatsiyalarni olish.

#### Payme Tranzaksiya Holatlar Mashinasi (State Lifecycle):
```
             [0: Mavjud emas]
                    |
                    v (CreateTransaction)
             [1: STATE_IN_PROGRESS] ---------------------------+
                    |                                          | (Cancel: Reason 1..5)
                    v (PerformTransaction)                     v
             [2: STATE_DONE]                             [-1: CANCELLED_BEFORE]
                    |
                    v (CancelTransaction)
             [-2: CANCELLED_AFTER_PAYMENT]
```

#### Payme Xatolik Kodlari (JSON-RPC Error Codes):
- `-32504`: Avtorizatsiya xatosi (Login yoki Parol noto'g'ri).
- `-31001`: Buyurtma summasi noto'g'ri.
- `-31050`: Foydalanuvchi / Buyurtma topilmadi.
- `-31008`: Tranzaksiyani bajarish mumkin emas (vaqt tugagan yoki bekor qilingan).
- `-31007`: Tranzaksiya allaqachon bajarilgan.

---

### 3.1.3 O'zbekiston Davlat Soliq Qo'mitasi (Soliq) OFD Fiskallashuvi va IKPU Kodi

O'zbekiston Respublikasi Soliq kodeksi va Vazirlar Mahkamasining qarorlariga muvofiq, aholidan elektron tarzda qabul qilingan barcha to'lovlar Davlat Soliq Qo'mitasining Onlayn Fiskal Ma'lumotlar Operatori (OFD) tizimida ro'yxatdan o'tkazilishi va xaridorga rasmiy elektron chek taqdim etilishi shart.

Payme integratsiyasida chek avtomatik shakllanishi uchun `CheckPerformTransaction` va `CreateTransaction` javoblariga maxsus `detail.receipt` obyekti joylashtiriladi:
- **Dasturiy Ta'minot Xizmati Uchun Rasmiy IKPU (MXIK) Kodi**: `10899001001000000` (Axborot texnologiyalari va dasturiy ta'minot xizmatlari).
- **QQS (VAT) Stavka Integratsiyasi**: Dasturchi QQS to'lovchisi bo'lmasa `0%`, aks holda `12%` etib belgilanadi.
- **Tiyinlar Bilan Hisob-kitob**: Payme tizimida barcha summalar tiyinlarda uzatiladi (19,000 so'm = 1,900,000 tiyin).

#### Payme JSON-RPC 2.0 To'liq Fiskal Javob Namunasi:
```json
{
  "jsonrpc": "2.0",
  "id": 123456,
  "result": {
    "allow": true,
    "detail": {
      "receipt": {
        "items": [
          {
            "title": "Telegram Task Bot: 1 Oylik Premium Obuna",
            "price": 1900000,
            "count": 1,
            "code": "10899001001000000",
            "units": 241092,
            "vat_percent": 0,
            "package_code": "123456"
          }
        ]
      }
    }
  }
}
```

---

### 3.1.4 Uzum Pay (Uzum Bank) Merchant API va Dinamik QR Integratsiyasi

Uzum ekotizimi (Uzum Market, Uzum Tezkor) O'zbekistonda eng tez o'sayotgan fintex tarmog'idir.
1. **OAuth2 Bearer Avtorizatsiyasi**: Savdogar `client_id` va `client_secret` orqali vaqtinchalik Bearer token oladi.
2. **Dinamik To'lov Havolasi va QR**:
   - Backend `POST https://api.uzumpay.uz/api/v1/merchant/invoice/create` manziliga buyurtma ma'lumotlarini yuboradi.
   - Javobda qaytgan `payment_url` va `qr_code_url` olinadi.
3. **Mini App Checkout Tajribasi**:
   - Foydalanuvchiga to'lov tugmasi ko'rsatiladi: `https://pay.uzum.uz/pay?invoice_id=...`
   - Mini App ochilgan qurilmada to'g'ridan-to'g'ri Uzum Bank ilovasi ishga tushadi va foydalanuvchi biometriya orqali to'lovni yakunlaydi.
4. **Webhook Xabarnoma**: To'lov o'tgach, Uzum serveri TaskBot webhookiga HMAC-SHA256 imzosi bilan xabar yuboradi va subscription faollashadi.

---

## 3.2 Qozog'iston To'lov Shlyuzlari

### 3.2.1 Kaspi Pay va Kaspi QR Integratsiyasi

Qozog'istonda muvaffaqiyat qozonish uchun Kaspi Pay yagona eng muhim to'lov vositasidir. Kaspi yopiq va yuqori darajada xavfsiz ekotizimga ega.

#### Integratsiya Bosqichlari:
1. **Invoice Yaratish (Create Order)**:
   - TaskBot backend xizmati Kaspi Pay Merchant API ga so'rov yuborib, buyurtma ID, narxi (KZT da) va tavsifini uzatadi.
   - Kaspi tizimi unikal `order_id` va to'lov havolasini generatsiya qiladi.
2. **Deep Link Orqali Kaspi Ilovasini Ochish**:
   - Telegram Mini App ichida foydalanuvchi "Kaspi orqali to'lash (990 ₸)" tugmasini bosadi.
   - TMA Native SDK orqali deep link chaqiriladi:
     ```javascript
     window.Telegram.WebApp.openLink(`https://kaspi.kz/pay?order_id=${orderId}`);
     // yoki bevosita mobil app protokoli:
     window.location.href = `kaspi://pay?order_id=${orderId}`;
     ```
3. **Kaspi QR Generatsiyasi (Desktop / Web versiyalar uchun)**:
   - Agar foydalanuvchi Telegram Desktop yoki Web versiyada bo'lsa, Mini App ekranida dinamik Kaspi QR kodi chiziladi. Foydalanuvchi smartfoni orqali Kaspi ilovasi kamerasini tutib, to'lovni 3 soniyada amalga oshiradi.
4. **Status Tekshirish va Callback**:
   - Kaspi Merchant Webhook TaskBot serveriga to'lov yakunlanganligini bildiradi.
   - Server tranzaksiyani tekshirib, foydalanuvchiga darhol bot orqali tabrik xabarini jo'natadi.

---

### 3.2.2 Halyk Epay (Halyk Bank) Integratsiyasi

Halyk Bank Qozog'istonning ikkinchi yirik banki bo'lib, xalqaro Visa va Mastercard kartalarini to'g'ridan-to'g'ri qabul qilish imkonini beradi:
1. **Protokol**: RESTful JSON API + OAuth 2.0.
2. **Halyk QR va Kartalar**: Foydalanuvchi ham Halyk ilovasi orqali QR kod bilan, ham istalgan xalqaro karta orqali to'lay oladi.
3. **HMAC-SHA256 Imzo**: Halyk Epay tomonidan yuborilgan har bir javob bankning ochiq kaliti (Public Key) va SHA-256 imzosi yordamida verifikatsiya qilinadi.

---

## 3.3 Telegram Stars (XTR) — Native Digital Goods Tizimi

### 3.3.1 Telegram Bot API 7.4+ Native Stars Arxitekturasi

2024-yil iyun oyida Telegram messenjeri o'zining ichki raqamli valyutasi — **Telegram Stars (XTR)** tizimini taqdim etdi. Bu raqamli xizmatlar, obunalar va bot funksiyalarini sotish uchun rasmiy vositadir.

```
+------------+                +------------------+            +-------------------+            +---------------+
| TMA Client |                | Backend Service  |            | Telegram Bot API  |            | Fragment / TON|
+------------+                +------------------+            +-------------------+            +---------------+
      |                                |                                |                             |
      |-- 1. "75 Starsga Premium" ---->|                                |                             |
      |                                |-- 2. createInvoiceLink ------->|                             |
      |                                |      (currency: "XTR")         |                             |
      |                                |<-- 3. invoice_link ------------|                             |
      |<-- 4. openInvoice(link) -------|                                |                             |
      |                                                                 |                             |
      |-- 5. Native Telegram Stars Dialogida to'lovni tasdiqlash ------>|                             |
      |                                                                 |                             |
      |                                |<-- 6. pre_checkout_query ------|                             |
      |                                |-- 7. answerPreCheckoutQuery -->|                             |
      |                                |      (ok: true, 10s ichida)    |                             |
      |                                                                 |                             |
      |                                |<-- 8. successful_payment ------|                             |
      |                                |      (Premium berish)          |                             |
      |<-- 9. TMA interfeysi yangilandi                                |                             |
      |                                                                 |                             |
      |                                                                 | (21 kundan so'ng)           |
      |                                                                 |-- 10. TON ga yechib olish ->|
```

#### Asosiy API Metodlari:
1. `createInvoiceLink`: Mini App ichida ochiladigan to'lov havolasini yaratish.
2. `sendInvoice`: To'g'ridan-to'g'ri Telegram chatida to'lov fakturasini yuborish.
3. `pre_checkout_query`: Telegram to'lov amalga oshirilishidan oldin botga so'rov yuboradi. Bot 10 soniya ichida `answerPreCheckoutQuery(ok=True)` deb javob qaytarishi shart.
4. `successful_payment`: To'lov muvaffaqiyatli o'tgach, botga yuboriladigan yakuniy xabar.

#### Bot API createInvoiceLink JSON So'rov Namunasi:
```json
// POST https://api.telegram.org/bot<BOT_TOKEN>/createInvoiceLink
{
  "title": "TaskBot 1 Oylik Premium",
  "description": "Cheksiz vazifalar, murakkab takrorlanish (RRULE) va ovozli kiritish",
  "payload": "{\"userId\":\"usr_94821\",\"plan\":\"MONTHLY\",\"created\":1728490000}",
  "currency": "XTR",
  "prices": [
    {
      "label": "1 Oylik Premium",
      "amount": 75
    }
  ]
}
```

---

### 3.3.2 Apple App Store va Google Play Qoidalariga Moslik

Apple App Store (Review Guideline 3.1.1) va Google Play qoidalariga ko'ra, iOS va Android mobil ilovalari ichida sotiladigan barcha raqamli xizmatlar (SaaS, obuna, o'yin ichidagi buyumlar) faqat do'konlarning In-App Purchase mexanizmlari orqali sotilishi kerak.
- Agar bot faqat Click yoki Payme orqali raqamli obuna sotsa, Apple yoki Google Telegram ilovasini o'z do'konidan bloklashi yoki cheklashi mumkin edi.
- **Telegram Stars bu muammoni to'liq hal qiladi**: Foydalanuvchilar Yulduzlarni (Stars) Apple Pay / Google Pay orqali sotib oladi (Apple/Google o'zining 30% komissiyasini oladi). Telegram esa ishlab chiquvchilarga Stars orqali raqamli xizmatlarni qonuniy sotish imkonini beradi.
- Natijada, botimiz Apple yoki Google tomonidan bloklanish xavfidan **100% himoyalangan** bo'ladi.

---

### 3.3.3 Yuridik Shaxs Talabisiz Butun Dunyodan To'lov Qabul Qilish va Fragment Orqali TON Ga Yechib Olish

Telegram Stars ning eng katta inqilobiy afzalligi:
1. **Yuridik shaxs yoki MChJ ochish shart emas**: Loyiha dastlabki bosqichida murakkab soliq, bank hisob raqamlari yoki qog'ozbozliksiz darhol butun dunyodagi (AQSH, Yevropa, Rossiya, Turkiya, Arab Amirliklari va hk.) istalgan foydalanuvchidan to'lov qabul qila oladi.
2. **Fragment.com orqali TON (The Open Network) ga yechish**:
   - To'plangan Yulduzlar to'lovdan 21 kun o'tgach **Fragment** platformasi orqali blokcheyndagi **Toncoin (TON)** kriptovalyutasiga aylantiriladi.
   - Toncoin ni istalgan xalqaro birjada (OKX, Bybit, Binance) sotish yoki to'g'ridan-to'g'ri bank kartalariga naqdlashtirish mumkin.
3. **Telegram Ads da 30% bonus bilan ishlatish**:
   - Agar ishlab chiquvchi to'plangan Yulduzlarni Toncoin ga naqdlashtirmasdan, botni reklama qilish uchun Telegram Ads platformasiga yo'naltirsa, Telegram hech qanday komissiya ushlamaydi va qo'shimcha **30% reklama byudjeti bonusi** taqdim etadi.

---

# 4. Mahalliy Valyutalardagi Narxlar Matritsasi va Unit Iqtisodiyot

## 4.1 Ko'p Valyutali Rasmiy Narxlar Matritsasi

Barcha narxlar mintaqaning xarid qobiliyati va valyuta kurslari mutanosibligi asosida qat'iy belgilangan:

| Tarif / Mahsulot | O'zbekiston (UZS) | Qozog'iston (KZT) | Telegram Stars (XTR) | AQSH Dollari Ekvivalenti | Foydalanuvchi Uchun Tejamkorlik |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1 Oylik Premium** | **19,000 so'm** | **990 ₸** | **75 ⭐** | ~$1.50 – $2.10 | Asosiy boshlang'ich narx |
| **6 Oylik Premium** | **99,000 so'm** | **4,990 ₸** | **390 ⭐** | ~$7.80 – $10.50 | **13% chegirma** |
| **1 Yillik Premium** | **169,000 so'm** | **8,990 ₸** | **690 ⭐** | ~$13.30 – $18.90 | **26% chegirma (Eng ommabop)** |
| **Umrbod Litsenziya (Lifetime)** | **299,000 so'm** | **15,900 ₸** | **1,200 ⭐** | ~$23.50 – $33.50 | Bir martalik to'lov (VIP) |
| **10 ta AI Task Breakdown** | **5,000 so'm** | **290 ₸** | **20 ⭐** | ~$0.40 – $0.60 | Mikro-to'lov paketi |
| **50 ta AI Task Breakdown** | **19,000 so'm** | **990 ₸** | **75 ⭐** | ~$1.50 – $2.10 | Katta mikro-to'lov paketi |
| **10 ta SMS Favqulodda Eslatma** | **3,000 so'm** | **180 ₸** | **15 ⭐** | ~$0.24 – $0.38 | Aloqa zaxira paketi |
| **1 ta PDF Hosildorlik Eksporti**| **2,000 so'm** | **120 ₸** | **10 ⭐** | ~$0.16 – $0.25 | Bir martalik eksport |

---

## 4.2 Nolinchi Server Xarajati ($0/oy) va Unit Iqtisodiyot Tahlili

Ushbu loyihaning boshqa barcha an'anaviy dasturiy ta'minot loyihalaridan tubdan farq qiluvchi strategik ustunligi — **100% bepul bulutli infratuzilma arxitekturasi** hisoblanadi (batafsil `ARCHITECTURE.md` hujjatida yoritilgan):

```
Infratuzilma Komponenti:           Oylik Server Xarajati:
- Cloudflare Workers (Backend API)          $0.00 (Kuniga 100,000 so'rov bepul)
- Cloudflare Pages (Mini App CDN)           $0.00 (Cheksiz trafik va so'rovlar)
- Supabase (PostgreSQL ma'lumotlar bazasi)  $0.00 (500 MB xotira, 50,000 MAU)
- Cloudflare Cron Triggers & QStash         $0.00 (Daqiqalik bepul rejalashtiruvchi)
----------------------------------------------------------------------------------
JAMI OYLIK SERVER XARAJATI:                 $0.00 / OY
```

### Unit Iqtisodiyot Formulasining Mohiyati:
Standart SaaS bizneslarda har bir yangi foydalanuvchi uchun hisoblash quvvati (CPU, RAM, Database hosting) sarflanadi va yalpi marja (Gross Margin) 60-80% ni tashkil qiladi. Bizning arxitekturamizda esa:
- Server tannarxi ($COGS_{server}$) = **0 so'm**.
- Barcha xarajatlar faqat to'lov shlyuzining komissiyasi ($Fee_{gateway}$) va davlat solig'idan ($Tax$) iborat.

$$\text{Gross Margin} = \frac{\text{Daromad} - \text{Shlyuz Komissiyasi}}{\text{Daromad}} \times 100\%$$

Mahalliy to'lov shlyuzlarida (Click, Payme) komissiya atigi **2.0% – 2.5%** bo'lgani sababli, har bir tushgan to'lovning **97.5% – 98% qismi toza foyda** (Gross Profit) bo'lib qoladi!

---

## 4.3 To'lov Shlyuzlari Komissiyalari va Sof Marja Taqqoslashi

Har bir to'lov kanali bo'yicha 1 oylik Premium obuna (19,000 so'm) misolida moliyaviy taqsimot:

| Ko'rsatkich | Click.uz | Payme | Uzum Pay | Kaspi Pay (KZT) | Telegram Stars |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **To'lov Summasi** | 19,000 so'm | 19,000 so'm | 19,000 so'm | 990 ₸ (~25,000 UZS) | 75 Stars (~20,000 UZS) |
| **Shlyuz Komissiyasi (%)** | **2.0%** | **2.0%** | **1.8%** | **2.3%** | **30.0%** (Apple/Google) |
| **Shlyuz Komissiyasi (Summa)**| 380 so'm | 380 so'm | 342 so'm | 23 ₸ (~575 UZS) | ~$0.45 (~5,700 UZS) |
| **Server Xarajati** | **0 so'm** | **0 so'm** | **0 so'm** | **0 so'm** | **0 so'm** |
| **Loyihaga Qoladigan Sof Tushum** | **18,620 so'm** | **18,620 so'm** | **18,658 so'm** | **967 ₸** | **~$1.05 (~13,300 UZS)** |
| **Sof Foyda Marjasi (%)** | **98.0%** | **98.0%** | **98.2%** | **97.7%** | **70.0%** |

*Xulosa*: Mahalliy to'lov kanallari (Click, Payme, Kaspi) rekord darajadagi **97.7% - 98.2% sof marja** beradi. Telegram Stars esa xalqaro foydalanuvchilar va In-App xavfsizligi evaziga **70% sof marja** taqdim etadi.

---

## 4.4 Foydalanuvchilar Soni Bo'yicha Moliyaviy Prognoz (1K, 5K, 25K MAU)

Foydalanuvchilar bazasining o'sishiga qarab konversiya ko'rsatkichlari:
- Faol foydalanuvchilardan Premiumga o'tish ko'rsatkichi (Conversion Rate): **4.5%**
- Reklama va mikro-billingdan olinadigan o'rtacha oylik daromad (bepul foydalanuvchi boshiga): **500 so'm**

### Moliyaviy Tahlil Jadvali:

| Ko'rsatkich | 1,000 MAU (Dastlabki Bosqich) | 5,000 MAU (Barqaror O'sish) | 25,000 MAU (Bozor Yetakchisi) |
| :--- | :---: | :---: | :---: |
| **Faol Foydalanuvchilar (MAU)** | 1,000 kishi | 5,000 kishi | 25,000 kishi |
| **Pullik Premium Obunachilar (4.5%)** | 45 kishi | 225 kishi | 1,125 kishi |
| **Oylik Premium Daromadi** (o'rtacha 19,000 so'm) | 855,000 so'm | 4,275,000 so'm | 21,375,000 so'm |
| **Yillik & Lifetime Paketlar Ulushi** | 500,000 so'm | 2,500,000 so'm | 12,500,000 so'm |
| **Mikro-Billing (AI & SMS paketlar)** | 350,000 so'm | 1,750,000 so'm | 8,750,000 so'm |
| **B2B Homiylik & Mahalliy Reklama** | 500,000 so'm | 2,500,000 so'm | 12,000,000 so'm |
| **JAMI OYLIK YALPI DAROMAD** | **2,205,000 so'm** | **11,025,000 so'm** | **54,625,000 so'm** |
| **To'lov Shlyuzlari Xarajati (~3%)** | -66,150 so'm | -330,750 so'm | -1,638,750 so'm |
| **Bulutli Server Xarajatlari** | **$0.00 (0 so'm)** | **$0.00 (0 so'm)** | **$0.00 (0 so'm)** |
| **OYLIK SOF DAROMAD (NET PROFIT)**| **2,138,850 so'm** | **10,694,250 so'm** | **52,986,250 so'm** |
| **SOF FOYDA RENTABELLIGI (%)** | **97.0%** | **97.0%** | **97.0%** |

---

# 5. Qonunchilik, Xavfsizlik va Litsenziyalash

## 5.1 O'zbekiston va Qozog'istonda Shaxsiy Ma'lumotlarni Saqlash Talablari

1. **O'zbekiston Respublikasi "Shaxsiy ma'lumotlar to'g'risida"gi O'RQ-547-son Qonuni**:
   - Qonunning 27-1-moddasiga binoan, O'zbekiston fuqarolarining shaxsiy ma'lumotlariga raqamli ishlov berishda ularning ma'lumotlar bazalari O'zbekiston Respublikasi hududida joylashgan bo'lishi talab etiladi.
   - Loyiha foydalanuvchilarning pasport ma'lumotlari yoki biometriyasini saqlamaydi. Foydalanuvchilar faqat Telegram ID va anonim vazifalar matnlari bilan belgilanadi.
2. **Qozog'iston Respublikasining 2013-yil 21-maydagi "Shaxsiy ma'lumotlar va ularni himoya qilish to'g'risida"gi Qonuni**:
   - Ma'lumotlar xavfsizligi va maxfiyligi shifrlash (TLS 1.3, AES-256) orqali to'liq ta'minlanadi.

---

## 5.2 PCI-DSS Cheklovlari va Karta Ma'lumotlarini Saqlamaslik Siyosati

- Tizim hech qanday holatda foydalanuvchining bank karta raqamlarini, amal qilish muddatlarini yoki PIN/CVV kodlarini o'z serverida yoki ma'lumotlar bazasida **saqlamaydi va qayta ishlamaydi**.
- Barcha to'lov amaliyotlari to'liq litsenziyaga ega bo'lgan to'lov tashkilotlarining (**Click**, **Payme**, **Uzum**, **Kaspi**, **Telegram**) xavfsiz shlyuzlarida bajariladi. Bu loyihani murakkab va qimmatbaho PCI-DSS Level 1 sertifikatlash byurokratiyasidan ozod qiladi.

---

## 5.3 Anti-Fraud va Qaytarilgan Tranzaksiyalarni (Chargeback) Boshqarish

1. **Idempotentlik Kalitlari (Idempotency Keys)**:
   Tarmoqdagi uzilishlar tufayli to'lov qayta yuborilganda foydalanuvchidan ikki marta pul yechilmasligi yoki bazada takroriy obuna ochilmasligi uchun har bir to'lov `transaction_id` bo'yicha unikal indekslanadi.
2. **To'lovni Bekor Qilish (Refund/Cancel)**:
   Agar foydalanuvchi xizmatdan norozi bo'lib to'lovni qaytarishni so'rasa, Payme `CancelTransaction` yoki Click orqali mablag' qaytariladi va tizimda Premium obuna muddati avtomatik ravishda bekor qilinadi.

---

# 6. Amalga Oshirish Yo'l Xaritasi (FinTech Roadmap)

Monetizatsiya va to'lov tizimlarini bosqichma-bosqich ishlab chiqarishga kiritish rejasi:

```
+--------------------------------------------------------------------------------------------------+
|                            MONETIZATSIYA YO'L XARITASI (FINTECH ROADMAP)                         |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   1-BOSQICH (1-Hafta): MVP & TELEGRAM STARS                                                      |
|   - Telegram Bot API 7.4+ createInvoiceLink va openInvoice integratsiyasi                        |
|   - 7 kunlik Free Trial voronkasi va 50 ta vazifa limiti hisoblagichini o'rnatish                |
|   - Xalqaro va sinov to'lovlarini darhol boshlash (Yuridik shaxssiz)                             |
|                                                                                                  |
|   2-BOSQICH (2-3-Hafta): O'ZBEKISTON MILLIY SHLYUZLARI (CLICK VA PAYME)                         |
|   - Click Shop API (Prepare / Complete) webhook routerini ishga tushirish                        |
|   - Payme JSON-RPC 2.0 protokoli va Soliq OFD IKPU 10899001001000000 chekini ulash             |
|   - Uzcard va Humo foydalanuvchilarining 98% qamrovini ta'minlash                                |
|                                                                                                  |
|   3-BOSQICH (4-5-Hafta): QOZOG'ISTON BOZORIGA CHIQISH (KASPI PAY VA EPAY)                       |
|   - Kaspi Pay dinamik QR va Deep Link to'lov tizimini sozlash                                    |
|   - Halyk Epay orqali Visa/Mastercard integratsiyasi                                             |
|                                                                                                  |
|   4-BOSQICH (6-Hafta va keyin): MIKRO-BILLING VA B2B HOMIYLIK EKOTIZIMI                         |
|   - AI Task Breakdown 10 talik paketlarini joriy qilish                                          |
|   - Eskiz.uz orqali Favqulodda SMS ogohlantirish kreditlarini sotish                             |
|   - Mahalliy bizneslar bilan B2B homiylik eslatmalari shartnomalarini tuzish                     |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

---

*Hujjat Worker 4 (Monetizatsiya va FinTex Mutaxassisi) tomonidan ishlab chiqildi va loyiha arxitekturasiga to'liq integratsiya qilindi.*
