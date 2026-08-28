# DNS Walkthrough — What Actually Happens When Someone Types a Website Address

*(Written for a non-technical teammate)*

When you type a website address like `ayush0121n.github.io` into a browser and press Enter, a short chain of lookups happens before any page appears. That chain is DNS — the Domain Name System. It is the internet’s phone book.

## The simple version

Computers talk to each other using numbers called IP addresses (for example `185.199.108.153`). Humans prefer names. DNS is the system that translates the name you typed into the number the computer needs.

## Step by step

1. **You type the address**  
   Your browser asks the local resolver (usually your ISP or a public service like Cloudflare’s 1.1.1.1) for the IP of that name.

2. **The resolver asks the nameservers**  
   If the resolver does not already know the answer (from a recent lookup), it contacts the authoritative nameservers for that domain. Those nameservers are the official source of truth for the domain’s records.

3. **The record that answers**  
   The nameserver returns a DNS record. The two most common ones you will hear about are:
   - **A record** — maps a name directly to an IPv4 address.
   - **CNAME record** — maps a name to *another name*. The second name is then looked up until an A record is found.  
     Example: many people point `www.example.com` as a CNAME to `example.com`, or point a custom domain as a CNAME to `username.github.io` so GitHub Pages can serve the site.

4. **The response comes back**  
   The resolver receives the IP, caches it for a short time (so the next request is faster), and hands the IP to your browser.

5. **The host answers**  
   Your browser opens a connection to that IP address over HTTPS. The server (GitHub Pages, Netlify, etc.) returns the HTML, CSS, and other files of the site. The padlock you see means the connection is encrypted; the certificate is almost always issued automatically by the host.

## Why this matters for a personal site

When you later connect your own domain (for example `ayushnarkhede.com`) to GitHub Pages or Netlify, you will usually create a **CNAME** (or A) record that points your domain at the host’s address. You are not moving the files; you are only telling the world’s phone book “when someone asks for my domain, send them to this host.” Once the record propagates, the same files that were already live on the free host URL become reachable at your own domain.

No custom domain is required for this assignment. Understanding the steps above means that if you ever do connect one, you will know what the CNAME is doing instead of just following a checklist.

---

*Ayush Narkhede · PF-04 DNS walkthrough · August 2026*
