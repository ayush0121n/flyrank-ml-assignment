# Make It Do Something — Plain-words explainer

**Feature:** One working contact form on the portfolio.  
**Live page:** https://ayush0121n.github.io/flyrank-ml-assignment/contact.html  
**Portfolio:** https://ayushdevxx.vercel.app/

---

## What a backend is (in plain words)

The browser only shows pages and runs small scripts. It cannot safely send email from your personal address or store messages by itself. A **backend** is the part that runs on a server (not on the visitor’s laptop). It receives the form data, checks it, and does the real work — here, delivering the message to my inbox.

I did not write my own server. I used a free form backend (Web3Forms). That service *is* the backend for this one feature.

## What the feature does

Someone opens the contact page, types their name, email, and message, and clicks Send.  
A few seconds later that message arrives in my real email inbox. That is the whole product: one reliable path from visitor → me.

## How the data flows (step by step)

1. **Visitor fills the form** in the browser (name, email, message).
2. **Browser sends an HTTPS POST** to `https://api.web3forms.com/submit` with those fields plus my private access key (the key is in the page as a hidden field; it only authorises *this* form).
3. **Web3Forms (the backend)** receives the request, verifies the key, and emails the contents to the address I registered when I created the form.
4. **I open my inbox** and see the message. No account is created for the visitor; nothing is stored on my portfolio host.

If the key is missing or wrong, the form shows an error and nothing is sent. If the key is valid, the success message appears and the email arrives.

## Why only one feature

The assignment asks for exactly one working end-to-end path. A contact form is the most useful single feature for a portfolio: it turns a static page into something a real person can use to reach me. Adding more half-wired features would dilute the proof that this one path works.

## Free tier

Web3Forms free tier is enough for portfolio volume. The page itself is static HTML hosted on GitHub Pages (also free, HTTPS automatic). No credit card, no custom server.

---

*Ayush Narkhede · General AI Fluency · Make It Do Something*
